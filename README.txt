BDOO_GML_Loader
================

Wtyczka służy do wczytywania danych BDOO do QGIS i nadawania im symbolizacji
zbliżonej do mapy ogólnogeograficznej w skali 1:250 000.

Źródłem danych może być:
- katalog z plikami BDOO,
- plik ZIP z danymi BDOO (bez konieczności ręcznego rozpakowywania),
- wojewódzka paczka BDOO pobrana bezpośrednio z Geoportalu GUGiK.

Obsługiwane są pliki GML/XML oraz SHP zgodne z konwencją nazewniczą BDOO,
np. PL.PZGiK.201.14__OT_ADMS_P.gml.

Dane z archiwum ZIP są odczytywane bezpośrednio przez mechanizm /vsizip/ GDAL/QGIS.
Style QML są ładowane bezpośrednio z katalogu wtyczki i nie są kopiowane do
katalogu z danymi.

Pobieranie z Geoportalu
-----------------------
Po wybraniu opcji „Geoportal” użytkownik wskazuje województwo i katalog zapisu.
Rok danych jest pobierany automatycznie z bieżącej daty systemowej. Adres paczki
jest budowany według schematu:
https://opendata.geoportal.gov.pl/bdoo/ROK/PL.PZGiK.201.KOD_WOJ.zip

Przykład dla województwa łódzkiego (TERYT 10):
https://opendata.geoportal.gov.pl/bdoo/ROK/PL.PZGiK.201.10.zip

W miejscu ROK wtyczka automatycznie wstawia bieżący rok, np. po rozpoczęciu
kolejnego roku nie jest wymagana zmiana kodu wtyczki.

Pobrany ZIP jest sprawdzany, zapisywany we wskazanym katalogu i następnie
automatycznie wczytywany przez wtyczkę.

Pomoc
-----
W oknie wyboru źródła danych przycisk „Pomoc” udostępnia:
- „Rozporządzenie BDOO (PDF)” – pobranie oficjalnego tekstu rozporządzenia
  (Dz.U. 2021 poz. 1412) z systemu ELI i otwarcie go w domyślnej aplikacji PDF,
- „Informacje” – nazwę i wersję wtyczki, repozytorium, zgłaszanie błędów,
  dokumentację, licencję oraz informację o właścicielu.
