# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.0.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from sailsim.gui.mapView import MapViewWidget
from sailsim.gui.boatInspector import BoatInspectorWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(963, 596)
        MainWindow.setStyleSheet(u"")
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionOpenGithub = QAction(MainWindow)
        self.actionOpenGithub.setObjectName(u"actionOpenGithub")
        self.actionShowWaypoints = QAction(MainWindow)
        self.actionShowWaypoints.setObjectName(u"actionShowWaypoints")
        self.actionShowWaypoints.setCheckable(True)
        self.actionShowMainSailMapView = QAction(MainWindow)
        self.actionShowMainSailMapView.setObjectName(u"actionShowMainSailMapView")
        self.actionShowMainSailMapView.setCheckable(True)
        self.actionShowMainSailBoatInspector = QAction(MainWindow)
        self.actionShowMainSailBoatInspector.setObjectName(u"actionShowMainSailBoatInspector")
        self.actionShowMainSailBoatInspector.setCheckable(True)
        self.actionShowRudderMapView = QAction(MainWindow)
        self.actionShowRudderMapView.setObjectName(u"actionShowRudderMapView")
        self.actionShowRudderMapView.setCheckable(True)
        self.actionShowRudderBoatInspector = QAction(MainWindow)
        self.actionShowRudderBoatInspector.setObjectName(u"actionShowRudderBoatInspector")
        self.actionShowRudderBoatInspector.setCheckable(True)
        self.actionShowWaypointLink = QAction(MainWindow)
        self.actionShowWaypointLink.setObjectName(u"actionShowWaypointLink")
        self.actionShowWaypointLink.setCheckable(True)
        self.actionShowBoat = QAction(MainWindow)
        self.actionShowBoat.setObjectName(u"actionShowBoat")
        self.actionShowBoat.setCheckable(True)
        self.actionShowBoatDirection = QAction(MainWindow)
        self.actionShowBoatDirection.setObjectName(u"actionShowBoatDirection")
        self.actionShowBoatDirection.setCheckable(True)
        self.actionShowSpeed = QAction(MainWindow)
        self.actionShowSpeed.setObjectName(u"actionShowSpeed")
        self.actionShowSpeed.setCheckable(True)
        self.actionShowForces = QAction(MainWindow)
        self.actionShowForces.setObjectName(u"actionShowForces")
        self.actionShowForces.setCheckable(True)
        self.widget = QWidget(MainWindow)
        self.widget.setObjectName(u"widget")
        self.widget.setLocale(QLocale(QLocale.English, QLocale.Germany))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.main = QHBoxLayout()
        self.main.setSpacing(0)
        self.main.setObjectName(u"main")
        self.main.setSizeConstraint(QLayout.SetNoConstraint)
        self.mapView = MapViewWidget(self.widget)
        self.mapView.setObjectName(u"mapView")

        self.main.addWidget(self.mapView)

        self.boatInspector = BoatInspectorWidget(self.widget)
        self.boatInspector.setObjectName(u"boatInspector")

        self.main.addWidget(self.boatInspector)

        self.main.setStretch(0, 2)
        self.main.setStretch(1, 1)

        self.verticalLayout.addLayout(self.main)

        self.controlBar = QHBoxLayout()
        self.controlBar.setSpacing(0)
        self.controlBar.setObjectName(u"controlBar")
        self.buttonStartFrame = QToolButton(self.widget)
        self.buttonStartFrame.setObjectName(u"buttonStartFrame")

        self.controlBar.addWidget(self.buttonStartFrame)

        self.buttonDecFrame = QToolButton(self.widget)
        self.buttonDecFrame.setObjectName(u"buttonDecFrame")
        self.buttonDecFrame.setAutoRepeat(True)
        self.buttonDecFrame.setAutoRepeatDelay(200)
        self.buttonDecFrame.setAutoRepeatInterval(50)

        self.controlBar.addWidget(self.buttonDecFrame)

        self.buttonPlay = QToolButton(self.widget)
        self.buttonPlay.setObjectName(u"buttonPlay")
        self.buttonPlay.setCheckable(True)
        self.buttonPlay.setChecked(False)

        self.controlBar.addWidget(self.buttonPlay)

        self.buttonIncFrame = QToolButton(self.widget)
        self.buttonIncFrame.setObjectName(u"buttonIncFrame")
        self.buttonIncFrame.setAutoRepeat(True)
        self.buttonIncFrame.setAutoRepeatDelay(200)
        self.buttonIncFrame.setAutoRepeatInterval(50)

        self.controlBar.addWidget(self.buttonIncFrame)

        self.buttonEndFrame = QToolButton(self.widget)
        self.buttonEndFrame.setObjectName(u"buttonEndFrame")

        self.controlBar.addWidget(self.buttonEndFrame)

        self.frameNr = QLabel(self.widget)
        self.frameNr.setObjectName(u"frameNr")

        self.controlBar.addWidget(self.frameNr)

        self.timeSlider = QSlider(self.widget)
        self.timeSlider.setObjectName(u"timeSlider")
        self.timeSlider.setCursor(QCursor(Qt.OpenHandCursor))
        self.timeSlider.setMaximum(1024)
        self.timeSlider.setOrientation(Qt.Horizontal)

        self.controlBar.addWidget(self.timeSlider)


        self.verticalLayout.addLayout(self.controlBar)

        self.verticalLayout.setStretch(0, 1)
        MainWindow.setCentralWidget(self.widget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 963, 26))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuTools = QMenu(self.menubar)
        self.menuTools.setObjectName(u"menuTools")
        MainWindow.setMenuBar(self.menubar)
        QWidget.setTabOrder(self.buttonStartFrame, self.buttonDecFrame)
        QWidget.setTabOrder(self.buttonDecFrame, self.buttonPlay)
        QWidget.setTabOrder(self.buttonPlay, self.buttonIncFrame)
        QWidget.setTabOrder(self.buttonIncFrame, self.buttonEndFrame)
        QWidget.setTabOrder(self.buttonEndFrame, self.timeSlider)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuView.addAction(self.actionShowWaypoints)
        self.menuView.addAction(self.actionShowWaypointLink)
        self.menuView.addAction(self.actionShowMainSailMapView)
        self.menuView.addAction(self.actionShowRudderMapView)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionShowBoat)
        self.menuView.addAction(self.actionShowMainSailBoatInspector)
        self.menuView.addAction(self.actionShowRudderBoatInspector)
        self.menuView.addAction(self.actionShowBoatDirection)
        self.menuView.addAction(self.actionShowSpeed)
        self.menuView.addAction(self.actionShowForces)
        self.menuHelp.addAction(self.actionOpenGithub)

        self.retranslateUi(MainWindow)
        self.timeSlider.valueChanged.connect(MainWindow.updateFrame)
        self.buttonIncFrame.clicked.connect(MainWindow.incFrame)
        self.buttonDecFrame.clicked.connect(MainWindow.decFrame)
        self.buttonPlay.clicked.connect(MainWindow.pressedPlay)
        self.buttonStartFrame.clicked.connect(MainWindow.startFrame)
        self.buttonEndFrame.clicked.connect(MainWindow.endFrame)
        self.actionShowMainSailMapView.toggled.connect(MainWindow.actionViewShowMainSailMapView)
        self.actionShowRudderMapView.toggled.connect(MainWindow.actionViewShowRudderMapView)
        self.actionShowWaypointLink.toggled.connect(MainWindow.actionViewShowWaypointLink)
        self.actionShowWaypoints.toggled.connect(MainWindow.actionViewShowWaypoints)
        self.actionShowMainSailBoatInspector.toggled.connect(MainWindow.actionViewShowMainSailBoatInspector)
        self.actionShowRudderBoatInspector.toggled.connect(MainWindow.actionViewShowRudderBoatInspector)
        self.actionShowSpeed.toggled.connect(MainWindow.actionViewShowSpeed)
        self.actionShowForces.toggled.connect(MainWindow.actionViewShowForces)
        self.actionShowBoatDirection.toggled.connect(MainWindow.actionViewShowBoatDirection)
        self.actionShowBoat.toggled.connect(MainWindow.actionViewShowBoat)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SailsimGUI", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"New", None))
#if QT_CONFIG(shortcut)
        self.actionNew.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
#if QT_CONFIG(shortcut)
        self.actionOpen.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionOpenGithub.setText(QCoreApplication.translate("MainWindow", u"Open Github", None))
#if QT_CONFIG(tooltip)
        self.actionOpenGithub.setToolTip(QCoreApplication.translate("MainWindow", u"Open the sailsim repository on Github", None))
#endif // QT_CONFIG(tooltip)
        self.actionShowWaypoints.setText(QCoreApplication.translate("MainWindow", u"Waypoints", None))
        self.actionShowMainSailMapView.setText(QCoreApplication.translate("MainWindow", u"Main sail", None))
        self.actionShowMainSailBoatInspector.setText(QCoreApplication.translate("MainWindow", u"Main sail", None))
        self.actionShowRudderMapView.setText(QCoreApplication.translate("MainWindow", u"Rudder", None))
        self.actionShowRudderBoatInspector.setText(QCoreApplication.translate("MainWindow", u"Rudder", None))
#if QT_CONFIG(tooltip)
        self.actionShowRudderBoatInspector.setToolTip(QCoreApplication.translate("MainWindow", u"Show Rudder in Boat Inspector", None))
#endif // QT_CONFIG(tooltip)
        self.actionShowWaypointLink.setText(QCoreApplication.translate("MainWindow", u"Waypoint link", None))
        self.actionShowBoat.setText(QCoreApplication.translate("MainWindow", u"Boat", None))
        self.actionShowBoatDirection.setText(QCoreApplication.translate("MainWindow", u"Direction", None))
        self.actionShowSpeed.setText(QCoreApplication.translate("MainWindow", u"Speed", None))
        self.actionShowForces.setText(QCoreApplication.translate("MainWindow", u"Forces", None))
        self.buttonStartFrame.setText(QCoreApplication.translate("MainWindow", u"|<", None))
        self.buttonDecFrame.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.buttonPlay.setText(QCoreApplication.translate("MainWindow", u"|>", None))
        self.buttonIncFrame.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.buttonEndFrame.setText(QCoreApplication.translate("MainWindow", u">|", None))
        self.frameNr.setText(QCoreApplication.translate("MainWindow", u"0000/1023", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuTools.setTitle(QCoreApplication.translate("MainWindow", u"Tools", None))
    # retranslateUi

