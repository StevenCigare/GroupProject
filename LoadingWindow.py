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
from multiprocessing import shared_memory
from PySide6.QtCore import (QProcess)
from shared_mem import MemoryManager
import array

def create_loading_window(no_frames):
    p = QProcess()
    p.start("python", ['LoadingWindow.py', f'{int(no_frames)}'])

    return p

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
        i = 0
        current_frame = 0
        prev = 0
        no_frames = int(sys.argv[1])
        manager = MemoryManager(name='mymemory')
        while i < 100:
            time.sleep(0.2)
            self.progressBar.setValue(i)
            try:
                current_frame = manager.get()
                if current_frame == prev:
                    raise Exception

                prev = current_frame
                i=int(100*current_frame/no_frames)
            except:
                i+=5
        
        manager.block.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Ui_LoadingWindow(app)
    #window2 = Ui_LoadingWindow()
    window.show()
    #window2.show()
    app.exec()

