from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QToolBar, QMessageBox, QFileDialog
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QPixmap, QImage
from ui_MainWindow import Ui_MainWindow
from extract_frames import extract

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, app):
        super().__init__()
        self.setupUi(self)
        self.app = app
        self.setWindowTitle("Custom MainWindow")
        #self.mainwindow.resize(1600, 900)


        self.frames = []
        self.slider_frames = [self.label1, self.label2, self.label3, self.label4, self.label5]

        self.actionOpen_file.triggered.connect(self.open_file)
        self.photoWoEffects.setPixmap(QPixmap("kot.jpg"))
        self.photoWoEffects.setScaledContents(True)
        
        #menubar and menus
        """
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("&File")
        quit_action = file_menu.addAction("Quit")
        quit_action.triggered.connect(self.quit_app)

        edit_menu = menu_bar.addMenu("&Edit")
        edit_menu.addAction("Copy")
        edit_menu.addAction("Cut")
        edit_menu.addAction("Paste")
        edit_menu.addAction("Undo")
        edit_menu.addAction("Redo")

        edit_menu = menu_bar.addMenu("Window")
        edit_menu = menu_bar.addMenu("Settings")
        edit_menu = menu_bar.addMenu("Help")

        button1 = QPushButton("BUTTON1")
        button1.clicked.connect(self.button1_clicked)
    

        #toolbar
        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16,16))
        self.addToolBar(toolbar)

        toolbar.addWidget(button1)
        """


    def open_file(self):
        #Open file dialog
        fname = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*);;MP4 Files (*.mp4)")

        if fname:
            self.frames, save_dir = extract(fname[0])
            #self.update_new_video(fname[0])
            self.photoWithEffects.setPixmap(QPixmap(f"{save_dir}/0.png"))
        else: 
            return
        
    
    def update_new_video(self, filename):
        with open(filename) as f:
            self.frames = [frame for frame in f]
            for i in range(5):
                print(self.frames[i])
            """
            for idx, _ in enumerate(self.slider_frames):
                self.slider_frames[idx].setPixmap(QPixmap(self.frames[idx]))
            """




    def button1_clicked(self):
        #could also be .information , .warning, .about
        ret = QMessageBox.critical(self, "Message title", "Critical Message!", QMessageBox.Ok | QMessageBox.Cancel)

        if ret == QMessageBox.Ok:
            print("User chose ok")     
        else:
            print("User chose Cancel")


    def quit_app(self):
        self.app.quit()