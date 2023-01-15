from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
from mainwindow import MainWindow
import sys


def button_clicked(data):
    print("You clicked a button: ", data)


app = QApplication(sys.argv)

window = MainWindow(app)

window.show()
 
app.exec()