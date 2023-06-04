from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,

    QMetaObject, QObject, QPoint, QRect,

    QSize, QTime, QUrl, Qt, QFile)

from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,

    QCursor, QFont, QFontDatabase, QGradient,

    QIcon, QImage, QKeySequence, QLinearGradient,

    QPainter, QPalette, QPixmap, QRadialGradient,

    QTransform)

from PySide6.QtWidgets import (QApplication, QCheckBox, QGroupBox, QLabel,

    QMainWindow, QMenu, QMenuBar, QPushButton,

    QSizePolicy, QSlider, QStatusBar, QToolButton,

    QVBoxLayout, QWidget, QSplashScreen)

from PySide6.QtUiTools import QUiLoader

from clickableLabel import ClickableLabel



class Ui_MainWindow(object):

    def setupUi(self, MainWindow):

        if not MainWindow.objectName():

            MainWindow.setObjectName(u"MainWindow")

        MainWindow.setFixedSize(1440, 920)
        MainWindow.setStyleSheet("background-color:#18122B;color: white;font-family:Consolas")
        
        self.actionSave_file_as = QAction(MainWindow)

        self.actionSave_file_as.setObjectName(u"actionSave_file_as")

        self.actionOpen_file = QAction(MainWindow)

        self.actionOpen_file.setObjectName(u"actionOpen_file")

        self.actionSave_file = QAction(MainWindow)

        self.actionSave_file.setObjectName(u"actionSave_file")

        self.actionNew = QAction(MainWindow)

        self.actionNew.setObjectName(u"actionNew")

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: #393053;color: white;")
        self.centralwidget.setObjectName(u"centralwidget;color: white;")
        self.centralwidget.setGeometry(QRect(0, 22, 1440, 900))
        
        self.infoWidget = QGroupBox(self.centralwidget)
        self.infoWidget.setObjectName(u"infowidget")
        
        self.infoWidget.setGeometry(QRect(40, 730, 1350, 130))
        self.infoWidget.setStyleSheet("#infowidget {border:4px solid #635985;border-radius:10px;font-size:15px}")


        self.vid_time_total = QLabel(self.infoWidget)
        self.vid_time_total.setObjectName(u"vid_time_total")
        self.vid_time_total.setGeometry(QRect(20, 30, 151, 20))

        self.vid_time = QLabel(self.infoWidget)
        self.vid_time.setObjectName(u"vid_time")
        self.vid_time.setGeometry(QRect(20, 50, 151, 20))
        self.vid_time.setScaledContents(True)

        self.video_current_frame = QLabel(self.infoWidget)
        self.video_current_frame.setObjectName(u"vid_current_frame")
        self.video_current_frame.setGeometry(QRect(20, 70, 151, 20))

        self.video_frame_rate = QLabel(self.infoWidget)
        self.video_frame_rate.setObjectName(u"video_frame_rate")
        self.video_frame_rate.setGeometry(QRect(20, 90, 151, 20))

        self.vid_width = QLabel(self.infoWidget)
        self.vid_width.setObjectName(u"vid_width")
        self.vid_width.setGeometry(QRect(220, 30, 151, 20))
        self.vid_width.setScaledContents(True)

        self.vid_height = QLabel(self.infoWidget)
        self.vid_height.setObjectName(u"vid_height")
        self.vid_height.setGeometry(QRect(220, 50, 151, 20))
        self.vid_height.setScaledContents(True)

        self.vid_codec_name = QLabel(self.infoWidget)
        self.vid_codec_name.setObjectName(u"codec_name")
        self.vid_codec_name.setGeometry(QRect(220, 70, 151, 20))
        self.vid_codec_name.setScaledContents(True)

        self.pix_format = QLabel(self.infoWidget)
        self.pix_format.setObjectName(u"pix_format")
        self.pix_format.setGeometry(QRect(220, 90, 151, 20))
        self.pix_format.setScaledContents(True)

        self.bit_rate = QLabel(self.infoWidget)
        self.bit_rate.setObjectName(u"bit_rate")
        self.bit_rate.setGeometry(QRect(420, 30, 151, 20))
        self.bit_rate.setScaledContents(True)

        self.color_space = QLabel(self.infoWidget)
        self.color_space.setObjectName(u"color_space")
        self.color_space.setGeometry(QRect(420, 50, 151, 20))
        self.color_space.setScaledContents(True)

        self.audio_codec_name = QLabel(self.infoWidget)
        self.audio_codec_name.setObjectName(u"codec_name")
        self.audio_codec_name.setGeometry(QRect(420, 70, 151, 20))
        self.audio_codec_name.setScaledContents(True)

        self.sample_rate = QLabel(self.infoWidget)
        self.sample_rate.setObjectName(u"sample_rate")
        self.sample_rate.setGeometry(QRect(420, 90, 151, 20))
        self.sample_rate.setScaledContents(True)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(40, 360, 1350, 345))
        self.widget.setStyleSheet("#widget {border:4px solid #635985;border-radius:10px}")
       
        self.widgetFrames = QWidget(self.widget)
        self.widgetFrames.setObjectName(u"widgetFrames")
        self.widgetFrames.setGeometry(QRect(10, 10, 1330, 330))
        
        self.toolButtonSub = QToolButton(self.widgetFrames)
        self.toolButtonSub.setObjectName(u"toolButtonSub")
        self.toolButtonSub.setStyleSheet("background-color: #443C68")
        self.toolButtonSub.setGeometry(QRect(0, 20, 75, 180))
        
        self.toolButtonSubOne = QToolButton(self.widgetFrames)
        self.toolButtonSubOne.setObjectName(u"toolButtonSubOne")
        self.toolButtonSubOne.setStyleSheet("background-color: #443C68")
        self.toolButtonSubOne.setGeometry(QRect(75, 20, 75, 180))

        self.toolButtonAddOne = QToolButton(self.widgetFrames)
        self.toolButtonAddOne.setObjectName(u"toolButtonAddOne")
        self.toolButtonAddOne.setStyleSheet("background-color: #443C68")
        self.toolButtonAddOne.setGeometry(QRect(1180, 20, 75, 180))

        self.toolButtonAdd = QToolButton(self.widgetFrames)
        self.toolButtonAdd.setObjectName(u"toolButtonAdd")
        self.toolButtonAdd.setStyleSheet("background-color: #443C68")
        self.toolButtonAdd.setGeometry(QRect(1255, 20, 75, 180))

        self.label1 = ClickableLabel(self.widgetFrames)

        self.label1.setObjectName(u"label1")

        self.label1.setGeometry(QRect(150, 20, 205, 180))

        self.label1.setScaledContents(True)

        self.label2 = ClickableLabel(self.widgetFrames)

        self.label2.setObjectName(u"label2")

        self.label2.setGeometry(QRect(356, 20, 205, 180))

        self.label2.setScaledContents(True)

        self.label3 = ClickableLabel(self.widgetFrames)

        self.label3.setObjectName(u"label3")

        self.label3.setGeometry(QRect(562, 20, 205, 180))

        self.label3.setScaledContents(True)

        self.label4 = ClickableLabel(self.widgetFrames)

        self.label4.setObjectName(u"label4")

        self.label4.setGeometry(QRect(768, 20, 205, 180))

        self.label4.setScaledContents(True)

        self.label5 = ClickableLabel(self.widgetFrames)

        self.label5.setObjectName(u"label5")

        self.label5.setGeometry(QRect(974, 20, 205, 180))

        self.label5.setScaledContents(True)


        self.horizontalSlider = QSlider(self.widget)

        self.horizontalSlider.setObjectName(u"horizontalSlider")

        self.horizontalSlider.setGeometry(QRect(120, 245, 1115, 75))

        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.widgetEffectsAndFrame = QWidget(self.centralwidget)

        self.widgetEffectsAndFrame.setObjectName(u"widgetEffectsAndFrame")

        self.widgetEffectsAndFrame.setGeometry(QRect(10, 0, 1440, 360))
        self.groupBox = QGroupBox(self.widgetEffectsAndFrame)
        
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setStyleSheet("#groupBox {margin:0px; border:4px solid #635985;border-radius:10px;font-size:15px}")
        self.groupBox.setGeometry(QRect(0, 10, 210, 330))

        self.pushButtonVideo = QPushButton(self.groupBox)

        self.pushButtonVideo.setObjectName(u"pushButtonVideo")
        self.pushButtonVideo.setStyleSheet("background-color: #443C68")
        self.pushButtonVideo.setGeometry(QRect(40, 190, 131, 25))

        self.pushButtonFrame = QPushButton(self.groupBox)

        self.pushButtonFrame.setObjectName(u"pushButtonFrame")
        self.pushButtonFrame.setStyleSheet("background-color: #443C68")
        self.pushButtonFrame.setGeometry(QRect(40, 220, 131, 25))

        self.pushButtonFrom = QPushButton(self.groupBox)

        self.pushButtonFrom.setObjectName(u"pushButtonFrom")
        self.pushButtonFrom.setStyleSheet("background-color: #443C68")
        self.pushButtonFrom.setGeometry(QRect(20, 250, 80, 25))

        self.pushButtonTo = QPushButton(self.groupBox)

        self.pushButtonTo.setObjectName(u"pushButtonTo")
        self.pushButtonTo.setStyleSheet("background-color: #443C68")
        self.pushButtonTo.setGeometry(QRect(110, 250, 80, 25))

        self.pushButtonFrames = QPushButton(self.groupBox)

        self.pushButtonFrames.setObjectName(u"pushButtonFrames")
        self.pushButtonFrames.setStyleSheet("background-color: #443C68")
        self.pushButtonFrames.setGeometry(QRect(40, 280, 131, 25))

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
        self.photoWithEffects.setStyleSheet("margin:5px; border:4px solid #635985;border-radius:5px")
        self.photoWithEffects.setAlignment(Qt.AlignCenter)
        self.photoWithEffects.setGeometry(QRect(240, 7, 580, 340))

        self.photoWithEffects.setScaledContents(True)

        self.photoWoEffects = QLabel(self.widgetEffectsAndFrame)

        self.photoWoEffects.setObjectName(u"photoWoEffects")
        self.photoWoEffects.setStyleSheet("margin:5px; border:4px solid #635985;border-radius:5px")
        self.photoWoEffects.setAlignment(Qt.AlignCenter)
        self.photoWoEffects.setGeometry(QRect(840, 7, 580, 340))

        self.photoWoEffects.setScaledContents(True)

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QMenuBar(MainWindow)

        self.menubar.setObjectName(u"menubar")

        self.menubar.setGeometry(QRect(0, 0, 1440, 22))

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

        self.pushButtonVideo.setText(QCoreApplication.translate("MainWindow", u"Apply to video", None))

        self.pushButtonFrame.setText(QCoreApplication.translate("MainWindow", u"Apply to frame", None))

        self.pushButtonFrom.setText(QCoreApplication.translate("MainWindow", u"From: ", None))

        self.pushButtonTo.setText(QCoreApplication.translate("MainWindow", u"To: ", None))

        self.pushButtonFrames.setText(QCoreApplication.translate("MainWindow", u"Apply to frames", None))

        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))

        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))

        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))

        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))

        self.checkBox_5.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))

        self.checkBox_6.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.photoWithEffects.setText("Frame With effects")

        self.photoWoEffects.setText("Frame Original")

        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))

        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))

        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))

        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))

    # retranslateUi



