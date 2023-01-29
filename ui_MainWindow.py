# -*- coding: utf-8 -*-



################################################################################

## Form generated from reading UI file 'untitled.ui'

##

## Created by: Qt User Interface Compiler version 6.4.2

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

from PySide6.QtWidgets import (QApplication, QCheckBox, QGroupBox, QLabel,

    QMainWindow, QMenu, QMenuBar, QPushButton,

    QSizePolicy, QSlider, QStatusBar, QToolButton,

    QVBoxLayout, QWidget)

from clickableLabel import ClickableLabel

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):

        if not MainWindow.objectName():

            MainWindow.setObjectName(u"MainWindow")

        MainWindow.resize(1045, 822)

        self.actionSave_file_as = QAction(MainWindow)

        self.actionSave_file_as.setObjectName(u"actionSave_file_as")

        self.actionOpen_file = QAction(MainWindow)

        self.actionOpen_file.setObjectName(u"actionOpen_file")

        self.actionSave_file = QAction(MainWindow)

        self.actionSave_file.setObjectName(u"actionSave_file")

        self.actionNew = QAction(MainWindow)

        self.actionNew.setObjectName(u"actionNew")

        self.centralwidget = QWidget(MainWindow)

        self.centralwidget.setObjectName(u"centralwidget")

        self.widget = QWidget(self.centralwidget)

        self.widget.setObjectName(u"widget")

        self.widget.setGeometry(QRect(40, 420, 971, 311))

        self.widgetFrames = QWidget(self.widget)

        self.widgetFrames.setObjectName(u"widgetFrames")

        self.widgetFrames.setGeometry(QRect(10, 10, 951, 181))

        self.toolButtonSub = QToolButton(self.widgetFrames)

        self.toolButtonSub.setObjectName(u"toolButtonSub")

        self.toolButtonSub.setGeometry(QRect(0, 0, 51, 181))

        self.toolButtonSubOne = QToolButton(self.widgetFrames)

        self.toolButtonSubOne.setObjectName(u"toolButtonSubOne")

        self.toolButtonSubOne.setGeometry(QRect(50, 0, 51, 181))

        self.toolButtonAddOne = QToolButton(self.widgetFrames)

        self.toolButtonAddOne.setObjectName(u"toolButtonAddOne")

        self.toolButtonAddOne.setGeometry(QRect(850, 0, 51, 181))

        self.toolButtonAdd = QToolButton(self.widgetFrames)

        self.toolButtonAdd.setObjectName(u"toolButtonAdd")

        self.toolButtonAdd.setGeometry(QRect(900, 0, 51, 181))

        self.label1 = ClickableLabel(self.widgetFrames)

        self.label1.setObjectName(u"label1")

        self.label1.setGeometry(QRect(100, 0, 151, 181))

        self.label1.setScaledContents(True)

        self.label2 = ClickableLabel(self.widgetFrames)

        self.label2.setObjectName(u"label2")

        self.label2.setGeometry(QRect(250, 0, 151, 181))

        self.label2.setScaledContents(True)

        self.label3 = ClickableLabel(self.widgetFrames)

        self.label3.setObjectName(u"label3")

        self.label3.setGeometry(QRect(400, 0, 151, 181))

        self.label3.setScaledContents(True)

        self.label4 = ClickableLabel(self.widgetFrames)

        self.label4.setObjectName(u"label4")

        self.label4.setGeometry(QRect(550, 0, 151, 181))

        self.label4.setScaledContents(True)

        self.label5 = ClickableLabel(self.widgetFrames)

        self.label5.setObjectName(u"label5")

        self.label5.setGeometry(QRect(700, 0, 151, 181))

        self.label5.setScaledContents(True)

        self.vid_time = QLabel(self.widget)
        self.vid_time.setFont(QFont('Arial', 20))
        self.vid_time.setObjectName(u"vid_time")

        self.vid_time.setGeometry(QRect(971/2-10, 210, 151, 181))


        self.vid_time.setScaledContents(True)

        self.vid_time_total = QLabel(self.widget)
        self.vid_time_total.setFont(QFont('Arial', 20))
        self.vid_time_total.setObjectName(u"vid_time")

        self.vid_time_total.setGeometry(QRect(815, 210, 151, 181))


        self.vid_time_zero = QLabel(self.widget)
        self.vid_time_zero.setFont(QFont('Arial', 20))
        self.vid_time_zero.setObjectName(u"vid_time")
        self.vid_time_zero.setText("0:0")
        self.vid_time_zero.setGeometry(QRect(110, 210, 151, 181))

        self.horizontalSlider = QSlider(self.widget)

        self.horizontalSlider.setObjectName(u"horizontalSlider")

        self.horizontalSlider.setGeometry(QRect(120, 230, 721, 51))

        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.widgetEffectsAndFrame = QWidget(self.centralwidget)

        self.widgetEffectsAndFrame.setObjectName(u"widgetEffectsAndFrame")

        self.widgetEffectsAndFrame.setGeometry(QRect(10, 0, 1021, 341))

        self.groupBox = QGroupBox(self.widgetEffectsAndFrame)

        self.groupBox.setObjectName(u"groupBox")

        self.groupBox.setGeometry(QRect(0, 0, 211, 341))

        self.pushButtonVideo = QPushButton(self.groupBox)

        self.pushButtonVideo.setObjectName(u"pushButtonVideo")

        self.pushButtonVideo.setGeometry(QRect(40, 200, 131, 41))

        self.pushButtonFrame = QPushButton(self.groupBox)

        self.pushButtonFrame.setObjectName(u"pushButtonFrame")

        self.pushButtonFrame.setGeometry(QRect(40, 260, 131, 41))

        self.widget1 = QWidget(self.groupBox)

        self.widget1.setObjectName(u"widget1")

        self.widget1.setGeometry(QRect(20, 30, 81, 152))

        self.verticalLayout = QVBoxLayout(self.widget1)

        self.verticalLayout.setObjectName(u"verticalLayout")

        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.checkBox = QCheckBox(self.widget1)

        self.checkBox.setObjectName(u"checkBox")



        self.verticalLayout.addWidget(self.checkBox)



        self.checkBox_2 = QCheckBox(self.widget1)

        self.checkBox_2.setObjectName(u"checkBox_2")



        self.verticalLayout.addWidget(self.checkBox_2)



        self.checkBox_3 = QCheckBox(self.widget1)

        self.checkBox_3.setObjectName(u"checkBox_3")



        self.verticalLayout.addWidget(self.checkBox_3)



        self.checkBox_4 = QCheckBox(self.widget1)

        self.checkBox_4.setObjectName(u"checkBox_4")



        self.verticalLayout.addWidget(self.checkBox_4)



        self.checkBox_5 = QCheckBox(self.widget1)

        self.checkBox_5.setObjectName(u"checkBox_5")



        self.verticalLayout.addWidget(self.checkBox_5)



        self.checkBox_6 = QCheckBox(self.widget1)

        self.checkBox_6.setObjectName(u"checkBox_6")



        self.verticalLayout.addWidget(self.checkBox_6)



        self.photoWithEffects = QLabel(self.widgetEffectsAndFrame)

        self.photoWithEffects.setObjectName(u"photoWithEffects")

        self.photoWithEffects.setGeometry(QRect(210, 0, 451, 341))

        self.photoWithEffects.setScaledContents(True)

        self.photoWoEffects = QLabel(self.widgetEffectsAndFrame)

        self.photoWoEffects.setObjectName(u"photoWoEffects")

        self.photoWoEffects.setGeometry(QRect(660, 0, 361, 341))

        self.photoWoEffects.setScaledContents(True)

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QMenuBar(MainWindow)

        self.menubar.setObjectName(u"menubar")

        self.menubar.setGeometry(QRect(0, 0, 1045, 22))

        self.menuFile = QMenu(self.menubar)

        self.menuFile.setObjectName(u"menuFile")

        self.menuView = QMenu(self.menubar)

        self.menuView.setObjectName(u"menuView")

        self.menuEdit = QMenu(self.menubar)

        self.menuEdit.setObjectName(u"menuEdit")

        self.menuHelp = QMenu(self.menubar)

        self.menuHelp.setObjectName(u"menuHelp")

        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QStatusBar(MainWindow)

        self.statusbar.setObjectName(u"statusbar")

        MainWindow.setStatusBar(self.statusbar)



        self.menubar.addAction(self.menuFile.menuAction())

        self.menubar.addAction(self.menuEdit.menuAction())

        self.menubar.addAction(self.menuView.menuAction())

        self.menubar.addAction(self.menuHelp.menuAction())

        self.menuFile.addAction(self.actionSave_file_as)

        self.menuFile.addAction(self.actionOpen_file)

        self.menuFile.addAction(self.actionSave_file)

        self.menuFile.addAction(self.actionNew)



        self.retranslateUi(MainWindow)



        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi



    def retranslateUi(self, MainWindow):

        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))

        self.actionSave_file_as.setText(QCoreApplication.translate("MainWindow", u"Save file as...", None))

        self.actionOpen_file.setText(QCoreApplication.translate("MainWindow", u"Open file...", None))

        self.actionSave_file.setText(QCoreApplication.translate("MainWindow", u"Save file...", None))

        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"New...", None))

        self.toolButtonSub.setText(QCoreApplication.translate("MainWindow", u"-10", None))

        self.toolButtonSubOne.setText(QCoreApplication.translate("MainWindow", u"-1", None))

        self.toolButtonAddOne.setText(QCoreApplication.translate("MainWindow", u"+1", None))

        self.toolButtonAdd.setText(QCoreApplication.translate("MainWindow", u"+10", None))

        self.label1.setText("")

        self.label2.setText("")

        self.label3.setText("")

        self.label4.setText("")

        self.label5.setText("")

        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Effects", None))

        self.pushButtonVideo.setText(QCoreApplication.translate("MainWindow", u"Apply to a whole video", None))

        self.pushButtonFrame.setText(QCoreApplication.translate("MainWindow", u"Apply to a frame", None))

        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))

        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))

        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))

        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))

        self.checkBox_5.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))

        self.checkBox_6.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))

        self.photoWithEffects.setText("")

        self.photoWoEffects.setText("")

        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))

        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))

        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))

        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))

    # retranslateUi



