from PySide6.QtWidgets import QPushButton, QWidget, QHBoxLayout, QVBoxLayout

class RockWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RockWidget")

        button1 = QPushButton("BUTTON1")
        button1.clicked.connect(self.button1_clicked)
        button2 = QPushButton("BUTTON2")
        button2.clicked.connect(self.button2_clicked)

        widget_layout = QVBoxLayout()
        widget_layout.addWidget(button1)
        widget_layout.addWidget(button2)
        self.setLayout(widget_layout)
    
    def button1_clicked(self):
        print("U clicked button 1")
    
    def button2_clicked(self):
        print("U clicked button 2")