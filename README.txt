BDOO_GML_Loader
================

Wtyczka służy do wczytywania danych BDOO do QGIS i nadawania im symbolizacji
zbliżonej do mapy ogólnogeograficznej w skali 1:250 000.

Źródłem danych może być:
- katalog z plikami BDOO,
- plik ZIP z danymi BDOO (bez konieczności ręcznego rozpakowywania),
- wojewódzka paczka BDOO pobrana bezpośrednio z Geoportalu GUGiK,
- komplet danych dla Polski pobierany jako 16 oddzielnych paczek wojewódzkich.

Obsługiwane są pliki GML/XML oraz SHP zgodne z konwencją nazewniczą BDOO,
np. PL.PZGiK.201.14__OT_ADMS_P.gml.

Dane z archiwum ZIP są odczytywane bezpośrednio przez mechanizm /vsizip/ GDAL/QGIS.
Style QML są ładowane bezpośrednio z katalogu wtyczki i nie są kopiowane do
katalogu z danymi.

Pobieranie z Geoportalu
-----------------------
Po wybraniu opcji „Geoportal” użytkownik wskazuje województwo i katalog zapisu.
Lista województw jest uporządkowana rosnąco według kodu TERYT: 02, 04, 06, 08,
10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32.
Rok danych jest pobierany automatycznie z bieżącej daty systemowej. Adres paczki
jest budowany według schematu:
https://opendata.geoportal.gov.pl/bdoo/ROK/PL.PZGiK.201.KOD_WOJ.zip

Przykład dla województwa łódzkiego (TERYT 10):
https://opendata.geoportal.gov.pl/bdoo/ROK/PL.PZGiK.201.10.zip

W miejscu ROK wtyczka automatycznie wstawia bieżący rok, np. po rozpoczęciu
kolejnego roku nie jest wymagana zmiana kodu wtyczki.

Pobrany ZIP jest sprawdzany, zapisywany we wskazanym katalogu i następnie
automatycznie wczytywany przez wtyczkę. Dane GML/XML są przy imporcie zapisywane
do pliku GeoPackage, a warstwy QGIS są wczytywane z utworzonego GPKG.

Dla całego kraju dostępne jest kompaktowe pole wyboru „Cały kraj” umieszczone
obok listy województw. Po jego zaznaczeniu lista województw jest wyłączana.
W tym trybie wtyczka nie pobiera paczki z kodem 00. Pobiera kolejno 16 paczek
wojewódzkich i scala ich zawartość do jednego pliku BDOO_POLSKA.gpkg. Każda
klasa obiektów ma jedną tabelę w GeoPackage, do której dopisywane są obiekty
z kolejnych województw. QGIS wczytuje następnie po jednej warstwie krajowej
na klasę obiektów w grupie „BDOO POLSKA”.

Pomoc
-----
W oknie wyboru źródła danych przycisk „Pomoc” udostępnia:
- „Rozporządzenie BDOO (PDF)” – pobranie oficjalnego tekstu rozporządzenia
  (Dz.U. 2021 poz. 1412) z systemu ELI i otwarcie go w domyślnej aplikacji PDF,
- „Informacje” – nazwę i wersję wtyczki, repozytorium, zgłaszanie błędów,
  dokumentację, licencję oraz informację o właścicielu.
