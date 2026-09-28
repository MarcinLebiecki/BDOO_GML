# -*- coding: utf-8 -*-
"""Pobieranie wojewódzkich paczek BDOO z Geoportalu GUGiK."""

from datetime import date
from pathlib import Path

from qgis.PyQt.QtCore import QEventLoop, QSettings, QSortFilterProxyModel, Qt, QUrl
from qgis.PyQt.QtWidgets import (
    QCheckBox,
    QComboBox,
    QCompleter,
    QDialog,
    QDialogButtonBox,
    QFileDialog,
    QFormLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMessageBox,
    QProgressDialog,
    QPushButton,
    QVBoxLayout,
    QWidget,
)
from qgis.core import QgsFileDownloader

from .constants import WOJEWODZTWA


# Rok danych jest wyznaczany na podstawie bieżącej daty systemowej.
# Dzięki temu po zmianie roku adres Geoportalu i komunikaty w interfejsie
# automatycznie używają nowego roku, bez modyfikowania kodu wtyczki.
def current_data_year():
    """Zwróć bieżący rok kalendarzowy używany w adresach danych BDOO."""
    return date.today().year


def geoportal_base_url():
    """Zwróć bazowy adres danych BDOO dla bieżącego roku."""
    return f"https://opendata.geoportal.gov.pl/bdoo/{current_data_year()}"
_SETTINGS_GROUP = "BDOO_GML_Loader"


class GeoportalDownloadDialog(QDialog):
    """Okno wyboru województwa i katalogu zapisu danych BDOO."""

    _POLISH_TRANSLATION = str.maketrans(
        "ąćęłńóśźżĄĆĘŁŃÓŚŹŻ",
        "acelnoszzACELNOSZZ",
    )

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Pobierz BDOO z Geoportalu")
        self.resize(650, 205)
        self._download_all_country = False

        settings = QSettings()
        default_dir = str(settings.value(f"{_SETTINGS_GROUP}/lastDownloadDir", ""))
        last_teryt = str(settings.value(f"{_SETTINGS_GROUP}/lastGeoportalTeryt", ""))

        self.wojewodztwo_combo = QComboBox(self)
        self.wojewodztwo_combo.setEditable(True)
        self.wojewodztwo_combo.setInsertPolicy(QComboBox.NoInsert)
        self.wojewodztwo_combo.setMinimumWidth(430)
        self.wojewodztwo_combo.lineEdit().setPlaceholderText(
            "Wpisz nazwę województwa / kod TERYT"
        )
        self.wojewodztwo_combo.lineEdit().setClearButtonEnabled(True)
        woj_tooltip = (
            "Wybierz województwo z listy lub wpisz fragment jego nazwy, np. „łódz” "
            "albo „lodz”. Możesz również wpisać dwucyfrowy kod TERYT województwa, "
            "np. „10”. Wyszukiwanie nie rozróżnia wielkości liter ani polskich znaków."
        )
        self.wojewodztwo_combo.setToolTip(woj_tooltip)
        self.wojewodztwo_combo.lineEdit().setToolTip(woj_tooltip)

        self.destination_edit = QLineEdit(default_dir, self)
        self.destination_edit.setToolTip(
            "Katalog, w którym zostanie zapisany pobrany plik ZIP z danymi BDOO."
        )
        browse_button = QPushButton("Wybierz katalog…", self)
        browse_button.setToolTip(
            "Wskaż katalog, do którego ma zostać zapisany pobrany plik ZIP z Geoportalu."
        )
        browse_button.clicked.connect(self._select_destination)

        destination_widget = QWidget(self)
        destination_layout = QHBoxLayout(destination_widget)
        destination_layout.setContentsMargins(0, 0, 0, 0)
        destination_layout.addWidget(self.destination_edit, 1)
        destination_layout.addWidget(browse_button)

        self.country_checkbox = QCheckBox("Cały kraj", self)
        self.country_checkbox.setToolTip(
            "Pobierz kolejno dane BDOO dla wszystkich 16 województw. Dane zostaną "
            "scalone klasami do jednego pliku BDOO_POLSKA.gpkg i wczytane do "
            "QGIS jako pełny zestaw dla Polski. Paczka z kodem 00 nie jest używana."
        )

        area_widget = QWidget(self)
        area_layout = QHBoxLayout(area_widget)
        area_layout.setContentsMargins(0, 0, 0, 0)
        area_layout.setSpacing(10)
        area_layout.addWidget(self.wojewodztwo_combo, 1)
        area_layout.addWidget(self.country_checkbox, 0)

        form = QFormLayout()
        form.addRow("Zakres danych:", area_widget)
        form.addRow("Katalog zapisu:", destination_widget)

        info = QLabel(
            f"Wybierz województwo lub zaznacz „Cały kraj”. Dane BDOO z "
            f"{current_data_year()} r. zostaną pobrane z Geoportalu, zapisane we "
            "wskazanym katalogu i automatycznie wczytane do QGIS. Dla całego kraju "
            "wtyczka pobiera kolejno 16 paczek wojewódzkich i scala je klasami do "
            "jednego pliku BDOO_POLSKA.gpkg.",
            self,
        )
        info.setWordWrap(True)

        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)
        self.download_button = buttons.button(QDialogButtonBox.Ok)
        self.download_button.setText("Pobierz i wczytaj dane")
        self.download_button.setToolTip(
            "Pobierz dane BDOO dla wybranego województwa albo, po zaznaczeniu "
            "opcji „Cały kraj”, kolejno dla wszystkich 16 województw i zapisz je "
            "do jednego GeoPackage."
        )
        cancel_button = buttons.button(QDialogButtonBox.Cancel)
        cancel_button.setText("Anuluj")
        cancel_button.setToolTip("Zamknij okno bez pobierania danych.")
        buttons.accepted.connect(self._accept_if_valid)
        buttons.rejected.connect(self.reject)

        layout = QVBoxLayout(self)
        layout.addWidget(info)
        layout.addLayout(form)
        layout.addWidget(buttons)

        self._populate_wojewodztwa()
        self._setup_completer()

        self.wojewodztwo_combo.currentIndexChanged.connect(
            self._update_download_button_state
        )
        self.wojewodztwo_combo.lineEdit().textChanged.connect(
            self._update_download_button_state
        )
        self.destination_edit.textChanged.connect(self._update_download_button_state)
        self.country_checkbox.stateChanged.connect(self._country_mode_changed)

        if last_teryt == "00":
            self.country_checkbox.setChecked(True)
            self.wojewodztwo_combo.setCurrentIndex(-1)
            self.wojewodztwo_combo.lineEdit().clear()
        elif last_teryt:
            index = self.wojewodztwo_combo.findData(last_teryt)
            if index >= 0:
                self.wojewodztwo_combo.setCurrentIndex(index)
            else:
                self.wojewodztwo_combo.setCurrentIndex(-1)
                self.wojewodztwo_combo.lineEdit().clear()
        else:
            self.wojewodztwo_combo.setCurrentIndex(-1)
            self.wojewodztwo_combo.lineEdit().clear()

        self._country_mode_changed()

    @classmethod
    def _normalize(cls, text):
        return str(text).translate(cls._POLISH_TRANSLATION).casefold().strip()

    def _matching_wojewodztwa(self, text):
        phrase = self._normalize(text)
        entries = [
            (teryt, name)
            for teryt, name in sorted(
                WOJEWODZTWA.items(), key=lambda item: item[0]
            )
            if teryt != "00"
        ]
        return [
            (teryt, name)
            for teryt, name in entries
            if not phrase or phrase in self._normalize(name) or phrase in teryt
        ]

    def _populate_wojewodztwa(self):
        for teryt, name in self._matching_wojewodztwa(""):
            self.wojewodztwo_combo.addItem(f"{name} — {teryt}", teryt)
            index = self.wojewodztwo_combo.count() - 1
            self.wojewodztwo_combo.setItemData(
                index,
                self._normalize(f"{name} {teryt}"),
                Qt.UserRole + 1,
            )

    def _setup_completer(self):
        self._woj_proxy = QSortFilterProxyModel(self)
        self._woj_proxy.setSourceModel(self.wojewodztwo_combo.model())
        self._woj_proxy.setFilterRole(Qt.UserRole + 1)
        self._woj_proxy.setFilterKeyColumn(0)
        self._woj_proxy.setFilterCaseSensitivity(Qt.CaseInsensitive)

        self._woj_completer = QCompleter(self._woj_proxy, self)
        self._woj_completer.setCompletionMode(QCompleter.UnfilteredPopupCompletion)
        self._woj_completer.setCaseSensitivity(Qt.CaseInsensitive)
        self._woj_completer.setMaxVisibleItems(16)
        self.wojewodztwo_combo.setCompleter(self._woj_completer)

        self.wojewodztwo_combo.lineEdit().textEdited.connect(self._update_completer)
        self._woj_completer.activated[str].connect(self._select_completion)

    def _update_completer(self, text):
        phrase = text.split(" — ", 1)[0] if " — " in text else text
        normalized = self._normalize(phrase)
        self._woj_proxy.setFilterFixedString(normalized)

        if normalized and self._woj_proxy.rowCount() > 0:
            self._woj_completer.complete()
        else:
            self._woj_completer.popup().hide()

    def _select_completion(self, text):
        index = self.wojewodztwo_combo.findText(text, Qt.MatchExactly)
        if index < 0:
            return
        self.wojewodztwo_combo.setCurrentIndex(index)
        self.wojewodztwo_combo.lineEdit().setCursorPosition(
            len(self.wojewodztwo_combo.currentText())
        )

    def _country_mode_changed(self, *args):
        """Włącz lub wyłącz tryb pobierania danych dla całego kraju."""
        country_mode = self.country_checkbox.isChecked()
        self.wojewodztwo_combo.setEnabled(not country_mode)
        self._download_all_country = country_mode
        self._update_download_button_state()

    def _update_download_button_state(self, *args):
        has_area = self.country_checkbox.isChecked() or bool(self.selected_teryt())
        destination_text = self.destination_edit.text().strip()
        has_directory = bool(destination_text) and self.destination_directory().is_dir()
        self.download_button.setEnabled(has_area and has_directory)

    @staticmethod
    def build_url(teryt):
        """Zbuduj adres paczki BDOO dla kodu województwa lub całego kraju (00)."""
        return f"{geoportal_base_url()}/PL.PZGiK.201.{teryt}.zip"

    @staticmethod
    def target_filename(teryt):
        return f"PL.PZGiK.201.{teryt}.zip"

    def selected_teryt(self):
        if self.country_checkbox.isChecked():
            return ""

        text = self.wojewodztwo_combo.currentText().strip()
        index = self.wojewodztwo_combo.currentIndex()

        if index >= 0 and text == self.wojewodztwo_combo.itemText(index):
            data = self.wojewodztwo_combo.itemData(index)
            return str(data) if data else ""

        matches = self._matching_wojewodztwa(text)
        if len(matches) == 1:
            return matches[0][0]
        return ""

    def destination_directory(self):
        return Path(self.destination_edit.text().strip()).expanduser()

    def _select_destination(self):
        start_dir = self.destination_edit.text().strip()
        directory = QFileDialog.getExistingDirectory(
            self,
            "Wybierz katalog zapisu danych BDOO",
            start_dir,
        )
        if directory:
            self.destination_edit.setText(directory)


    def download_all_country(self):
        """Zwróć True, gdy zaznaczono pobieranie wszystkich 16 województw."""
        return self.country_checkbox.isChecked()

    def _accept_if_valid(self):
        country_mode = self.country_checkbox.isChecked()
        teryt = self.selected_teryt()
        if not country_mode and not teryt:
            matches = self._matching_wojewodztwa(
                self.wojewodztwo_combo.currentText()
            )
            if not matches:
                message = (
                    "Nie znaleziono pozycji pasującej do wpisanej nazwy "
                    "lub kodu TERYT."
                )
            else:
                message = "Wybierz właściwe województwo z listy podpowiedzi."
            QMessageBox.warning(self, "BDOO", message)
            return

        directory = self.destination_directory()
        if not directory.is_dir():
            QMessageBox.warning(
                self,
                "BDOO",
                "Wskazany katalog zapisu nie istnieje.",
            )
            return

        settings = QSettings()
        settings.setValue(
            f"{_SETTINGS_GROUP}/lastGeoportalTeryt",
            "00" if country_mode else teryt,
        )
        settings.setValue(f"{_SETTINGS_GROUP}/lastDownloadDir", str(directory))
        self._download_all_country = country_mode
        self.accept()


def _ask_existing_file(parent, target_path):
    dialog = QMessageBox(parent)
    dialog.setWindowTitle("Plik BDOO już istnieje")
    dialog.setIcon(QMessageBox.Question)
    dialog.setText(
        "W wybranym katalogu znajduje się już wskazana paczka danych BDOO.\n\n"
        f"{target_path.name}"
    )
    replace_button = dialog.addButton(
        "Pobierz ponownie i zastąp plik", QMessageBox.AcceptRole
    )
    replace_button.setToolTip(
        "Pobierz aktualną paczkę z Geoportalu i zastąp istniejący plik ZIP."
    )
    use_button = dialog.addButton("Użyj istniejącego pliku", QMessageBox.ActionRole)
    use_button.setToolTip(
        "Nie pobieraj danych ponownie. Użyj istniejącego pliku ZIP i wczytaj go do QGIS."
    )
    cancel_button = dialog.addButton("Anuluj", QMessageBox.RejectRole)
    cancel_button.setToolTip(
        "Przerwij operację bez pobierania i bez wczytywania danych."
    )
    dialog.exec_()

    clicked = dialog.clickedButton()
    if clicked is replace_button:
        return "replace"
    if clicked is use_button:
        return "use"
    return "cancel"


def download_geoportal_zip(
    parent, teryt, destination_directory, batch_index=None, batch_total=None
):
    """Pobierz paczkę BDOO z Geoportalu i zwróć ścieżkę do pliku ZIP."""
    import zipfile

    destination_directory = Path(destination_directory).expanduser()
    target_path = destination_directory / GeoportalDownloadDialog.target_filename(teryt)

    if not destination_directory.is_dir():
        QMessageBox.critical(
            parent,
            "BDOO",
            "Wskazany katalog zapisu nie istnieje.",
        )
        return None

    if target_path.exists():
        existing_action = _ask_existing_file(parent, target_path)
        if existing_action == "use":
            if zipfile.is_zipfile(target_path):
                return target_path
            QMessageBox.critical(
                parent,
                "BDOO",
                "Istniejący plik nie jest poprawnym archiwum ZIP. "
                "Wybierz ponowne pobranie danych.",
            )
            return None
        if existing_action == "cancel":
            return None

    temporary_path = target_path.with_suffix(target_path.suffix + ".part")
    try:
        if temporary_path.exists():
            temporary_path.unlink()
    except OSError as exc:
        QMessageBox.critical(
            parent,
            "BDOO",
            f"Nie można przygotować pliku tymczasowego do pobierania:\n{exc}",
        )
        return None

    url = GeoportalDownloadDialog.build_url(teryt)
    if teryt == "00":
        area_label = "całego kraju"
    else:
        woj_name = WOJEWODZTWA.get(teryt, teryt)
        area_label = f"województwa {woj_name} ({teryt})"

    batch_label = ""
    if batch_index is not None and batch_total:
        batch_label = f"\nPakiet {batch_index} z {batch_total}"

    progress_label = f"Pobieranie danych BDOO dla {area_label}…{batch_label}"
    progress = QProgressDialog(
        progress_label,
        "Anuluj pobieranie",
        0,
        100,
        parent,
    )
    progress.setWindowTitle("Pobieranie danych BDOO")
    progress.setWindowModality(Qt.WindowModal)
    progress.setMinimumDuration(0)
    progress.setAutoClose(False)
    progress.setAutoReset(False)
    progress.setToolTip(
        "Dane są pobierane z Geoportalu i zapisywane bezpośrednio we wskazanym katalogu."
    )
    progress.show()

    cancel_button = progress.findChild(QPushButton)
    if cancel_button is not None:
        cancel_button.setToolTip(
            "Przerwij pobieranie danych i usuń niekompletny plik."
        )

    state = {"completed": False, "canceled": False, "errors": []}
    downloader = QgsFileDownloader(
        QUrl(url),
        str(temporary_path),
        "",
        True,
    )

    def update_progress(received, total):
        if total > 0:
            progress.setRange(0, 100)
            progress.setValue(min(100, int(received * 100 / total)))
            progress.setLabelText(
                progress_label
                + "\n"
                + f"{received / (1024 * 1024):.1f} MB z "
                + f"{total / (1024 * 1024):.1f} MB"
            )
        else:
            progress.setRange(0, 0)
            progress.setLabelText(
                progress_label
                + "\n"
                + f"Pobrano {received / (1024 * 1024):.1f} MB"
            )

    def mark_completed(_url):
        state["completed"] = True

    def mark_canceled():
        state["canceled"] = True

    def mark_error(messages):
        state["errors"].extend(str(message) for message in messages)

    loop = QEventLoop()
    downloader.downloadProgress.connect(update_progress)
    downloader.downloadCompleted.connect(mark_completed)
    downloader.downloadCanceled.connect(mark_canceled)
    downloader.downloadError.connect(mark_error)
    downloader.downloadExited.connect(loop.quit)
    progress.canceled.connect(downloader.cancelDownload)

    downloader.startDownload()
    loop.exec_()

    try:
        progress.canceled.disconnect(downloader.cancelDownload)
    except (TypeError, RuntimeError):
        pass
    progress.close()

    if state["canceled"]:
        _safe_unlink(temporary_path)
        return None

    if state["errors"] or not state["completed"]:
        _safe_unlink(temporary_path)
        details = (
            "\n".join(state["errors"])
            if state["errors"]
            else "Pobieranie nie zostało zakończone poprawnie."
        )
        QMessageBox.critical(
            parent,
            "BDOO",
            "Nie udało się pobrać danych z Geoportalu.\n\n" + details,
        )
        return None

    if not temporary_path.is_file() or temporary_path.stat().st_size == 0:
        _safe_unlink(temporary_path)
        QMessageBox.critical(
            parent,
            "BDOO",
            "Pobieranie zakończyło się bez zapisania danych do pliku.",
        )
        return None

    if not zipfile.is_zipfile(temporary_path):
        _safe_unlink(temporary_path)
        QMessageBox.critical(
            parent,
            "BDOO",
            "Geoportal nie zwrócił poprawnego archiwum ZIP dla wybranego województwa.",
        )
        return None

    try:
        temporary_path.replace(target_path)
    except OSError as exc:
        _safe_unlink(temporary_path)
        QMessageBox.critical(
            parent,
            "BDOO",
            f"Pobrano dane, ale nie można zapisać pliku docelowego:\n{exc}",
        )
        return None

    return target_path


def _safe_unlink(path):
    try:
        Path(path).unlink()
    except OSError:
        pass
