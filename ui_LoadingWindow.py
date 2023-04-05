from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QProgressBar, QSizePolicy,
    QWidget, QVBoxLayout)

counter = 0


class Ui_LoadingWindow(QWidget):
    def __init__(self, app):
        super().__init__()
        self.resize(1000, 800)
        self.app = app
        self.setObjectName(u"LoadingWindow")
        self.setWindowTitle("siemka")
        #self.setupUi()
        self.progressBar = QProgressBar(self)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(50, 240, 301, 23))
        self.progressBar.setValue(0)
        self.progressBar.setAlignment(Qt.AlignCenter)

        self.label = QLabel(self)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(120, 110, 171, 41))
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setAlignment(Qt.AlignCenter)
 

        self.retranslateUi(self)

        QMetaObject.connectSlotsByName(self)

    def setupUi(self, LoadingWindow):
        if not LoadingWindow.objectName():
            LoadingWindow.setObjectName(u"LoadingWindow")
        LoadingWindow.resize(400, 300)
        self.progressBar = QProgressBar(LoadingWindow)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(50, 240, 301, 23))
        self.progressBar.setValue(0)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.label = QLabel(LoadingWindow)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(120, 110, 171, 41))
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setAlignment(Qt.AlignCenter)

        self.retranslateUi(LoadingWindow)

        QMetaObject.connectSlotsByName(LoadingWindow)
    # setupUi

    def retranslateUi(self, LoadingWindow):
        LoadingWindow.setWindowTitle(QCoreApplication.translate("LoadingWindow", u"Form", None))
        self.label.setText(QCoreApplication.translate("LoadingWindow", u"Loading...", None))
    # retranslateUi

    def load_frames(no_frames, loading_window):     
        global counter

        print(no_frames)
        while counter != no_frames:
            loading_window.progressBar.setValue(100*counter//no_frames)
            loading_window.repaint()
            print(counter)
            #print(idx)
            
        print(counter)

