from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow

class ButtonHolder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Button holder app")
        self.button = QPushButton("Press Me!")
        self.button.setCheckable(True)
        self.setCentralWidget(self.button)