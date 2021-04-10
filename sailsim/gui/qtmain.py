# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.0.2
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
        self.actionOpen_project_on_Github = QAction(MainWindow)
        self.actionOpen_project_on_Github.setObjectName(u"actionOpen_project_on_Github")
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
        self.toolButton = QToolButton(self.widget)
        self.toolButton.setObjectName(u"toolButton")

        self.controlBar.addWidget(self.toolButton)

        self.toolButton_2 = QToolButton(self.widget)
        self.toolButton_2.setObjectName(u"toolButton_2")

        self.controlBar.addWidget(self.toolButton_2)

        self.toolButton_3 = QToolButton(self.widget)
        self.toolButton_3.setObjectName(u"toolButton_3")

        self.controlBar.addWidget(self.toolButton_3)

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
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuHelp.addAction(self.actionOpen_project_on_Github)

        self.retranslateUi(MainWindow)
        self.timeSlider.valueChanged.connect(self.mapView.viewFrame)
        self.timeSlider.valueChanged.connect(self.frameNr.setNum)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionOpen_project_on_Github.setText(QCoreApplication.translate("MainWindow", u"Open on Github", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"|<", None))
        self.toolButton_2.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.toolButton_3.setText(QCoreApplication.translate("MainWindow", u">|", None))
        self.frameNr.setText(QCoreApplication.translate("MainWindow", u"0000/1023", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

