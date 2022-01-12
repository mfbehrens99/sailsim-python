# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QGraphicsView, QHBoxLayout, QHeaderView,
    QLabel, QLayout, QMainWindow, QMenu,
    QMenuBar, QSizePolicy, QSlider, QToolButton,
    QTreeWidgetItem, QVBoxLayout, QWidget)

from sailsim.gui.mapView import MapViewView
from sailsim.gui.valueInspector import ValueInspectorWidget

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
        self.mapView = MapViewView(self.widget)
        self.mapView.setObjectName(u"mapView")
        self.mapView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.mapView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.mapView.setRenderHints(QPainter.Antialiasing)
        self.mapView.setDragMode(QGraphicsView.ScrollHandDrag)
        self.mapView.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)

        self.main.addWidget(self.mapView)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetNoConstraint)
        self.boatInspector = QGraphicsView(self.widget)
        self.boatInspector.setObjectName(u"boatInspector")
        self.boatInspector.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.boatInspector.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_3.addWidget(self.boatInspector)

        self.valueInspector = ValueInspectorWidget(self.widget)
        QTreeWidgetItem(self.valueInspector)
        QTreeWidgetItem(self.valueInspector)
        QTreeWidgetItem(self.valueInspector)
        QTreeWidgetItem(self.valueInspector)
        __qtreewidgetitem = QTreeWidgetItem(self.valueInspector)
        QTreeWidgetItem(__qtreewidgetitem)
        QTreeWidgetItem(__qtreewidgetitem)
        QTreeWidgetItem(__qtreewidgetitem)
        QTreeWidgetItem(__qtreewidgetitem)
        QTreeWidgetItem(__qtreewidgetitem)
        QTreeWidgetItem(__qtreewidgetitem)
        __qtreewidgetitem1 = QTreeWidgetItem(self.valueInspector)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        __qtreewidgetitem2 = QTreeWidgetItem(self.valueInspector)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem2)
        self.valueInspector.setObjectName(u"valueInspector")
        self.valueInspector.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.valueInspector.header().setCascadingSectionResizes(True)
        self.valueInspector.header().setMinimumSectionSize(30)
        self.valueInspector.header().setDefaultSectionSize(80)

        self.verticalLayout_3.addWidget(self.valueInspector)

        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 1)

        self.main.addLayout(self.verticalLayout_3)

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
        ___qtreewidgetitem = self.valueInspector.headerItem()
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("MainWindow", u"Unit", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("MainWindow", u"Y", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"X", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"Value", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"Name", None));

        __sortingEnabled = self.valueInspector.isSortingEnabled()
        self.valueInspector.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.valueInspector.topLevelItem(0)
        ___qtreewidgetitem1.setText(4, QCoreApplication.translate("MainWindow", u"m", None));
        ___qtreewidgetitem1.setText(3, QCoreApplication.translate("MainWindow", u"0", None));
        ___qtreewidgetitem1.setText(2, QCoreApplication.translate("MainWindow", u"0", None));
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("MainWindow", u"0", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"Position", None));
        ___qtreewidgetitem2 = self.valueInspector.topLevelItem(1)
        ___qtreewidgetitem2.setText(4, QCoreApplication.translate("MainWindow", u"Deg", None));
        ___qtreewidgetitem2.setText(1, QCoreApplication.translate("MainWindow", u"0", None));
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("MainWindow", u"Direction", None));
        ___qtreewidgetitem3 = self.valueInspector.topLevelItem(2)
        ___qtreewidgetitem3.setText(4, QCoreApplication.translate("MainWindow", u"m/s", None));
        ___qtreewidgetitem3.setText(3, QCoreApplication.translate("MainWindow", u"0", None));
        ___qtreewidgetitem3.setText(2, QCoreApplication.translate("MainWindow", u"0", None));
        ___qtreewidgetitem3.setText(1, QCoreApplication.translate("MainWindow", u"0", None));
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("MainWindow", u"Speed", None));
        ___qtreewidgetitem4 = self.valueInspector.topLevelItem(3)
        ___qtreewidgetitem4.setText(4, QCoreApplication.translate("MainWindow", u"deg/s", None));
        ___qtreewidgetitem4.setText(1, QCoreApplication.translate("MainWindow", u"0", None));
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("MainWindow", u"Ang speed", None));
        ___qtreewidgetitem5 = self.valueInspector.topLevelItem(4)
        ___qtreewidgetitem5.setText(4, QCoreApplication.translate("MainWindow", u"N", None));
        ___qtreewidgetitem5.setText(3, QCoreApplication.translate("MainWindow", u"0", None));
        ___qtreewidgetitem5.setText(2, QCoreApplication.translate("MainWindow", u"0", None));
        ___qtreewidgetitem5.setText(1, QCoreApplication.translate("MainWindow", u"0", None));
        ___qtreewidgetitem5.setText(0, QCoreApplication.translate("MainWindow", u"Force", None));
        ___qtreewidgetitem6 = ___qtreewidgetitem5.child(0)
        ___qtreewidgetitem6.setText(4, QCoreApplication.translate("MainWindow", u"N", None));
        ___qtreewidgetitem6.setText(3, QCoreApplication.translate("MainWindow", u"0", None));
        ___qtreewidgetitem6.setText(2, QCoreApplication.translate("MainWindow", u"0", None));
        ___qtreewidgetitem6.setText(1, QCoreApplication.translate("MainWindow", u"0", None));
        ___qtreewidgetitem6.setText(0, QCoreApplication.translate("MainWindow", u"SailDrag", None));
        ___qtreewidgetitem7 = ___qtreewidgetitem5.child(1)
        ___qtreewidgetitem7.setText(4, QCoreApplication.translate("MainWindow", u"N", None));
        ___qtreewidgetitem7.setText(3, QCoreApplication.translate("MainWindow", u"0", None));
        ___qtreewidgetitem7.setText(2, QCoreApplication.translate("MainWindow", u"0", None));
        ___qtreewidgetitem7.setText(1, QCoreApplication.translate("MainWindow", u"0", None));
        ___qtreewidgetitem7.setText(0, QCoreApplication.translate("MainWindow", u"SailLift", None));
        ___qtreewidgetitem8 = ___qtreewidgetitem5.child(2)
        ___qtreewidgetitem8.setText(4, QCoreApplication.translate("MainWindow", u"N", None));
        ___qtreewidgetitem8.setText(3, QCoreApplication.translate("MainWindow", u"0", None));
        ___qtreewidgetitem8.setText(2, QCoreApplication.translate("MainWindow", u"0", None));
        ___qtreewidgetitem8.setText(1, QCoreApplication.translate("MainWindow", u"0", None));
        ___qtreewidgetitem8.setText(0, QCoreApplication.translate("MainWindow", u"CenterboardDrag", None));
        ___qtreewidgetitem9 = ___qtreewidgetitem5.child(3)
        ___qtreewidgetitem9.setText(4, QCoreApplication.translate("MainWindow", u"N", None));
        ___qtreewidgetitem9.setText(3, QCoreApplication.translate("MainWindow", u"0", None));
        ___qtreewidgetitem9.setText(2, QCoreApplication.translate("MainWindow", u"0", None));
        ___qtreewidgetitem9.setText(1, QCoreApplication.translate("MainWindow", u"0", None));
        ___qtreewidgetitem9.setText(0, QCoreApplication.translate("MainWindow", u"CenterboardLift", None));
        ___qtreewidgetitem10 = ___qtreewidgetitem5.child(4)
        ___qtreewidgetitem10.setText(4, QCoreApplication.translate("MainWindow", u"N", None));
        ___qtreewidgetitem10.setText(3, QCoreApplication.translate("MainWindow", u"0", None));
        ___qtreewidgetitem10.setText(2, QCoreApplication.translate("MainWindow", u"0", None));
        ___qtreewidgetitem10.setText(1, QCoreApplication.translate("MainWindow", u"0", None));
        ___qtreewidgetitem10.setText(0, QCoreApplication.translate("MainWindow", u"RudderDrag", None));
        ___qtreewidgetitem11 = ___qtreewidgetitem5.child(5)
        ___qtreewidgetitem11.setText(4, QCoreApplication.translate("MainWindow", u"N", None));
        ___qtreewidgetitem11.setText(3, QCoreApplication.translate("MainWindow", u"0", None));
        ___qtreewidgetitem11.setText(2, QCoreApplication.translate("MainWindow", u"0", None));
        ___qtreewidgetitem11.setText(1, QCoreApplication.translate("MainWindow", u"0", None));
        ___qtreewidgetitem11.setText(0, QCoreApplication.translate("MainWindow", u"RudderLift", None));
        ___qtreewidgetitem12 = self.valueInspector.topLevelItem(5)
        ___qtreewidgetitem12.setText(4, QCoreApplication.translate("MainWindow", u"Nm", None));
        ___qtreewidgetitem12.setText(1, QCoreApplication.translate("MainWindow", u"0", None));
        ___qtreewidgetitem12.setText(0, QCoreApplication.translate("MainWindow", u"Torque", None));
        ___qtreewidgetitem13 = ___qtreewidgetitem12.child(0)
        ___qtreewidgetitem13.setText(4, QCoreApplication.translate("MainWindow", u"Nm", None));
        ___qtreewidgetitem13.setText(1, QCoreApplication.translate("MainWindow", u"0", None));
        ___qtreewidgetitem13.setText(0, QCoreApplication.translate("MainWindow", u"WaterDrag", None));
        ___qtreewidgetitem14 = ___qtreewidgetitem12.child(1)
        ___qtreewidgetitem14.setText(4, QCoreApplication.translate("MainWindow", u"Nm", None));
        ___qtreewidgetitem14.setText(0, QCoreApplication.translate("MainWindow", u"Centerboard", None));
        ___qtreewidgetitem15 = ___qtreewidgetitem12.child(2)
        ___qtreewidgetitem15.setText(4, QCoreApplication.translate("MainWindow", u"Nm", None));
        ___qtreewidgetitem15.setText(1, QCoreApplication.translate("MainWindow", u"0", None));
        ___qtreewidgetitem15.setText(0, QCoreApplication.translate("MainWindow", u"Rudder", None));
        ___qtreewidgetitem16 = ___qtreewidgetitem12.child(3)
        ___qtreewidgetitem16.setText(4, QCoreApplication.translate("MainWindow", u"Nm", None));
        ___qtreewidgetitem16.setText(1, QCoreApplication.translate("MainWindow", u"0", None));
        ___qtreewidgetitem16.setText(0, QCoreApplication.translate("MainWindow", u"Hull", None));
        ___qtreewidgetitem17 = self.valueInspector.topLevelItem(6)
        ___qtreewidgetitem17.setText(0, QCoreApplication.translate("MainWindow", u"Angle", None));
        ___qtreewidgetitem18 = ___qtreewidgetitem17.child(0)
        ___qtreewidgetitem18.setText(4, QCoreApplication.translate("MainWindow", u"Deg", None));
        ___qtreewidgetitem18.setText(0, QCoreApplication.translate("MainWindow", u"Main sail", None));
        ___qtreewidgetitem19 = ___qtreewidgetitem17.child(1)
        ___qtreewidgetitem19.setText(4, QCoreApplication.translate("MainWindow", u"Deg", None));
        ___qtreewidgetitem19.setText(0, QCoreApplication.translate("MainWindow", u"Rudder", None));
        ___qtreewidgetitem20 = ___qtreewidgetitem17.child(2)
        ___qtreewidgetitem20.setText(4, QCoreApplication.translate("MainWindow", u"Deg", None));
        ___qtreewidgetitem20.setText(0, QCoreApplication.translate("MainWindow", u"LeewayAngle", None));
        self.valueInspector.setSortingEnabled(__sortingEnabled)

        self.buttonStartFrame.setText(QCoreApplication.translate("MainWindow", u"\u23ee", None))
        self.buttonDecFrame.setText(QCoreApplication.translate("MainWindow", u"\u23ea", None))
        self.buttonPlay.setText(QCoreApplication.translate("MainWindow", u"\u23f5", None))
        self.buttonIncFrame.setText(QCoreApplication.translate("MainWindow", u"\u23e9", None))
        self.buttonEndFrame.setText(QCoreApplication.translate("MainWindow", u"\u23ed", None))
        self.frameNr.setText(QCoreApplication.translate("MainWindow", u"0000/1000", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuTools.setTitle(QCoreApplication.translate("MainWindow", u"Tools", None))
    # retranslateUi
