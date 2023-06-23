from numba import cuda
from numba.cuda import jit
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
from mainwindow import MainWindow
import sys
from LoadingWindow import Ui_LoadingWindow



app = QApplication(sys.argv)

window = MainWindow(app)
#window2 = Ui_LoadingWindow()
window.show()
#window2.show()
app.exec()
