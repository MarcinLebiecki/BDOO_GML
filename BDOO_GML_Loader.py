# -*- coding: utf-8 -*-
"""
/***************************************************************************
 BDOO_GML_Loader
                                 A QGIS plugin
 Importuje BDOO w formacie GML
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2020-07-20
        git sha              : $Format:%H$
        copyright            : (C) 2024 by Marcin Lebiecki / Główny Urząd Geodezji i Kartografii
        email                : marcin.lebiecki@gugik.gov.pl
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from qgis.PyQt.QtCore import *
from qgis.core import *
from qgis.utils import *
from qgis.gui import *
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QAction,QFileDialog,QProgressBar,QMessageBox

# Initialize Qt resources from file resources.py
from . import resources
from shutil import copyfile
import os.path
import re
import time
import shutil
from pathlib import Path


class BDOO_GML_Loader:
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'BDOO_GML_Loader_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)
            QCoreApplication.installTranslator(self.translator)

        # Declare instance attributes
        self.actions = []
        self.menu = self.tr(u'&BDOO_GML')

        # Check if plugin was started the first time in current QGIS session
        # Must be set in initGui() to survive plugin reloads
        self.first_start = None

    # noinspection PyMethodMayBeStatic
    def tr(self, message):
        """Get the translation for a string using Qt translation API.

        We implement this ourselves since we do not inherit QObject.

        :param message: String for translation.
        :type message: str, QString

        :returns: Translated version of message.
        :rtype: QString
        """
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate('BDOO_GML_Loader', message)


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
        parent=None):
        """Add a toolbar icon to the toolbar.

        :param icon_path: Path to the icon for this action. Can be a resource
            path (e.g. ':/plugins/foo/bar.png') or a normal file system path.
        :type icon_path: str

        :param text: Text that should be shown in menu items for this action.
        :type text: str

        :param callback: Function to be called when the action is triggered.
        :type callback: function

        :param enabled_flag: A flag indicating if the action should be enabled
            by default. Defaults to True.
        :type enabled_flag: bool

        :param add_to_menu: Flag indicating whether the action should also
            be added to the menu. Defaults to True.
        :type add_to_menu: bool

        :param add_to_toolbar: Flag indicating whether the action should also
            be added to the toolbar. Defaults to True.
        :type add_to_toolbar: bool

        :param status_tip: Optional text to show in a popup when mouse pointer
            hovers over the action.
        :type status_tip: str

        :param parent: Parent widget for the new action. Defaults None.
        :type parent: QWidget

        :param whats_this: Optional text to show in the status bar when the
            mouse pointer hovers over the action.

        :returns: The action that was created. Note that the action is also
            added to self.actions list.
        :rtype: QAction
        """

        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            # Adds plugin icon to Plugins toolbar
            self.iface.addToolBarIcon(action)

        if add_to_menu:
            self.iface.addPluginToMenu(
                self.menu,
                action)

        self.actions.append(action)

        return action

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""

        icon_path = ':/plugins/BDOO_GML_Loader/icon.png'
        self.add_action(
            icon_path,
            text=self.tr(u'Import BDOO GML'),
            callback=self.run,
            parent=self.iface.mainWindow())

        # will be set False in run()
        self.first_start = True


    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginMenu(
                self.tr(u'&BDOO_GML'),
                action)
            self.iface.removeToolBarIcon(action)


    def run(self):
        """Run method that performs all the real work"""

        if self.first_start == True:
            self.first_start = False
        
        wojewodztwo ={
        "02" : "DOLNOŚLĄSKIE",
        "04" : "KUJAWSKO-POMORSKIE",
        "06" : "LUBELSKIE",
        "08" : "LUBUSKIE",
        "10" : "ŁÓDZKIE",
        "12" : "MAŁOPOLSKIE",
        "14" : "MAZOWIECKIE",
        "16" : "OPOLSKIE",
        "18" : "PODKARPACKIE",
        "20" : "PODLASKIE",
        "22" : "POMORSKIE",
        "24" : "ŚLĄSKIE",
        "26" : "ŚWIĘTOKRZYSKIE",
        "28" : "WARMIŃSKO-MAZURSKIE",
        "30" : "WIELKOPOLSKIE",
        "32" : "ZACHODNIOPOMORSKIE"}
        
        folder_path = QFileDialog.getExistingDirectory(self.iface.mainWindow(),'Wybierz folder BDOO')
        path = folder_path.replace("\\", "/")+"/"
        result = False
        files = None
        
        if folder_path == "":
            return
        
        for file in os.listdir(folder_path):
            if (file.endswith(".gml") or file.endswith(".shp")) and re.match("PL\.PZG[i|I]K\.201\.\d{2}(__OT_)", file):
                    result = True
                    przestrzen_nazw = str(re.split("__", file)[0])
                    if file.endswith(".gml"):
                        formatPliku = "gml"
        
        if result:
            qmlPath = Path(QgsApplication.qgisSettingsDirPath())/Path("python/plugins/BDOO_GML_Loader/BDOO_QML/")
            svgPluginPath = Path(QgsApplication.qgisSettingsDirPath())/Path("python/plugins/BDOO_GML_Loader/BDOO_SVG/KARTO250k/")
            svgQGISpath = Path(QgsApplication.qgisSettingsDirPath())/Path("SVG/")
            
            #kopiuje pliki SVG na konto uzytkownika
            try:
                shutil.copytree(svgPluginPath, svgQGISpath/Path("KARTO250k"))
            except:
                pass
            
            progressMessageBar = iface.messageBar().createMessage("Postęp importowania BDOO...")
            progress = QProgressBar()
            progress.setMaximum(33)
            progress.setAlignment(Qt.AlignLeft|Qt.AlignVCenter)
            progressMessageBar.layout().addWidget(progress)
            iface.messageBar().pushWidget(progressMessageBar, Qgis.Info)
            
            teryt = przestrzen_nazw[-2:]
            nazwa_wojewodztwa = wojewodztwo[teryt]
            groupName = 'BDOO WOJEWÓDZTWO '+nazwa_wojewodztwa
            root = QgsProject.instance().layerTreeRoot()
            group = root.addGroup(groupName)
            group.setExpanded(False)
            groupNapisy = group.addGroup(przestrzen_nazw+' napisy')
            groupNapisy.setExpanded(False)
            groupPunktowe = group.addGroup(przestrzen_nazw+' znaki punktowe')
            groupPunktowe.setExpanded(False)
            
            if os.path.exists(path+przestrzen_nazw+'__OT_ADMS_P.'+formatPliku):
                copyfile(qmlPath/Path("OT_ADMS_P__nazwy_miejscowosci.qml"), path+przestrzen_nazw+'__nazwy_miejscowosci.qml')
                nazwy_miejscowosci = QgsVectorLayer(path+przestrzen_nazw+"__OT_ADMS_P."+formatPliku, przestrzen_nazw+"__nazwy miejscowości","ogr")
                if nazwy_miejscowosci.featureCount()>0:
                    QgsProject.instance().addMapLayer(nazwy_miejscowosci, False)
                    groupNapisy.addLayer(nazwy_miejscowosci)
                    nazwy_miejscowosci.loadNamedStyle(path+przestrzen_nazw+'__nazwy_miejscowosci.qml')
                    myLayerNode = root.findLayer(nazwy_miejscowosci.id())
                    myLayerNode.setExpanded(False)
                else:
                    nazwy_miejscowosci = None
            progress.setValue(1)
            if os.path.exists(path+przestrzen_nazw+'__OT_SKDR_L.'+formatPliku):
                copyfile(qmlPath/Path("OT_SKDR_L__szlaki_drogowe.qml"), path+przestrzen_nazw+'__szlaki_drogowe.qml')
                szlaki_drogowe = QgsVectorLayer(path+przestrzen_nazw+"__OT_SKDR_L."+formatPliku, przestrzen_nazw+"__szlaki drogowe","ogr")
                if szlaki_drogowe.featureCount()>0:
                    QgsProject.instance().addMapLayer(szlaki_drogowe, False)
                    groupNapisy.addLayer(szlaki_drogowe)
                    szlaki_drogowe.loadNamedStyle(path+przestrzen_nazw+'__szlaki_drogowe.qml')
                    myLayerNode = root.findLayer(szlaki_drogowe.id())
                    myLayerNode.setExpanded(False)
                else:
                    szlaki_drogowe = None
            progress.setValue(2)
            if os.path.exists(path+przestrzen_nazw+'__OT_SWRS_L.'+formatPliku):
                copyfile(qmlPath/Path("OT_SWRS_L__nazwy_rzek.qml"), path+przestrzen_nazw+'__nazwy_rzek.qml')
                nazwy_rzek = QgsVectorLayer(path+przestrzen_nazw+"__OT_SWRS_L."+formatPliku, przestrzen_nazw+"__nazwy rzek","ogr")
                if nazwy_rzek.featureCount()>0:
                    QgsProject.instance().addMapLayer(nazwy_rzek, False)
                    groupNapisy.addLayer(nazwy_rzek)
                    nazwy_rzek.loadNamedStyle(path+przestrzen_nazw+'__nazwy_rzek.qml')
                    myLayerNode = root.findLayer(nazwy_rzek.id())
                    myLayerNode.setExpanded(False)
                else:
                    nazwy_rzek = None
            progress.setValue(3)
            if os.path.exists(path+przestrzen_nazw+'__OT_PTWP_A.'+formatPliku):
                copyfile(qmlPath/Path("OT_PTWP_A__nazwy_wod_powierzchniowych.qml"), path+przestrzen_nazw+'__nazwy_wod_powierzchniowych.qml')
                nazwy_wod_powierzchniowych = QgsVectorLayer(path+przestrzen_nazw+"__OT_PTWP_A."+formatPliku, przestrzen_nazw+"__nazwy wód powierzchniowych","ogr")
                if nazwy_wod_powierzchniowych.featureCount()>0:
                    QgsProject.instance().addMapLayer(nazwy_wod_powierzchniowych, False)
                    groupNapisy.addLayer(nazwy_wod_powierzchniowych)
                    nazwy_wod_powierzchniowych.loadNamedStyle(path+przestrzen_nazw+'__nazwy_wod_powierzchniowych.qml')
                    myLayerNode = root.findLayer(nazwy_wod_powierzchniowych.id())
                    myLayerNode.setExpanded(False)
                else:
                    nazwy_wod_powierzchniowych = None
            progress.setValue(4)
            if os.path.exists(path+przestrzen_nazw+'__OT_TCPN_A.'+formatPliku):
                copyfile(qmlPath/Path("OT_TCPN_A__nazwy_parkow_narodowych.qml"), path+przestrzen_nazw+'__nazwy_parkow_narodowych.qml')
                nazwy_parkow_narodowych = QgsVectorLayer(path+przestrzen_nazw+"__OT_TCPN_A."+formatPliku, przestrzen_nazw+"__nazwy parków narodowych","ogr")
                if nazwy_parkow_narodowych.featureCount()>0:
                    QgsProject.instance().addMapLayer(nazwy_parkow_narodowych, False)
                    groupNapisy.addLayer(nazwy_parkow_narodowych)
                    nazwy_parkow_narodowych.loadNamedStyle(path+przestrzen_nazw+'__nazwy_parkow_narodowych.qml')
                    myLayerNode = root.findLayer(nazwy_parkow_narodowych.id())
                    myLayerNode.setExpanded(False)
                else:
                    nazwy_parkow_narodowych = None
            progress.setValue(5)
            if os.path.exists(path+przestrzen_nazw+'__OT_TCRZ_A.'+formatPliku):
                copyfile(qmlPath/Path("OT_TCRZ_A__nazwy_rezerwatow.qml"), path+przestrzen_nazw+'__nazwy_rezerwatow.qml')
                nazwy_rezerwatow = QgsVectorLayer(path+przestrzen_nazw+"__OT_TCRZ_A."+formatPliku, przestrzen_nazw+"__nazwy rezerwatów","ogr")
                if nazwy_rezerwatow.featureCount()>0:
                    QgsProject.instance().addMapLayer(nazwy_rezerwatow, False)
                    groupNapisy.addLayer(nazwy_rezerwatow)
                    nazwy_rezerwatow.loadNamedStyle(path+przestrzen_nazw+'__nazwy_rezerwatow.qml')
                    myLayerNode = root.findLayer(nazwy_rezerwatow.id())
                    myLayerNode.setExpanded(False)
                else:
                    nazwy_rezerwatow = None
            progress.setValue(6)
            if os.path.exists(path+przestrzen_nazw+'__OT_TCPK_A.'+formatPliku):
                copyfile(qmlPath/Path("OT_TCPK_A__nazwy_parkow_krajobrazowych.qml"), path+przestrzen_nazw+'__nazwy_parkow_krajobrazowych.qml')
                nazwy_parkow_krajobrazowych = QgsVectorLayer(path+przestrzen_nazw+"__OT_TCPK_A."+formatPliku, przestrzen_nazw+"__nazwy parków krajobrazowych","ogr")
                if nazwy_parkow_krajobrazowych.featureCount()>0:
                    QgsProject.instance().addMapLayer(nazwy_parkow_krajobrazowych, False)
                    groupNapisy.addLayer(nazwy_parkow_krajobrazowych)
                    nazwy_parkow_krajobrazowych.loadNamedStyle(path+przestrzen_nazw+'__nazwy_parkow_krajobrazowych.qml')
                    myLayerNode = root.findLayer(nazwy_parkow_krajobrazowych.id())
                    myLayerNode.setExpanded(False)
                else:
                    nazwy_parkow_krajobrazowych = None
            progress.setValue(7)
            if os.path.exists(path+przestrzen_nazw+'__OT_KUKO_A.'+formatPliku):
                copyfile(qmlPath/Path("OT_KUKO_A__nazwy_kompleksow.qml"), path+przestrzen_nazw+'__nazwy_kompleksow.qml')
                nazwy_kompleksow = QgsVectorLayer(path+przestrzen_nazw+"__OT_KUKO_A."+formatPliku, przestrzen_nazw+"__nazwy kompleksów","ogr")
                if nazwy_kompleksow.featureCount()>0:
                    QgsProject.instance().addMapLayer(nazwy_kompleksow, False)
                    groupNapisy.addLayer(nazwy_kompleksow)
                    nazwy_kompleksow.loadNamedStyle(path+przestrzen_nazw+'__nazwy_kompleksow.qml')
                    myLayerNode = root.findLayer(nazwy_kompleksow.id())
                    myLayerNode.setExpanded(False)
                else:
                    nazwy_kompleksow = None
            progress.setValue(8)
            if os.path.exists(path+przestrzen_nazw+'__OT_ADMS_P.'+formatPliku):
                copyfile(qmlPath/Path("OT_ADMS_P.qml"), path+przestrzen_nazw+'__OT_ADMS_P.qml')
                OT_ADMS_P = QgsVectorLayer(path+przestrzen_nazw+"__OT_ADMS_P."+formatPliku, przestrzen_nazw+"__OT_ADMS_P","ogr")
                if OT_ADMS_P.featureCount()>0:
                    QgsProject.instance().addMapLayer(OT_ADMS_P, False)
                    groupPunktowe.addLayer(OT_ADMS_P)
                    OT_ADMS_P.loadNamedStyle(path+przestrzen_nazw+'__OT_KUSK_A opis.qml')
                    myLayerNode = root.findLayer(OT_ADMS_P.id())
                    myLayerNode.setExpanded(False)
                else:
                    OT_ADMS_P = None
            progress.setValue(9)
            if os.path.exists(path+przestrzen_nazw+'__OT_TCRZ_A.'+formatPliku):
                copyfile(qmlPath/Path("OT_TCRZ_A_pkt.qml"), path+przestrzen_nazw+'__OT_TCRZ_A_pkt.qml')
                OT_TCRZ_A = QgsVectorLayer(path+przestrzen_nazw+"__OT_TCRZ_A."+formatPliku, przestrzen_nazw+"__OT_TCRZ_A","ogr")
                if OT_TCRZ_A.featureCount()>0:
                    QgsProject.instance().addMapLayer(OT_TCRZ_A, False)
                    groupPunktowe.addLayer(OT_TCRZ_A)
                    OT_TCRZ_A.loadNamedStyle(path+przestrzen_nazw+'__OT_TCRZ_A_pkt.qml')
                    myLayerNode = root.findLayer(OT_TCRZ_A.id())
                    myLayerNode.setExpanded(False)
                else:
                    OT_TCRZ_A = None
            progress.setValue(10)
            if os.path.exists(path+przestrzen_nazw+'__OT_KUPG_P.'+formatPliku):
                copyfile(qmlPath/Path("OT_KUPG_P.qml"), path+przestrzen_nazw+'__OT_KUPG_P.qml')
                OT_KUPG_P = QgsVectorLayer(path+przestrzen_nazw+"__OT_KUPG_P."+formatPliku, przestrzen_nazw+"__OT_KUPG_P","ogr")
                if OT_KUPG_P.featureCount()>0:
                    QgsProject.instance().addMapLayer(OT_KUPG_P, False)
                    groupPunktowe.addLayer(OT_KUPG_P)
                    OT_KUPG_P.loadNamedStyle(path+przestrzen_nazw+'__OT_KUPG_P.qml')
                    myLayerNode = root.findLayer(OT_KUPG_P.id())
                    myLayerNode.setExpanded(False)
                else:
                    OT_KUPG_P = None
            progress.setValue(11)
            if os.path.exists(path+przestrzen_nazw+'__OT_KUKO_P.'+formatPliku):
                copyfile(qmlPath/Path("OT_KUKO_P.qml"), path+przestrzen_nazw+'__OT_KUKO_P.qml')
                OT_KUKO_P = QgsVectorLayer(path+przestrzen_nazw+"__OT_KUKO_P."+formatPliku, przestrzen_nazw+"__OT_KUKO_P","ogr")
                if OT_KUKO_P.featureCount()>0:
                    QgsProject.instance().addMapLayer(OT_KUKO_P, False)
                    groupPunktowe.addLayer(OT_KUKO_P)
                    OT_KUKO_P.loadNamedStyle(path+przestrzen_nazw+'__OT_KUKO_P.qml')
                    myLayerNode = root.findLayer(OT_KUKO_P.id())
                    myLayerNode.setExpanded(False)
                else:
                    OT_KUKO_P = None
            progress.setValue(12)
            if os.path.exists(path+przestrzen_nazw+'__OT_OIKM_P.'+formatPliku):
                copyfile(qmlPath/Path("OT_OIKM_P.qml"), path+przestrzen_nazw+'__OT_OIKM_P.qml')
                OT_OIKM_P = QgsVectorLayer(path+przestrzen_nazw+"__OT_OIKM_P."+formatPliku, przestrzen_nazw+"__OT_OIKM_P","ogr")
                if OT_OIKM_P.featureCount()>0:
                    QgsProject.instance().addMapLayer(OT_OIKM_P, False)
                    groupPunktowe.addLayer(OT_OIKM_P)
                    OT_OIKM_P.loadNamedStyle(path+przestrzen_nazw+'__OT_OIKM_P.qml')
                    myLayerNode = root.findLayer(OT_OIKM_P.id())
                    myLayerNode.setExpanded(False)
                else:
                    OT_OIKM_P = None
            progress.setValue(13)
            if os.path.exists(path+przestrzen_nazw+'__OT_SULN_L.'+formatPliku):
                copyfile(qmlPath/Path("OT_SULN_L.qml"), path+przestrzen_nazw+'__OT_SULN_L.qml')
                OT_SULN_L = QgsVectorLayer(path+przestrzen_nazw+"__OT_SULN_L."+formatPliku, przestrzen_nazw+"__OT_SULN_L","ogr")
                if OT_SULN_L.featureCount()>0:
                    QgsProject.instance().addMapLayer(OT_SULN_L, False)
                    group.addLayer(OT_SULN_L)
                    OT_SULN_L.loadNamedStyle(path+przestrzen_nazw+'__OT_SULN_L.qml')
                    myLayerNode = root.findLayer(OT_SULN_L.id())
                    myLayerNode.setExpanded(False)
                else:
                    OT_SULN_L = None
            progress.setValue(14)
            if os.path.exists(path+przestrzen_nazw+'__OT_SKPP_L.'+formatPliku):
                copyfile(qmlPath/Path("OT_SKPP_L.qml"), path+przestrzen_nazw+'__OT_SKPP_L.qml')
                OT_SKPP_L = QgsVectorLayer(path+przestrzen_nazw+"__OT_SKPP_L."+formatPliku, przestrzen_nazw+"__OT_SKPP_L","ogr")
                if OT_SKPP_L.featureCount()>0:
                    QgsProject.instance().addMapLayer(OT_SKPP_L, False)
                    group.addLayer(OT_SKPP_L)
                    OT_SKPP_L.loadNamedStyle(path+przestrzen_nazw+'__OT_SKPP_L.qml')
                    myLayerNode = root.findLayer(OT_SKPP_L.id())
                    myLayerNode.setExpanded(False)
                else:
                    OT_SKPP_L = None
            progress.setValue(15)
            if os.path.exists(path+przestrzen_nazw+'__OT_SKTR_L.'+formatPliku):
                copyfile(qmlPath/Path("OT_SKTR_L.qml"), path+przestrzen_nazw+'__OT_SKTR_L.qml')
                OT_SKTR_L = QgsVectorLayer(path+przestrzen_nazw+"__OT_SKTR_L."+formatPliku, przestrzen_nazw+"__OT_SKTR_L","ogr")
                if OT_SKTR_L.featureCount()>0:
                    QgsProject.instance().addMapLayer(OT_SKTR_L, False)
                    group.addLayer(OT_SKTR_L)
                    OT_SKTR_L.loadNamedStyle(path+przestrzen_nazw+'__OT_SKTR_L.qml')
                    myLayerNode = root.findLayer(OT_SKTR_L.id())
                    myLayerNode.setExpanded(False)
                else:
                    OT_SKTR_L = None
            progress.setValue(16)
            if os.path.exists(path+przestrzen_nazw+'__OT_SKDR_L.'+formatPliku):
                copyfile(qmlPath/Path("OT_SKDR_L.qml"), path+przestrzen_nazw+'__OT_SKDR_L.qml')
                OT_SKDR_L = QgsVectorLayer(path+przestrzen_nazw+"__OT_SKDR_L."+formatPliku, przestrzen_nazw+"__OT_SKDR_L","ogr")
                if OT_SKDR_L.featureCount()>0:
                    QgsProject.instance().addMapLayer(OT_SKDR_L, False)
                    group.addLayer(OT_SKDR_L)
                    OT_SKDR_L.loadNamedStyle(path+przestrzen_nazw+'__OT_SKDR_L.qml')
                    myLayerNode = root.findLayer(OT_SKDR_L.id())
                    myLayerNode.setExpanded(False)
                else:
                    OT_SKDR_L = None
            progress.setValue(17)
            if os.path.exists(path+przestrzen_nazw+'__OT_ADJA_A.'+formatPliku):
                copyfile(qmlPath/Path("OT_ADJA_A.qml"), path+przestrzen_nazw+'__OT_ADJA_A.qml')
                OT_ADJA_A = QgsVectorLayer(path+przestrzen_nazw+"__OT_ADJA_A."+formatPliku, przestrzen_nazw+"__OT_ADJA_A","ogr")
                if OT_ADJA_A.featureCount()>0:
                    QgsProject.instance().addMapLayer(OT_ADJA_A, False)
                    group.addLayer(OT_ADJA_A)
                    OT_ADJA_A.loadNamedStyle(path+przestrzen_nazw+'__OT_ADJA_A.qml')
                    myLayerNode = root.findLayer(OT_ADJA_A.id())
                    myLayerNode.setExpanded(False)
                else:
                    OT_ADJA_A = None
            progress.setValue(18)
            if os.path.exists(path+przestrzen_nazw+'__OT_TCPN_A.'+formatPliku):
                copyfile(qmlPath/Path("OT_TCPN_A.qml"), path+przestrzen_nazw+'__OT_TCPN_A.qml')
                OT_TCPN_A = QgsVectorLayer(path+przestrzen_nazw+"__OT_TCPN_A."+formatPliku, przestrzen_nazw+"__OT_TCPN_A","ogr")
                if OT_TCPN_A.featureCount()>0:
                    QgsProject.instance().addMapLayer(OT_TCPN_A, False)
                    group.addLayer(OT_TCPN_A)
                    OT_TCPN_A.loadNamedStyle(path+przestrzen_nazw+'__OT_TCPN_A.qml')
                    myLayerNode = root.findLayer(OT_TCPN_A.id())
                    myLayerNode.setExpanded(False)
                else:
                    OT_TCPN_A = None
            progress.setValue(19)
            if os.path.exists(path+przestrzen_nazw+'__OT_TCPK_A.'+formatPliku):
                copyfile(qmlPath/Path("OT_TCPK_A.qml"), path+przestrzen_nazw+'__OT_TCPK_A.qml')
                OT_TCPK_A = QgsVectorLayer(path+przestrzen_nazw+"__OT_TCPK_A."+formatPliku, przestrzen_nazw+"__OT_TCPK_A","ogr")
                if OT_TCPK_A.featureCount()>0:
                    QgsProject.instance().addMapLayer(OT_TCPK_A, False)
                    group.addLayer(OT_TCPK_A)
                    OT_TCPK_A.loadNamedStyle(path+przestrzen_nazw+'__OT_TCPK_A.qml')
                    myLayerNode = root.findLayer(OT_TCPK_A.id())
                    myLayerNode.setExpanded(False)
                else:
                    OT_TCPK_A = None
            progress.setValue(20)
            if os.path.exists(path+przestrzen_nazw+'__OT_BUUO_L.'+formatPliku):
                copyfile(qmlPath/Path("OT_BUUO_L.qml"), path+przestrzen_nazw+'__OT_BUUO_L.qml')
                OT_BUUO_L = QgsVectorLayer(path+przestrzen_nazw+"__OT_BUUO_L."+formatPliku, przestrzen_nazw+"__OT_BUUO_L","ogr")
                if OT_BUUO_L.featureCount()>0:
                    QgsProject.instance().addMapLayer(OT_BUUO_L, False)
                    group.addLayer(OT_BUUO_L)
                    OT_BUUO_L.loadNamedStyle(path+przestrzen_nazw+'__OT_BUUO_L.qml')
                    myLayerNode = root.findLayer(OT_BUUO_L.id())
                    myLayerNode.setExpanded(False)
                else:
                    OT_BUUO_L = None
            progress.setValue(21)
            if os.path.exists(path+przestrzen_nazw+'__OT_PTWP_A.'+formatPliku):
                copyfile(qmlPath/Path("OT_PTWP_A.qml"), path+przestrzen_nazw+'__OT_PTWP_A.qml')
                OT_PTWP_A = QgsVectorLayer(path+przestrzen_nazw+"__OT_PTWP_A."+formatPliku, przestrzen_nazw+"__OT_PTWP_A","ogr")
                if OT_PTWP_A.featureCount()>0:
                    QgsProject.instance().addMapLayer(OT_PTWP_A, False)
                    group.addLayer(OT_PTWP_A)
                    OT_PTWP_A.loadNamedStyle(path+przestrzen_nazw+'__OT_PTWP_A.qml')
                    myLayerNode = root.findLayer(OT_PTWP_A.id())
                    myLayerNode.setExpanded(False)
                else:
                    OT_PTWP_A = None
            progress.setValue(22)
            if os.path.exists(path+przestrzen_nazw+'__OT_SWKN_L.'+formatPliku):
                copyfile(qmlPath/Path("OT_SWKN_L.qml"), path+przestrzen_nazw+'__OT_SWKN_L.qml')
                OT_SWKN_L = QgsVectorLayer(path+przestrzen_nazw+"__OT_SWKN_L."+formatPliku, przestrzen_nazw+"__OT_SWKN_L","ogr")
                if OT_SWKN_L.featureCount()>0:
                    QgsProject.instance().addMapLayer(OT_SWKN_L, False)
                    group.addLayer(OT_SWKN_L)
                    OT_SWKN_L.loadNamedStyle(path+przestrzen_nazw+'__OT_SWKN_L.qml')
                    myLayerNode = root.findLayer(OT_SWKN_L.id())
                    myLayerNode.setExpanded(False)
                else:
                    OT_SWKN_L = None
            progress.setValue(23)
            if os.path.exists(path+przestrzen_nazw+'__OT_SWRS_L.'+formatPliku):
                copyfile(qmlPath/Path("OT_SWRS_L.qml"), path+przestrzen_nazw+'__OT_SWRS_L.qml')
                OT_SWRS_L = QgsVectorLayer(path+przestrzen_nazw+"__OT_SWRS_L."+formatPliku, przestrzen_nazw+"__OT_SWRS_L","ogr")
                if OT_SWRS_L.featureCount()>0:
                    QgsProject.instance().addMapLayer(OT_SWRS_L, False)
                    group.addLayer(OT_SWRS_L)
                    OT_SWRS_L.loadNamedStyle(path+przestrzen_nazw+'__OT_SWRS_L.qml')
                    myLayerNode = root.findLayer(OT_SWRS_L.id())
                    myLayerNode.setExpanded(False)
                else:
                    OT_SWRS_L = None
            progress.setValue(24)
            if os.path.exists(path+przestrzen_nazw+'__OT_OIMK_A.'+formatPliku):
                copyfile(qmlPath/Path("OT_OIMK_A.qml"), path+przestrzen_nazw+'__OT_OIMK_A.qml')
                OT_OIMK_A = QgsVectorLayer(path+przestrzen_nazw+"__OT_OIMK_A."+formatPliku, przestrzen_nazw+"__OT_OIMK_A","ogr")
                if OT_OIMK_A.featureCount()>0:
                    QgsProject.instance().addMapLayer(OT_OIMK_A, False)
                    group.addLayer(OT_OIMK_A)
                    OT_OIMK_A.loadNamedStyle(path+przestrzen_nazw+'__OT_OIMK_A.qml')
                    myLayerNode = root.findLayer(OT_OIMK_A.id())
                    myLayerNode.setExpanded(False)
                else:
                    OT_OIMK_A = None
            progress.setValue(25)
            if os.path.exists(path+przestrzen_nazw+'__OT_KUSC_A.'+formatPliku):
                copyfile(qmlPath/Path("OT_KUSC_A.qml"), path+przestrzen_nazw+'__OT_KUSC_A.qml')
                OT_KUSC_A = QgsVectorLayer(path+przestrzen_nazw+"__OT_KUSC_A."+formatPliku, przestrzen_nazw+"__OT_KUSC_A","ogr")
                if OT_KUSC_A.featureCount()>0:
                    QgsProject.instance().addMapLayer(OT_KUSC_A, False)
                    group.addLayer(OT_KUSC_A)
                    OT_KUSC_A.loadNamedStyle(path+przestrzen_nazw+'__OT_KUSC_A.qml')
                    myLayerNode = root.findLayer(OT_KUSC_A.id())
                    myLayerNode.setExpanded(False)
                else:
                    OT_KUSC_A = None
            progress.setValue(26)
            if os.path.exists(path+przestrzen_nazw+'__OT_PTZB_A.'+formatPliku):
                copyfile(qmlPath/Path("OT_PTZB_A.qml"), path+przestrzen_nazw+'__OT_PTZB_A.qml')
                OT_PTZB_A = QgsVectorLayer(path+przestrzen_nazw+"__OT_PTZB_A."+formatPliku, przestrzen_nazw+"__OT_PTZB_A","ogr")
                if OT_PTZB_A.featureCount()>0:
                    QgsProject.instance().addMapLayer(OT_PTZB_A, False)
                    group.addLayer(OT_PTZB_A)
                    OT_PTZB_A.loadNamedStyle(path+przestrzen_nazw+'__OT_PTZB_A.qml')
                    myLayerNode = root.findLayer(OT_PTZB_A.id())
                    myLayerNode.setExpanded(False)
                else:
                    OT_PTZB_A = None
            progress.setValue(27)
            if os.path.exists(path+przestrzen_nazw+'__OT_PTUT_A.'+formatPliku):
                copyfile(qmlPath/Path("OT_PTUT_A.qml"), path+przestrzen_nazw+'__OT_PTUT_A.qml')
                OT_PTUT_A = QgsVectorLayer(path+przestrzen_nazw+"__OT_PTUT_A."+formatPliku, przestrzen_nazw+"__OT_PTUT_A","ogr")
                if OT_PTUT_A.featureCount()>0:
                    QgsProject.instance().addMapLayer(OT_PTUT_A, False)
                    group.addLayer(OT_PTUT_A)
                    OT_PTUT_A.loadNamedStyle(path+przestrzen_nazw+'__OT_PTUT_A.qml')
                    myLayerNode = root.findLayer(OT_PTUT_A.id())
                    myLayerNode.setExpanded(False)
                else:
                    OT_PTUT_A = None
            progress.setValue(28)
            if os.path.exists(path+przestrzen_nazw+'__OT_PTGN_A.'+formatPliku):
                copyfile(qmlPath/Path("OT_PTGN_A.qml"), path+przestrzen_nazw+'__OT_PTGN_A.qml')
                OT_PTGN_A = QgsVectorLayer(path+przestrzen_nazw+"__OT_PTGN_A."+formatPliku, przestrzen_nazw+"__OT_PTGN_A","ogr")
                if OT_PTGN_A.featureCount()>0:
                    QgsProject.instance().addMapLayer(OT_PTGN_A, False)
                    group.addLayer(OT_PTGN_A)
                    OT_PTGN_A.loadNamedStyle(path+przestrzen_nazw+'__OT_PTGN_A.qml')
                    myLayerNode = root.findLayer(OT_PTGN_A.id())
                    myLayerNode.setExpanded(False)
                else:
                    OT_PTGN_A = None
            progress.setValue(29)
            if os.path.exists(path+przestrzen_nazw+'__OT_PTRK_A.'+formatPliku):
                copyfile(qmlPath/Path("OT_PTRK_A.qml"), path+przestrzen_nazw+'__OT_PTRK_A.qml')
                OT_PTRK_A = QgsVectorLayer(path+przestrzen_nazw+"__OT_PTRK_A."+formatPliku, przestrzen_nazw+"__OT_PTRK_A","ogr")
                if OT_PTRK_A.featureCount()>0:
                    QgsProject.instance().addMapLayer(OT_PTRK_A, False)
                    group.addLayer(OT_PTRK_A)
                    OT_PTRK_A.loadNamedStyle(path+przestrzen_nazw+'__OT_PTRK_A.qml')
                    myLayerNode = root.findLayer(OT_PTRK_A.id())
                    myLayerNode.setExpanded(False)
                else:
                    OT_PTRK_A = None
            progress.setValue(30)
            if os.path.exists(path+przestrzen_nazw+'__OT_PTNZ_A.'+formatPliku):
                copyfile(qmlPath/Path("OT_PTNZ_A.qml"), path+przestrzen_nazw+'__OT_PTNZ_A.qml')
                OT_PTNZ_A = QgsVectorLayer(path+przestrzen_nazw+"__OT_PTNZ_A."+formatPliku, przestrzen_nazw+"__OT_PTNZ_A","ogr")
                if OT_PTNZ_A.featureCount()>0:
                    QgsProject.instance().addMapLayer(OT_PTNZ_A, False)
                    group.addLayer(OT_PTNZ_A)
                    OT_PTNZ_A.loadNamedStyle(path+przestrzen_nazw+'__OT_PTNZ_A.qml')
                    myLayerNode = root.findLayer(OT_PTNZ_A.id())
                    myLayerNode.setExpanded(False)
                else:
                    OT_PTNZ_A = None
            progress.setValue(31)
            if os.path.exists(path+przestrzen_nazw+'__OT_PTLZ_A.'+formatPliku):
                copyfile(qmlPath/Path("OT_PTLZ_A.qml"), path+przestrzen_nazw+'__OT_PTLZ_A.qml')
                OT_PTLZ_A = QgsVectorLayer(path+przestrzen_nazw+"__OT_PTLZ_A."+formatPliku, przestrzen_nazw+"__OT_PTLZ_A","ogr")
                if OT_PTLZ_A.featureCount()>0:
                    QgsProject.instance().addMapLayer(OT_PTLZ_A, False)
                    group.addLayer(OT_PTLZ_A)
                    OT_PTLZ_A.loadNamedStyle(path+przestrzen_nazw+'__OT_PTLZ_A.qml')
                    myLayerNode = root.findLayer(OT_PTLZ_A.id())
                    myLayerNode.setExpanded(False)
                else:
                    OT_PTLZ_A = None
            progress.setValue(32)
            if os.path.exists(path+przestrzen_nazw+'__OT_PTTR_A.'+formatPliku):
                copyfile(qmlPath/Path("OT_PTTR_A.qml"), path+przestrzen_nazw+'__OT_PTTR_A.qml')
                OT_PTTR_A = QgsVectorLayer(path+przestrzen_nazw+"__OT_PTTR_A."+formatPliku, przestrzen_nazw+"__OT_PTTR_A","ogr")
                if OT_PTTR_A.featureCount()>0:
                    QgsProject.instance().addMapLayer(OT_PTTR_A, False)
                    group.addLayer(OT_PTTR_A)
                    OT_PTTR_A.loadNamedStyle(path+przestrzen_nazw+'__OT_PTTR_A.qml')
                    myLayerNode = root.findLayer(OT_PTTR_A.id())
                    myLayerNode.setExpanded(False)
                else:
                    OT_PTTR_A = None
            progress.setValue(33)
            
            time.sleep(1)
            iface.messageBar().clearWidgets()
    pass
