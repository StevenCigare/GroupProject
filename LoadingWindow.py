from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, QIODevice, QByteArray)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QProgressBar, QSizePolicy,
    QWidget, QVBoxLayout)
import sys
import time
from threading import Thread

counter = 12

def update_counter():
    global counter

    info = 0
    while not QByteArray.isEmpty(info):
        print(counter)
        data = sys.stdout.readline()
        sys.stdout.flush()
        
        #info = QIODevice.read()
        counter = int(data)
        #sys.stdout.write(f'wszystko git tutaj!\n')
        #QIODevice.write(QByteArray('jes git'))
    

class Ui_LoadingWindow(QWidget):
    def __init__(self, app):
        super().__init__()
        self.resize(400, 300)
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
        
        thread = Thread(target=self.load_frames, args=())
        thread.start()
        #thread.join()

    def retranslateUi(self, LoadingWindow):
        LoadingWindow.setWindowTitle(QCoreApplication.translate("LoadingWindow", u"Form", None))
        self.label.setText(QCoreApplication.translate("LoadingWindow", u"Loading...", None))
    # retranslateUi

    def load_frames(self):     
        global counter
        i = 0
        
        no_frames = int(sys.argv[1])
        #print(no_frames)
        #t1 = Thread(target=update_counter, args=())
        #print(no_frames)
        while i != no_frames:
            self.progressBar.setValue(i)
            #print(i)
            time.sleep(0.05)
            #self.repaint()
            #print(counter)
            #print(idx)
            i+=1

        #t1.join()
        print(counter)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Ui_LoadingWindow(app)
    #window2 = Ui_LoadingWindow()
    window.show()
    #window2.show()
    app.exec()

