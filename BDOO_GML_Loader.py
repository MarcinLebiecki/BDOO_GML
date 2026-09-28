# -*- coding: utf-8 -*-
"""Wtyczka QGIS do wczytywania i symbolizacji danych BDOO."""

import re
import shutil
import zipfile
from pathlib import Path, PurePosixPath

from qgis.PyQt.QtCore import QCoreApplication, QSettings, QTranslator, Qt
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import (
    QAction,
    QApplication,
    QFileDialog,
    QMenu,
    QMessageBox,
    QProgressBar,
)
from qgis.core import (
    Qgis,
    QgsApplication,
    QgsCoordinateReferenceSystem,
    QgsCoordinateTransform,
    QgsMessageLog,
    QgsProject,
    QgsVectorFileWriter,
    QgsVectorLayer,
)

from . import resources
from .constants import WOJEWODZTWA
from .geoportal import GeoportalDownloadDialog, download_geoportal_zip
from .help_tools import download_bdoo_regulation, show_about_dialog
from .layer_specs import LAYER_SPECS


# Obsługujemy historycznie spotykane rozszerzenia GML/XML oraz SHP.
# Typowa przestrzeń nazw ma postać PL.PZGiK.201.14. Wyrażenie dopuszcza też
# dodatkowy człon (np. BDOO) przed identyfikatorem terytorialnym, aby nie
# blokować paczek o nieco innej konwencji nazewniczej.
_DATA_FILE_RE = re.compile(
    r"^(PL\.PZGiK\.201(?:\.[A-Za-z0-9_-]+)*)__OT_.+\.(gml|xml|shp)$",
    re.IGNORECASE,
)

_SETTINGS_GROUP = "BDOO_GML_Loader"


class BDOO_GML_Loader:
    """Główna klasa wtyczki BDOO_GML_Loader."""

    def __init__(self, iface):
        """Zapisz interfejs QGIS i przygotuj tłumaczenia wtyczki."""
        self.iface = iface
        self.plugin_dir = Path(__file__).resolve().parent

        locale = str(QSettings().value("locale/userLocale", "en"))[:2]
        locale_path = self.plugin_dir / "i18n" / f"BDOO_GML_Loader_{locale}.qm"
        if locale_path.is_file():
            self.translator = QTranslator()
            self.translator.load(str(locale_path))
            QCoreApplication.installTranslator(self.translator)

        self.actions = []
        self.menu = self.tr("&BDOO_GML")
        self.first_start = None
        self._available_source_uris = None

    @staticmethod
    def tr(message):
        """Zwróć przetłumaczony tekst interfejsu."""
        return QCoreApplication.translate("BDOO_GML_Loader", message)

    def add_action(
        self,
        icon_path,
        text,
        callback,
        enabled_flag=True,
        add_to_menu=True,
        add_to_toolbar=True,
        status_tip=None,
        whats_this=None,
        parent=None,
    ):
        """Dodaj akcję wtyczki do menu i opcjonalnie do paska narzędzi."""
        action = QAction(QIcon(icon_path), text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)
            action.setToolTip(status_tip)
        if whats_this is not None:
            action.setWhatsThis(whats_this)
        if add_to_toolbar:
            self.iface.addToolBarIcon(action)
        if add_to_menu:
            self.iface.addPluginToMenu(self.menu, action)

        self.actions.append(action)
        return action

    def initGui(self):
        """Utwórz pozycję menu i ikonę wtyczki."""
        self.add_action(
            str(self.plugin_dir / "icon.png"),
            text=self.tr("Wczytaj dane BDOO"),
            callback=self.run,
            status_tip=self.tr(
                "Wczytaj dane BDOO z katalogu, pliku ZIP albo pobierz je z Geoportalu."
            ),
            whats_this=self.tr(
                "Pozwala wskazać lokalne dane BDOO lub pobrać paczkę dla wybranego "
                "województwa albo całego kraju z Geoportalu GUGiK."
            ),
            parent=self.iface.mainWindow(),
        )
        self.first_start = True

    def unload(self):
        """Usuń elementy interfejsu dodane przez wtyczkę."""
        for action in self.actions:
            self.iface.removePluginMenu(self.menu, action)
            self.iface.removeToolBarIcon(action)

    def run(self):
        """Wybierz źródło BDOO, zweryfikuj je i wczytaj warstwy."""
        if self.first_start:
            self.first_start = False

        source = self._select_source()
        if source is None:
            return

        if source[0] == "country":
            self._load_country_sources(source[1])
            return

        dataset = self._prepare_source(*source)
        if dataset is None:
            return

        self._load_dataset(**dataset)

    def _close_plugin_windows(self):
        """Zamknij wszystkie aktualnie otwarte okna należące do wtyczki."""
        for widget in QApplication.topLevelWidgets():
            if widget.property("BDOO_GML_Loader_window"):
                widget.close()

    def _select_source(self):
        """Pozwól wybrać lokalne dane BDOO albo pobrać je z Geoportalu."""
        settings = QSettings()
        start_path = str(settings.value(f"{_SETTINGS_GROUP}/lastSource", ""))

        choice = QMessageBox(self.iface.mainWindow())
        choice.setProperty("BDOO_GML_Loader_window", True)
        choice.setWindowTitle("Źródło danych BDOO")
        choice.setIcon(QMessageBox.Question)
        choice.setText("Wybierz sposób wczytania danych BDOO.")

        folder_button = choice.addButton("katalog", QMessageBox.AcceptRole)
        folder_button.setToolTip(
            "Wskaż katalog zawierający dane BDOO w formacie GML/XML albo SHP."
        )
        zip_button = choice.addButton("plik ZIP", QMessageBox.AcceptRole)
        zip_button.setToolTip(
            "Wskaż plik ZIP zawierający dane BDOO. Archiwum nie będzie rozpakowywane."
        )
        geoportal_button = choice.addButton("Geoportal", QMessageBox.ActionRole)
        geoportal_button.setToolTip(
            "Wybierz województwo albo cały kraj, pobierz paczkę BDOO z Geoportalu "
            "GUGiK i automatycznie wczytaj ją do QGIS."
        )

        # HelpRole nie zamyka okna źródła danych. Użytkownik może otworzyć
        # rozporządzenie lub informacje, a następnie wrócić do wyboru danych.
        help_button = choice.addButton("Pomoc", QMessageBox.HelpRole)
        help_button.setToolTip(
            "Otwórz menu pomocy z rozporządzeniem BDOO i informacjami o wtyczce."
        )
        help_menu = QMenu(help_button)
        help_menu.setToolTipsVisible(True)

        regulation_action = help_menu.addAction("Rozporządzenie BDOO (PDF)")
        regulation_action.setToolTip(
            "Pobierz oficjalny tekst rozporządzenia dotyczącego BDOO z systemu ELI."
        )
        regulation_action.triggered.connect(lambda: download_bdoo_regulation(choice))

        help_menu.addSeparator()
        info_action = help_menu.addAction("Informacje")
        info_action.setToolTip(
            "Wyświetl informacje o wtyczce, jej wersji, właścicielu i repozytorium."
        )
        info_action.triggered.connect(
            lambda: show_about_dialog(
                choice,
                self.plugin_dir,
                self._close_plugin_windows,
            )
        )
        help_button.setMenu(help_menu)

        cancel_button = choice.addButton("Anuluj", QMessageBox.RejectRole)
        cancel_button.setToolTip("Zamknij okno bez wczytywania danych.")

        choice.exec_()
        clicked = choice.clickedButton()

        if clicked is folder_button:
            folder = QFileDialog.getExistingDirectory(
                self.iface.mainWindow(),
                "Wybierz katalog BDOO",
                start_path,
            )
            if not folder:
                return None

            folder_path = Path(folder)
            settings.setValue(f"{_SETTINGS_GROUP}/lastSource", str(folder_path.parent))
            return "folder", folder_path

        if clicked is zip_button:
            zip_name, _ = QFileDialog.getOpenFileName(
                self.iface.mainWindow(),
                "Wybierz plik ZIP z danymi BDOO",
                start_path,
                "Archiwa ZIP (*.zip)",
            )
            if not zip_name:
                return None

            zip_path = Path(zip_name)
            settings.setValue(f"{_SETTINGS_GROUP}/lastSource", str(zip_path.parent))
            return "zip", zip_path

        if clicked is geoportal_button:
            dialog = GeoportalDownloadDialog(self.iface.mainWindow())
            dialog.setProperty("BDOO_GML_Loader_window", True)
            if dialog.exec_() != dialog.Accepted:
                return None

            selected_teryt = dialog.selected_teryt()
            download_country = dialog.download_all_country() or selected_teryt == "00"

            if download_country:
                zip_paths = []
                voivodeships = [
                    code for code in sorted(WOJEWODZTWA) if code != "00"
                ]
                for index, code in enumerate(voivodeships, start=1):
                    zip_path = download_geoportal_zip(
                        self.iface.mainWindow(),
                        code,
                        dialog.destination_directory(),
                        batch_index=index,
                        batch_total=len(voivodeships),
                    )
                    if zip_path is None:
                        return None
                    zip_paths.append(zip_path)

                if not zip_paths:
                    return None

                settings.setValue(
                    f"{_SETTINGS_GROUP}/lastSource", str(zip_paths[0].parent)
                )
                return "country", zip_paths

            zip_path = download_geoportal_zip(
                self.iface.mainWindow(),
                selected_teryt,
                dialog.destination_directory(),
            )
            if zip_path is None:
                return None

            settings.setValue(f"{_SETTINGS_GROUP}/lastSource", str(zip_path.parent))
            return "zip", zip_path

        return None

    def _load_country_sources(self, zip_paths):
        """Scal 16 wojewódzkich paczek BDOO do jednego GeoPackage i wczytaj go."""
        root = QgsProject.instance().layerTreeRoot()
        country_namespace = "PL.PZGiK.201.00"
        country_group_name = "BDOO POLSKA"

        if self._dataset_already_loaded(root, country_namespace, country_group_name):
            if not self._confirm_duplicate(country_namespace, country_group_name):
                return

        datasets = []
        for zip_path in zip_paths:
            dataset = self._prepare_source("zip", zip_path)
            if dataset is None:
                QMessageBox.warning(
                    self.iface.mainWindow(),
                    "BDOO",
                    "Nie udało się przygotować wszystkich wojewódzkich paczek BDOO. "
                    "Tworzenie danych dla całego kraju zostało przerwane.",
                )
                return
            datasets.append(dataset)

        if not datasets:
            return

        country_gpkg = self._convert_country_to_gpkg(datasets)
        if country_gpkg is None:
            return

        loaded = self._load_dataset(
            path="",
            przestrzen_nazw=country_namespace,
            formatPliku="gpkg",
            source_type="gpkg",
            source_path=country_gpkg,
            source_records=[],
            available_source_uris=None,
            skip_duplicate_check=True,
            gpkg_path_override=country_gpkg,
        )

        if loaded:
            self.iface.messageBar().pushSuccess(
                "BDOO",
                "Wczytano BDOO dla całego kraju z jednego GeoPackage: "
                f"{country_gpkg.name}",
            )

    def _convert_country_to_gpkg(self, datasets):
        """Zapisz dane 16 województw do jednego GPKG, po jednej tabeli na klasę."""
        if not datasets:
            return None

        first_source = Path(datasets[0]["source_path"])
        gpkg_path = self._unique_path(first_source.parent / "BDOO_POLSKA.gpkg")
        written_tables = set()
        total_records = sum(len(dataset["source_records"]) for dataset in datasets)

        progress_message = self.iface.messageBar().createMessage(
            "Tworzenie wspólnego GeoPackage BDOO dla całego kraju..."
        )
        progress = QProgressBar()
        progress.setMaximum(max(total_records, 1))
        progress.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        progress_message.layout().addWidget(progress)
        self.iface.messageBar().pushWidget(progress_message, Qgis.Info)

        progress_value = 0
        try:
            for dataset in datasets:
                ok, processed = self._append_records_to_gpkg(
                    path=dataset["path"],
                    source_type=dataset["source_type"],
                    source_path=dataset["source_path"],
                    source_records=dataset["source_records"],
                    gpkg_path=gpkg_path,
                    written_tables=written_tables,
                    progress=progress,
                    progress_start=progress_value,
                )
                progress_value += processed
                if not ok:
                    try:
                        gpkg_path.unlink(missing_ok=True)
                    except OSError:
                        pass
                    return None
        finally:
            self.iface.messageBar().clearWidgets()

        if not written_tables or not gpkg_path.is_file():
            try:
                gpkg_path.unlink(missing_ok=True)
            except OSError:
                pass
            QMessageBox.warning(
                self.iface.mainWindow(),
                "BDOO",
                "Nie utworzono wspólnego pliku GeoPackage dla danych krajowych.",
            )
            return None

        return gpkg_path

    def _prepare_source(self, source_type, source_path):
        """Rozpoznaj przestrzeń nazw i format danych dla katalogu albo ZIP."""
        try:
            if source_type == "folder":
                records = self._scan_folder(source_path)
            else:
                records = self._scan_zip(source_path)
        except (OSError, zipfile.BadZipFile) as exc:
            QMessageBox.critical(
                self.iface.mainWindow(),
                "BDOO",
                f"Nie można odczytać wskazanego źródła:\n{exc}",
            )
            return None

        if not records:
            QMessageBox.warning(
                self.iface.mainWindow(),
                "BDOO",
                "Nie znaleziono plików BDOO w formacie GML/XML ani SHP.",
            )
            return None

        locations = sorted({(record["parent"], record["namespace"]) for record in records})
        if len(locations) != 1:
            names = "\n".join(
                f"• {namespace}" + (f" ({parent})" if parent else "")
                for parent, namespace in locations[:10]
            )
            QMessageBox.warning(
                self.iface.mainWindow(),
                "BDOO",
                "Wskazane źródło zawiera więcej niż jeden zbiór BDOO. "
                "Wskaż katalog lub ZIP zawierający jeden zbiór.\n\n" + names,
            )
            return None

        parent, namespace = locations[0]
        selected_records = [
            record
            for record in records
            if record["parent"] == parent and record["namespace"] == namespace
        ]
        formats = sorted({record["format"] for record in selected_records})
        data_format = self._choose_format(formats)
        if data_format is None:
            return None

        selected_records = [
            record for record in selected_records if record["format"] == data_format
        ]

        if source_type == "folder":
            data_directory = source_path.resolve()
            if parent:
                data_directory = data_directory / Path(parent)
            prefix = data_directory.as_posix().rstrip("/") + "/"
            self._available_source_uris = None
        else:
            # GDAL/QGIS czyta GML/XML i SHP bezpośrednio z ZIP przez /vsizip/.
            # Dzięki temu nie tworzymy katalogów tymczasowych i nie pozostawiamy
            # rozpakowanych danych na dysku użytkownika.
            zip_prefix = f"/vsizip/{source_path.resolve().as_posix()}"
            if parent:
                zip_prefix += "/" + parent.strip("/")
            prefix = zip_prefix.rstrip("/") + "/"
            self._available_source_uris = {
                prefix + PurePosixPath(record["member"]).name
                for record in selected_records
            }

        return {
            "path": prefix,
            "przestrzen_nazw": namespace,
            "formatPliku": data_format,
            "source_type": source_type,
            "source_path": source_path,
            "source_records": selected_records,
            "available_source_uris": (
                None
                if self._available_source_uris is None
                else set(self._available_source_uris)
            ),
        }

    @staticmethod
    def _scan_folder(folder_path):
        """Zwróć rozpoznane pliki BDOO z katalogu lub pojedynczego podkatalogu."""
        records = []
        folder_path = folder_path.resolve()

        for item in folder_path.rglob("*"):
            if not item.is_file():
                continue

            match = _DATA_FILE_RE.match(item.name)
            if not match:
                continue

            relative_parent = item.parent.relative_to(folder_path).as_posix()
            parent = "" if relative_parent == "." else relative_parent
            records.append(
                {
                    "parent": parent,
                    "namespace": match.group(1),
                    "format": match.group(2).lower(),
                    "member": item.name,
                }
            )

        return records

    @staticmethod
    def _scan_zip(zip_path):
        """Zwróć rozpoznane pliki BDOO z ZIP, także z katalogu nadrzędnego."""
        records = []
        with zipfile.ZipFile(zip_path, "r") as archive:
            for member in archive.namelist():
                if member.endswith("/"):
                    continue

                pure = PurePosixPath(member)
                match = _DATA_FILE_RE.match(pure.name)
                if not match:
                    continue

                parent = "" if str(pure.parent) == "." else pure.parent.as_posix()
                records.append(
                    {
                        "parent": parent,
                        "namespace": match.group(1),
                        "format": match.group(2).lower(),
                        "member": member,
                    }
                )

        return records

    def _choose_format(self, formats):
        """W razie obecności SHP i GML/XML pozwól użytkownikowi wybrać format."""
        formats = set(formats)
        text_formats = [fmt for fmt in ("gml", "xml") if fmt in formats]
        has_shp = "shp" in formats

        if text_formats and not has_shp:
            # Preferujemy GML, jeżeli źródło zawiera równolegle GML i XML.
            return text_formats[0]
        if has_shp and not text_formats:
            return "shp"
        if not text_formats and not has_shp:
            return None

        dialog = QMessageBox(self.iface.mainWindow())
        dialog.setWindowTitle("Format danych BDOO")
        dialog.setIcon(QMessageBox.Question)
        dialog.setText(
            "Znaleziono jednocześnie dane GML/XML i SHP. Wybierz format do wczytania."
        )
        gml_button = dialog.addButton("Wczytaj dane GML / XML", QMessageBox.AcceptRole)
        gml_button.setToolTip(
            "Wczytaj dane GML/XML i zastosuj style kartograficzne wtyczki."
        )
        shp_button = dialog.addButton("Wczytaj dane SHP", QMessageBox.AcceptRole)
        shp_button.setToolTip(
            "Wczytaj dane SHP i zastosuj style kartograficzne wtyczki."
        )
        cancel_button = dialog.addButton("Anuluj", QMessageBox.RejectRole)
        cancel_button.setToolTip("Zamknij okno bez wczytywania danych.")
        dialog.exec_()

        clicked = dialog.clickedButton()
        if clicked is gml_button:
            return text_formats[0]
        if clicked is shp_button:
            return "shp"
        return None

    def _source_exists(self, uri):
        """Sprawdź istnienie pliku zarówno na dysku, jak i wewnątrz ZIP."""
        if self._available_source_uris is not None:
            return uri in self._available_source_uris
        return Path(uri).is_file()

    @staticmethod
    def _table_name_from_record(record):
        """Zwróć nazwę klasy BDOO na podstawie nazwy pliku źródłowego."""
        file_name = PurePosixPath(record["member"]).name
        try:
            data_part = file_name.split("__", 1)[1]
            return data_part.rsplit(".", 1)[0]
        except (IndexError, ValueError):
            return Path(file_name).stem

    @staticmethod
    def _default_gpkg_path(source_type, source_path, namespace):
        """Wyznacz lokalizację wspólnego GeoPackage dla danych GML/XML."""
        file_name = f"{namespace}_BDOO.gpkg"
        if source_type == "folder":
            return source_path / file_name
        return source_path.parent / file_name

    @staticmethod
    def _unique_path(path):
        """Zwróć wolną nazwę pliku, dodając numer, gdy plik już istnieje."""
        if not path.exists():
            return path

        counter = 2
        while True:
            candidate = path.with_name(f"{path.stem}_{counter}{path.suffix}")
            if not candidate.exists():
                return candidate
            counter += 1

    @staticmethod
    def _text_source_uri(path, record):
        """Zbuduj URI pliku źródłowego znajdującego się w katalogu albo ZIP."""
        return f"{path}{PurePosixPath(record['member']).name}"

    @staticmethod
    def _text_record_has_features(source_type, source_path, path, record, table_name):
        """Awaryjnie sprawdź, czy źródłowy GML/XML zawiera obiekty."""
        table_name_bytes = table_name.encode("utf-8")
        class_tag = re.compile(
            rb"<(?:[A-Za-z_][A-Za-z0-9_.-]*:)?"
            + re.escape(table_name_bytes)
            + rb"(?=[\s/>])",
            re.IGNORECASE,
        )
        member_tag = re.compile(
            rb"<(?:[A-Za-z_][A-Za-z0-9_.-]*:)?(?:featureMember|member)(?=[\s>])",
            re.IGNORECASE,
        )
        any_bdoo_tag = re.compile(
            rb"<(?:[A-Za-z_][A-Za-z0-9_.-]*:)?OT_[A-Za-z0-9_]+(?=[\s/>])",
            re.IGNORECASE,
        )

        def stream_has_feature(stream):
            tail = b""
            while True:
                chunk = stream.read(64 * 1024)
                if not chunk:
                    return False
                data = tail + chunk
                if (
                    class_tag.search(data)
                    or member_tag.search(data)
                    or any_bdoo_tag.search(data)
                ):
                    return True
                tail = data[-1024:]

        if source_type == "zip":
            with zipfile.ZipFile(source_path, "r") as archive:
                with archive.open(record["member"], "r") as stream:
                    return stream_has_feature(stream)

        file_path = Path(path) / PurePosixPath(record["member"]).name
        with file_path.open("rb") as stream:
            return stream_has_feature(stream)

    def _append_records_to_gpkg(
        self,
        path,
        source_type,
        source_path,
        source_records,
        gpkg_path,
        written_tables,
        progress=None,
        progress_start=0,
    ):
        """Dopisz rekordy źródłowe do GPKG, łącząc województwa według klas."""
        records = sorted(
            source_records,
            key=lambda r: PurePosixPath(r["member"]).name.lower(),
        )
        if not records:
            return True, 0

        transform_context = QgsProject.instance().transformContext()
        target_crs = QgsCoordinateReferenceSystem("EPSG:2180")
        seen_in_dataset = set()
        processed = 0

        for record in records:
            processed += 1
            table_name = self._table_name_from_record(record)
            if table_name in seen_in_dataset:
                if progress is not None:
                    self._set_progress(progress, progress_start + processed)
                continue
            seen_in_dataset.add(table_name)

            source_uri = self._text_source_uri(path, record)
            source_layer = None
            for candidate_uri in (
                f"{source_uri}|layername={table_name}",
                source_uri,
            ):
                candidate_layer = QgsVectorLayer(candidate_uri, table_name, "ogr")
                if not candidate_layer.isValid():
                    continue
                try:
                    feature_count = candidate_layer.featureCount()
                except Exception:
                    feature_count = -1
                if feature_count > 0:
                    source_layer = candidate_layer
                    break

            if source_layer is None:
                try:
                    has_features = self._text_record_has_features(
                        source_type,
                        source_path,
                        path,
                        record,
                        table_name,
                    ) if record["format"] in ("gml", "xml") else False
                except (OSError, KeyError, zipfile.BadZipFile) as exc:
                    QMessageBox.critical(
                        self.iface.mainWindow(),
                        "BDOO",
                        "Nie można odczytać pliku podczas sprawdzania zawartości:\n"
                        f"{source_uri}\n\nBłąd: {exc}",
                    )
                    return False, processed

                if not has_features:
                    if progress is not None:
                        self._set_progress(progress, progress_start + processed)
                    continue

                QMessageBox.critical(
                    self.iface.mainWindow(),
                    "BDOO",
                    "Plik zawiera obiekty, ale OGR nie potrafi odczytać warstwy "
                    f"{table_name}:\n{source_uri}",
                )
                return False, processed

            options = QgsVectorFileWriter.SaveVectorOptions()
            options.driverName = "GPKG"
            options.fileEncoding = "UTF-8"
            options.layerName = table_name

            source_crs = source_layer.crs()
            if not source_crs.isValid():
                source_layer.setCrs(target_crs)
            elif source_crs != target_crs:
                options.ct = QgsCoordinateTransform(
                    source_crs,
                    target_crs,
                    transform_context,
                )

            if not gpkg_path.exists():
                options.actionOnExistingFile = QgsVectorFileWriter.CreateOrOverwriteFile
            elif table_name in written_tables:
                options.actionOnExistingFile = QgsVectorFileWriter.AppendToLayerNoNewFields
            else:
                options.actionOnExistingFile = QgsVectorFileWriter.CreateOrOverwriteLayer

            result = QgsVectorFileWriter.writeAsVectorFormatV3(
                source_layer,
                str(gpkg_path),
                transform_context,
                options,
            )
            error = result[0]
            error_message = result[1] if len(result) > 1 else ""
            if error != QgsVectorFileWriter.NoError:
                QMessageBox.critical(
                    self.iface.mainWindow(),
                    "BDOO",
                    "Nie udało się zapisać danych do GeoPackage.\n\n"
                    f"Klasa: {table_name}\n"
                    f"Źródło: {source_uri}\n"
                    f"Błąd: {error_message or error}",
                )
                return False, processed

            written_tables.add(table_name)
            if progress is not None:
                self._set_progress(progress, progress_start + processed)

        return True, processed

    def _convert_text_to_gpkg(
        self,
        path,
        przestrzen_nazw,
        source_type,
        source_path,
        source_records,
        progress=None,
    ):
        """Zapisz wszystkie pliki GML/XML jednego zbioru BDOO do GeoPackage."""
        text_records = [
            record
            for record in source_records
            if record["format"] in ("gml", "xml")
        ]
        if not text_records:
            return None

        gpkg_path = self._unique_path(
            self._default_gpkg_path(source_type, source_path, przestrzen_nazw)
        )
        written_tables = set()
        ok, _ = self._append_records_to_gpkg(
            path=path,
            source_type=source_type,
            source_path=source_path,
            source_records=text_records,
            gpkg_path=gpkg_path,
            written_tables=written_tables,
            progress=progress,
            progress_start=0,
        )

        if not ok:
            try:
                gpkg_path.unlink(missing_ok=True)
            except OSError:
                pass
            return None

        if not written_tables:
            QMessageBox.information(
                self.iface.mainWindow(),
                "BDOO",
                "Wszystkie pliki GML/XML są puste. Nie utworzono pliku "
                "GeoPackage ani warstw w projekcie.",
            )
            return None

        if not gpkg_path.is_file():
            QMessageBox.critical(
                self.iface.mainWindow(),
                "BDOO",
                "Nie utworzono pliku GeoPackage z danych GML/XML.",
            )
            return None

        return gpkg_path

    def _install_svg_symbols(self):
        """Skopiuj symbole KARTO250k do katalogu SVG profilu QGIS."""
        source = self.plugin_dir / "BDOO_SVG" / "KARTO250k"
        destination = Path(QgsApplication.qgisSettingsDirPath()) / "SVG" / "KARTO250k"

        if not source.is_dir():
            QgsMessageLog.logMessage(
                f"Nie znaleziono katalogu symboli: {source}",
                "BDOO_GML_Loader",
                Qgis.Warning,
            )
            return

        try:
            shutil.copytree(source, destination, dirs_exist_ok=True)
        except OSError as exc:
            QgsMessageLog.logMessage(
                f"Nie udało się skopiować symboli KARTO250k: {exc}",
                "BDOO_GML_Loader",
                Qgis.Warning,
            )

    @staticmethod
    def _set_progress(progress, value):
        """Ustaw postęp i pozwól Qt odświeżyć interfejs podczas importu."""
        progress.setValue(value)
        QCoreApplication.processEvents()

    def _add_configured_layer(
        self,
        spec,
        path,
        przestrzen_nazw,
        formatPliku,
        target_group,
        root,
        qml_path,
        gpkg_path=None,
    ):
        """Wczytaj pojedynczą warstwę opisaną w ``LAYER_SPECS``."""
        if gpkg_path is not None:
            source_uri = f"{gpkg_path}|layername={spec['source']}"
        else:
            source_uri = f"{path}{przestrzen_nazw}__{spec['source']}.{formatPliku}"
            if not self._source_exists(source_uri):
                return None

        style_path = qml_path / spec["style"]
        if not style_path.is_file():
            QgsMessageLog.logMessage(
                f"Pominięto warstwę {spec['name']}: brak stylu {style_path.name}.",
                "BDOO_GML_Loader",
                Qgis.Warning,
            )
            return None

        layer = QgsVectorLayer(
            source_uri,
            f"{przestrzen_nazw}__{spec['name']}",
            "ogr",
        )
        if not layer.isValid():
            QgsMessageLog.logMessage(
                f"Nie udało się utworzyć warstwy z: {source_uri}",
                "BDOO_GML_Loader",
                Qgis.Warning,
            )
            return None

        if gpkg_path is not None:
            layer.setCrs(QgsCoordinateReferenceSystem("EPSG:2180"))

        if layer.featureCount() <= 0:
            return None

        QgsProject.instance().addMapLayer(layer, False)
        target_group.addLayer(layer)
        layer.loadNamedStyle(str(style_path))

        layer_node = root.findLayer(layer.id())
        if layer_node is not None:
            layer_node.setExpanded(False)

        return layer

    @staticmethod
    def _region_code(namespace):
        """Zwróć dwucyfrowy kod województwa z przestrzeni nazw, jeżeli występuje."""
        match = re.search(r"(?:^|\.)(\d{2})$", namespace)
        return match.group(1) if match else ""

    def _group_name(self, namespace):
        """Zbuduj czytelną nazwę grupy warstw dla zbioru BDOO."""
        code = self._region_code(namespace)
        if code in WOJEWODZTWA:
            if code == "00":
                return "BDOO POLSKA"
            return f"BDOO WOJEWÓDZTWO {WOJEWODZTWA[code]}"
        return f"BDOO {namespace}"

    def _dataset_already_loaded(self, root, namespace, group_name):
        """Sprawdź, czy ten sam zbiór BDOO jest już obecny w projekcie."""
        for child in root.children():
            try:
                loaded_namespace = str(
                    child.customProperty(f"{_SETTINGS_GROUP}/namespace", "")
                )
            except (AttributeError, TypeError):
                loaded_namespace = ""

            try:
                child_name = child.name()
            except AttributeError:
                child_name = ""

            if loaded_namespace == namespace or child_name == group_name:
                return True

        return False

    def _confirm_duplicate(self, namespace, group_name):
        """Zapytaj, czy ponownie wczytać zbiór obecny już w projekcie."""
        dialog = QMessageBox(self.iface.mainWindow())
        dialog.setWindowTitle("Zbiór BDOO jest już wczytany")
        dialog.setIcon(QMessageBox.Warning)
        dialog.setText(
            f"Zbiór BDOO {namespace} jest już wczytany do bieżącego projektu "
            f"w grupie „{group_name}”.\n\nCzy chcesz wczytać go ponownie?"
        )
        load_again_button = dialog.addButton("Wczytaj ponownie", QMessageBox.AcceptRole)
        load_again_button.setToolTip(
            "Dodaj ten sam zbiór BDOO do projektu jako kolejną grupę."
        )
        cancel_button = dialog.addButton("Anuluj", QMessageBox.RejectRole)
        cancel_button.setToolTip(
            "Pozostaw już wczytane dane bez dodawania kolejnej kopii."
        )
        dialog.exec_()
        return dialog.clickedButton() is load_again_button

    def _load_dataset(
        self,
        path,
        przestrzen_nazw,
        formatPliku,
        source_type,
        source_path,
        source_records,
        available_source_uris=None,
        parent_group=None,
        skip_duplicate_check=False,
        gpkg_path_override=None,
    ):
        """Wczytaj wszystkie skonfigurowane warstwy BDOO do projektu QGIS."""
        self._available_source_uris = available_source_uris
        root = parent_group or QgsProject.instance().layerTreeRoot()
        group_name = self._group_name(przestrzen_nazw)

        if (
            not skip_duplicate_check
            and self._dataset_already_loaded(root, przestrzen_nazw, group_name)
        ):
            if not self._confirm_duplicate(przestrzen_nazw, group_name):
                return False

        qml_path = self.plugin_dir / "BDOO_QML"
        self._install_svg_symbols()

        text_count = (
            len([r for r in source_records if r["format"] in ("gml", "xml")])
            if formatPliku in ("gml", "xml")
            else 0
        )
        progress_message = self.iface.messageBar().createMessage(
            "Postęp importowania BDOO..."
        )
        progress = QProgressBar()
        progress.setMaximum(max(spec["progress"] for spec in LAYER_SPECS) + text_count)
        progress.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        progress_message.layout().addWidget(progress)
        self.iface.messageBar().pushWidget(progress_message, Qgis.Info)

        gpkg_path = gpkg_path_override
        if gpkg_path is None and formatPliku in ("gml", "xml"):
            gpkg_path = self._convert_text_to_gpkg(
                path,
                przestrzen_nazw,
                source_type,
                source_path,
                source_records,
                progress=progress,
            )
            if gpkg_path is None:
                self.iface.messageBar().clearWidgets()
                return False

        progress_offset = text_count if gpkg_path is not None else 0

        group = root.addGroup(group_name)
        group.setCustomProperty(f"{_SETTINGS_GROUP}/namespace", przestrzen_nazw)
        if gpkg_path is not None:
            group.setCustomProperty(f"{_SETTINGS_GROUP}/gpkg_path", str(gpkg_path))
        group.setExpanded(False)

        group_labels = group.addGroup(f"{przestrzen_nazw} napisy")
        group_labels.setExpanded(False)
        group_points = group.addGroup(f"{przestrzen_nazw} znaki punktowe")
        group_points.setExpanded(False)

        target_groups = {
            "labels": group_labels,
            "points": group_points,
            "main": group,
        }

        loaded_count = 0
        current_progress = 0
        try:
            for spec in LAYER_SPECS:
                layer = self._add_configured_layer(
                    spec,
                    path,
                    przestrzen_nazw,
                    formatPliku,
                    target_groups[spec["target"]],
                    root,
                    qml_path,
                    gpkg_path=gpkg_path,
                )
                if layer is not None:
                    loaded_count += 1

                if spec["progress"] != current_progress:
                    current_progress = spec["progress"]
                    self._set_progress(progress, progress_offset + current_progress)
        finally:
            self.iface.messageBar().clearWidgets()

        if loaded_count == 0:
            root.removeChildNode(group)
            QMessageBox.warning(
                self.iface.mainWindow(),
                "BDOO",
                "Nie wczytano żadnej warstwy BDOO. Sprawdź zawartość wskazanego źródła.",
            )
            return False

        if gpkg_path is not None:
            message = (
                f"Dane wczytano ze wspólnego GeoPackage: {gpkg_path}"
                if gpkg_path_override is not None
                else f"Dane GML/XML zapisano do GeoPackage i wczytano z pliku: {gpkg_path}"
            )
            self.iface.messageBar().pushSuccess("BDOO", message)

        return True
