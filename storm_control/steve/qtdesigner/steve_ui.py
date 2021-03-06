# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'steve.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1148, 831)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.mosaicTab = QtWidgets.QWidget()
        self.mosaicTab.setObjectName("mosaicTab")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.mosaicTab)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.mosaicFrame = QtWidgets.QFrame(self.mosaicTab)
        self.mosaicFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mosaicFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mosaicFrame.setObjectName("mosaicFrame")
        self.horizontalLayout_2.addWidget(self.mosaicFrame)
        self.widget = QtWidgets.QWidget(self.mosaicTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(0, 0))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 100000))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.positionsGroupBox = QtWidgets.QGroupBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.positionsGroupBox.sizePolicy().hasHeightForWidth())
        self.positionsGroupBox.setSizePolicy(sizePolicy)
        self.positionsGroupBox.setMinimumSize(QtCore.QSize(0, 0))
        self.positionsGroupBox.setMaximumSize(QtCore.QSize(10000, 10000))
        self.positionsGroupBox.setObjectName("positionsGroupBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.positionsGroupBox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.positionsFrame = QtWidgets.QFrame(self.positionsGroupBox)
        self.positionsFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.positionsFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.positionsFrame.setObjectName("positionsFrame")
        self.verticalLayout_4.addWidget(self.positionsFrame)
        self.verticalLayout_2.addWidget(self.positionsGroupBox)
        self.tilesGroupBox = QtWidgets.QGroupBox(self.widget)
        self.tilesGroupBox.setMinimumSize(QtCore.QSize(300, 150))
        self.tilesGroupBox.setMaximumSize(QtCore.QSize(300, 300))
        self.tilesGroupBox.setObjectName("tilesGroupBox")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.tilesGroupBox)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.startingPositionLabel = QtWidgets.QLabel(self.tilesGroupBox)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.startingPositionLabel.setFont(font)
        self.startingPositionLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.startingPositionLabel.setObjectName("startingPositionLabel")
        self.verticalLayout_3.addWidget(self.startingPositionLabel)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.xPosLabel = QtWidgets.QLabel(self.tilesGroupBox)
        self.xPosLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.xPosLabel.setObjectName("xPosLabel")
        self.horizontalLayout_4.addWidget(self.xPosLabel)
        self.xStartPosSpinBox = QtWidgets.QDoubleSpinBox(self.tilesGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xStartPosSpinBox.sizePolicy().hasHeightForWidth())
        self.xStartPosSpinBox.setSizePolicy(sizePolicy)
        self.xStartPosSpinBox.setMinimum(-50000.0)
        self.xStartPosSpinBox.setMaximum(50000.0)
        self.xStartPosSpinBox.setObjectName("xStartPosSpinBox")
        self.horizontalLayout_4.addWidget(self.xStartPosSpinBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.yPosLabel = QtWidgets.QLabel(self.tilesGroupBox)
        self.yPosLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.yPosLabel.setObjectName("yPosLabel")
        self.horizontalLayout_6.addWidget(self.yPosLabel)
        self.yStartPosSpinBox = QtWidgets.QDoubleSpinBox(self.tilesGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.yStartPosSpinBox.sizePolicy().hasHeightForWidth())
        self.yStartPosSpinBox.setSizePolicy(sizePolicy)
        self.yStartPosSpinBox.setMinimum(-50000.0)
        self.yStartPosSpinBox.setMaximum(500000.0)
        self.yStartPosSpinBox.setObjectName("yStartPosSpinBox")
        self.horizontalLayout_6.addWidget(self.yStartPosSpinBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_8.addLayout(self.verticalLayout_3)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.gridDimLabel = QtWidgets.QLabel(self.tilesGroupBox)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.gridDimLabel.setFont(font)
        self.gridDimLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.gridDimLabel.setObjectName("gridDimLabel")
        self.verticalLayout_7.addWidget(self.gridDimLabel)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.numXLabel = QtWidgets.QLabel(self.tilesGroupBox)
        self.numXLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.numXLabel.setObjectName("numXLabel")
        self.horizontalLayout_5.addWidget(self.numXLabel)
        self.xSpinBox = QtWidgets.QSpinBox(self.tilesGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xSpinBox.sizePolicy().hasHeightForWidth())
        self.xSpinBox.setSizePolicy(sizePolicy)
        self.xSpinBox.setMinimum(1)
        self.xSpinBox.setProperty("value", 5)
        self.xSpinBox.setObjectName("xSpinBox")
        self.horizontalLayout_5.addWidget(self.xSpinBox)
        self.verticalLayout_7.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.numYLabel = QtWidgets.QLabel(self.tilesGroupBox)
        self.numYLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.numYLabel.setObjectName("numYLabel")
        self.horizontalLayout_7.addWidget(self.numYLabel)
        self.ySpinBox = QtWidgets.QSpinBox(self.tilesGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ySpinBox.sizePolicy().hasHeightForWidth())
        self.ySpinBox.setSizePolicy(sizePolicy)
        self.ySpinBox.setMinimum(1)
        self.ySpinBox.setProperty("value", 3)
        self.ySpinBox.setObjectName("ySpinBox")
        self.horizontalLayout_7.addWidget(self.ySpinBox)
        self.verticalLayout_7.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8.addLayout(self.verticalLayout_7)
        self.verticalLayout_8.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.getStagePosButton = QtWidgets.QPushButton(self.tilesGroupBox)
        self.getStagePosButton.setMaximumSize(QtCore.QSize(150, 16777215))
        self.getStagePosButton.setObjectName("getStagePosButton")
        self.horizontalLayout_10.addWidget(self.getStagePosButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem)
        self.imageGridButton = QtWidgets.QPushButton(self.tilesGroupBox)
        self.imageGridButton.setMaximumSize(QtCore.QSize(150, 16777215))
        self.imageGridButton.setObjectName("imageGridButton")
        self.horizontalLayout_10.addWidget(self.imageGridButton)
        self.verticalLayout_8.addLayout(self.horizontalLayout_10)
        self.verticalLayout_2.addWidget(self.tilesGroupBox)
        self.objectivesGroupBox = ObjectivesGroupBox(self.widget)
        self.objectivesGroupBox.setMinimumSize(QtCore.QSize(250, 50))
        self.objectivesGroupBox.setMaximumSize(QtCore.QSize(300, 300))
        self.objectivesGroupBox.setObjectName("objectivesGroupBox")
        self.verticalLayout_2.addWidget(self.objectivesGroupBox)
        self.miscGroupBox = QtWidgets.QGroupBox(self.widget)
        self.miscGroupBox.setMinimumSize(QtCore.QSize(0, 20))
        self.miscGroupBox.setObjectName("miscGroupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.miscGroupBox)
        self.verticalLayout.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.trackStageCheckBox = QtWidgets.QCheckBox(self.miscGroupBox)
        self.trackStageCheckBox.setObjectName("trackStageCheckBox")
        self.horizontalLayout.addWidget(self.trackStageCheckBox)
        self.scaleLabel = QtWidgets.QLabel(self.miscGroupBox)
        self.scaleLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.scaleLabel.setObjectName("scaleLabel")
        self.horizontalLayout.addWidget(self.scaleLabel)
        self.scaleLineEdit = QtWidgets.QLineEdit(self.miscGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scaleLineEdit.sizePolicy().hasHeightForWidth())
        self.scaleLineEdit.setSizePolicy(sizePolicy)
        self.scaleLineEdit.setMaximumSize(QtCore.QSize(100, 16777215))
        self.scaleLineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.scaleLineEdit.setObjectName("scaleLineEdit")
        self.horizontalLayout.addWidget(self.scaleLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.cursorPosition = QtWidgets.QLabel(self.miscGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cursorPosition.sizePolicy().hasHeightForWidth())
        self.cursorPosition.setSizePolicy(sizePolicy)
        self.cursorPosition.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.cursorPosition.setObjectName("cursorPosition")
        self.horizontalLayout_9.addWidget(self.cursorPosition)
        self.mosaicLabel = QtWidgets.QLabel(self.miscGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mosaicLabel.sizePolicy().hasHeightForWidth())
        self.mosaicLabel.setSizePolicy(sizePolicy)
        self.mosaicLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.mosaicLabel.setObjectName("mosaicLabel")
        self.horizontalLayout_9.addWidget(self.mosaicLabel)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.verticalLayout_2.addWidget(self.miscGroupBox)
        self.horizontalLayout_2.addWidget(self.widget)
        self.tabWidget.addTab(self.mosaicTab, "")
        self.sectionsTab = QtWidgets.QWidget()
        self.sectionsTab.setObjectName("sectionsTab")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.sectionsTab)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.sectionsDisplayFrame = QtWidgets.QFrame(self.sectionsTab)
        self.sectionsDisplayFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sectionsDisplayFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sectionsDisplayFrame.setObjectName("sectionsDisplayFrame")
        self.horizontalLayout_3.addWidget(self.sectionsDisplayFrame)
        self.sectionsWidget = QtWidgets.QWidget(self.sectionsTab)
        self.sectionsWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.sectionsWidget.setMaximumSize(QtCore.QSize(300, 16777215))
        self.sectionsWidget.setObjectName("sectionsWidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.sectionsWidget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.sectionsGroupBox = QtWidgets.QGroupBox(self.sectionsWidget)
        self.sectionsGroupBox.setMaximumSize(QtCore.QSize(100000, 16777215))
        self.sectionsGroupBox.setObjectName("sectionsGroupBox")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.sectionsGroupBox)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.sectionsScrollArea = QtWidgets.QScrollArea(self.sectionsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sectionsScrollArea.sizePolicy().hasHeightForWidth())
        self.sectionsScrollArea.setSizePolicy(sizePolicy)
        self.sectionsScrollArea.setWidgetResizable(True)
        self.sectionsScrollArea.setObjectName("sectionsScrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 98, 28))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.sectionsScrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_6.addWidget(self.sectionsScrollArea)
        self.verticalLayout_5.addWidget(self.sectionsGroupBox)
        self.sectionViewSettingsGroupBox = QtWidgets.QGroupBox(self.sectionsWidget)
        self.sectionViewSettingsGroupBox.setMaximumSize(QtCore.QSize(16777215, 120))
        self.sectionViewSettingsGroupBox.setObjectName("sectionViewSettingsGroupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.sectionViewSettingsGroupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.thresholdLabel = QtWidgets.QLabel(self.sectionViewSettingsGroupBox)
        self.thresholdLabel.setObjectName("thresholdLabel")
        self.gridLayout.addWidget(self.thresholdLabel, 1, 0, 1, 1)
        self.foregroundOpacitySlider = QtWidgets.QSlider(self.sectionViewSettingsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.foregroundOpacitySlider.sizePolicy().hasHeightForWidth())
        self.foregroundOpacitySlider.setSizePolicy(sizePolicy)
        self.foregroundOpacitySlider.setMaximum(100)
        self.foregroundOpacitySlider.setProperty("value", 50)
        self.foregroundOpacitySlider.setOrientation(QtCore.Qt.Horizontal)
        self.foregroundOpacitySlider.setObjectName("foregroundOpacitySlider")
        self.gridLayout.addWidget(self.foregroundOpacitySlider, 4, 1, 1, 1)
        self.moveAllSectionsCheckBox = QtWidgets.QCheckBox(self.sectionViewSettingsGroupBox)
        self.moveAllSectionsCheckBox.setObjectName("moveAllSectionsCheckBox")
        self.gridLayout.addWidget(self.moveAllSectionsCheckBox, 0, 0, 1, 1)
        self.foregroundOpacityLabel = QtWidgets.QLabel(self.sectionViewSettingsGroupBox)
        self.foregroundOpacityLabel.setObjectName("foregroundOpacityLabel")
        self.gridLayout.addWidget(self.foregroundOpacityLabel, 4, 0, 1, 1)
        self.showFeaturesCheckBox = QtWidgets.QCheckBox(self.sectionViewSettingsGroupBox)
        self.showFeaturesCheckBox.setObjectName("showFeaturesCheckBox")
        self.gridLayout.addWidget(self.showFeaturesCheckBox, 0, 1, 1, 1)
        self.backgroundLabel = QtWidgets.QLabel(self.sectionViewSettingsGroupBox)
        self.backgroundLabel.setObjectName("backgroundLabel")
        self.gridLayout.addWidget(self.backgroundLabel, 2, 0, 1, 1)
        self.backgroundComboBox = QtWidgets.QComboBox(self.sectionViewSettingsGroupBox)
        self.backgroundComboBox.setObjectName("backgroundComboBox")
        self.backgroundComboBox.addItem("")
        self.gridLayout.addWidget(self.backgroundComboBox, 2, 1, 1, 1)
        self.thresholdSlider = QtWidgets.QSlider(self.sectionViewSettingsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.thresholdSlider.sizePolicy().hasHeightForWidth())
        self.thresholdSlider.setSizePolicy(sizePolicy)
        self.thresholdSlider.setMaximum(100)
        self.thresholdSlider.setProperty("value", 50)
        self.thresholdSlider.setOrientation(QtCore.Qt.Horizontal)
        self.thresholdSlider.setObjectName("thresholdSlider")
        self.gridLayout.addWidget(self.thresholdSlider, 1, 1, 1, 1)
        self.verticalLayout_5.addWidget(self.sectionViewSettingsGroupBox)
        self.horizontalLayout_3.addWidget(self.sectionsWidget)
        self.tabWidget.addTab(self.sectionsTab, "")
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1148, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionConnect = QtWidgets.QAction(MainWindow)
        self.actionConnect.setObjectName("actionConnect")
        self.actionDisconnect = QtWidgets.QAction(MainWindow)
        self.actionDisconnect.setObjectName("actionDisconnect")
        self.actionSave_Positions = QtWidgets.QAction(MainWindow)
        self.actionSave_Positions.setObjectName("actionSave_Positions")
        self.actionSave_Mosaic = QtWidgets.QAction(MainWindow)
        self.actionSave_Mosaic.setObjectName("actionSave_Mosaic")
        self.actionSet_Working_Directory = QtWidgets.QAction(MainWindow)
        self.actionSet_Working_Directory.setObjectName("actionSet_Working_Directory")
        self.actionLoad_Mosaic = QtWidgets.QAction(MainWindow)
        self.actionLoad_Mosaic.setObjectName("actionLoad_Mosaic")
        self.actionDelete_Images = QtWidgets.QAction(MainWindow)
        self.actionDelete_Images.setObjectName("actionDelete_Images")
        self.actionLoad_Positions = QtWidgets.QAction(MainWindow)
        self.actionLoad_Positions.setObjectName("actionLoad_Positions")
        self.actionSave_Snapshot = QtWidgets.QAction(MainWindow)
        self.actionSave_Snapshot.setObjectName("actionSave_Snapshot")
        self.actionLoad_Movie = QtWidgets.QAction(MainWindow)
        self.actionLoad_Movie.setObjectName("actionLoad_Movie")
        self.actionLoad_Dax_By_Pattern = QtWidgets.QAction(MainWindow)
        self.actionLoad_Dax_By_Pattern.setObjectName("actionLoad_Dax_By_Pattern")
        self.actionAdjust_Contrast = QtWidgets.QAction(MainWindow)
        self.actionAdjust_Contrast.setObjectName("actionAdjust_Contrast")
        self.menuFile.addAction(self.actionSet_Working_Directory)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionDelete_Images)
        self.menuFile.addAction(self.actionLoad_Movie)
        self.menuFile.addAction(self.actionLoad_Mosaic)
        self.menuFile.addAction(self.actionLoad_Positions)
        self.menuFile.addAction(self.actionSave_Mosaic)
        self.menuFile.addAction(self.actionSave_Positions)
        self.menuFile.addAction(self.actionSave_Snapshot)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuView.addAction(self.actionAdjust_Contrast)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.xStartPosSpinBox, self.yStartPosSpinBox)
        MainWindow.setTabOrder(self.yStartPosSpinBox, self.xSpinBox)
        MainWindow.setTabOrder(self.xSpinBox, self.ySpinBox)
        MainWindow.setTabOrder(self.ySpinBox, self.tabWidget)
        MainWindow.setTabOrder(self.tabWidget, self.foregroundOpacitySlider)
        MainWindow.setTabOrder(self.foregroundOpacitySlider, self.backgroundComboBox)
        MainWindow.setTabOrder(self.backgroundComboBox, self.thresholdSlider)
        MainWindow.setTabOrder(self.thresholdSlider, self.showFeaturesCheckBox)
        MainWindow.setTabOrder(self.showFeaturesCheckBox, self.moveAllSectionsCheckBox)
        MainWindow.setTabOrder(self.moveAllSectionsCheckBox, self.sectionsScrollArea)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Steve"))
        self.positionsGroupBox.setTitle(_translate("MainWindow", "Positions"))
        self.tilesGroupBox.setTitle(_translate("MainWindow", "Tile Settings"))
        self.startingPositionLabel.setText(_translate("MainWindow", "Center"))
        self.xPosLabel.setText(_translate("MainWindow", "X:"))
        self.yPosLabel.setText(_translate("MainWindow", "Y:"))
        self.gridDimLabel.setText(_translate("MainWindow", "Grid Size"))
        self.numXLabel.setText(_translate("MainWindow", "# X:"))
        self.numYLabel.setText(_translate("MainWindow", "# Y:"))
        self.getStagePosButton.setText(_translate("MainWindow", "Get Stage Position"))
        self.imageGridButton.setText(_translate("MainWindow", "Acquire"))
        self.objectivesGroupBox.setTitle(_translate("MainWindow", "Objective Settings"))
        self.miscGroupBox.setTitle(_translate("MainWindow", "Misc"))
        self.trackStageCheckBox.setText(_translate("MainWindow", "Track Stage"))
        self.scaleLabel.setText(_translate("MainWindow", "Scale:"))
        self.scaleLineEdit.setText(_translate("MainWindow", "1.0"))
        self.cursorPosition.setText(_translate("MainWindow", "Cursor:"))
        self.mosaicLabel.setText(_translate("MainWindow", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.mosaicTab), _translate("MainWindow", "Mosaic"))
        self.sectionsGroupBox.setTitle(_translate("MainWindow", "Sections"))
        self.sectionViewSettingsGroupBox.setTitle(_translate("MainWindow", "Section View Settings"))
        self.thresholdLabel.setText(_translate("MainWindow", "Threshold"))
        self.moveAllSectionsCheckBox.setText(_translate("MainWindow", "Move All Sections"))
        self.foregroundOpacityLabel.setText(_translate("MainWindow", "Section Opacity"))
        self.showFeaturesCheckBox.setText(_translate("MainWindow", "Show Features"))
        self.backgroundLabel.setText(_translate("MainWindow", "Background Type"))
        self.backgroundComboBox.setItemText(0, _translate("MainWindow", "Mean"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.sectionsTab), _translate("MainWindow", "Sections"))
        self.menuFile.setTitle(_translate("MainWindow", "Fi&le"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.actionQuit.setText(_translate("MainWindow", "&Quit (Ctrl+Q)"))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionConnect.setText(_translate("MainWindow", "Connect"))
        self.actionDisconnect.setText(_translate("MainWindow", "Disconnect"))
        self.actionSave_Positions.setText(_translate("MainWindow", "Sav&e Positions"))
        self.actionSave_Positions.setShortcut(_translate("MainWindow", "Ctrl+T"))
        self.actionSave_Mosaic.setText(_translate("MainWindow", "Sa&ve Mosaic"))
        self.actionSave_Mosaic.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionSet_Working_Directory.setText(_translate("MainWindow", "&Set Working Directory"))
        self.actionLoad_Mosaic.setText(_translate("MainWindow", "Load &Mosaic"))
        self.actionLoad_Mosaic.setShortcut(_translate("MainWindow", "Ctrl+M"))
        self.actionDelete_Images.setText(_translate("MainWindow", "&Delete Images"))
        self.actionDelete_Images.setShortcut(_translate("MainWindow", "Ctrl+D"))
        self.actionLoad_Positions.setText(_translate("MainWindow", "Load &Positions"))
        self.actionLoad_Positions.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.actionSave_Snapshot.setText(_translate("MainWindow", "Save S&napshot"))
        self.actionSave_Snapshot.setShortcut(_translate("MainWindow", "Ctrl+I"))
        self.actionLoad_Movie.setText(_translate("MainWindow", "&Load Movie"))
        self.actionLoad_Movie.setShortcut(_translate("MainWindow", "Ctrl+L"))
        self.actionLoad_Dax_By_Pattern.setText(_translate("MainWindow", "Load Dax By Pattern"))
        self.actionAdjust_Contrast.setText(_translate("MainWindow", "&Adjust Contrast"))
        self.actionAdjust_Contrast.setShortcut(_translate("MainWindow", "Ctrl+C"))

from storm_control.steve.objectives import ObjectivesGroupBox
