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
        # self.mainwindow.resize(1600, 900)
        self.framesNumber = 0
        self.frames = []
        self.slider_frames = [self.label1, self.label2, self.label3, self.label4, self.label5]
        self.firstFrame = 0
        self.actionOpen_file.triggered.connect(self.open_file)
        self.photoWoEffects.setPixmap(QPixmap("kot.jpg"))
        self.photoWoEffects.setScaledContents(True)
        self.framesDir = ""


        self.toolButtonAddOne.released.connect(lambda: self.change_frames(1))
        self.toolButtonAdd.clicked.connect(lambda: self.change_frames(10))
        self.toolButtonSub.clicked.connect(lambda: self.change_frames(-10))
        self.toolButtonSubOne.clicked.connect(lambda: self.change_frames(-1))
        self.horizontalSlider.valueChanged.connect(self.slider_moved)
        self.label1.clicked.connect(lambda: self.change_main_frame(1))
        self.label2.clicked.connect(lambda: self.change_main_frame(2))
        self.label3.clicked.connect(lambda: self.change_main_frame(3))
        self.label4.clicked.connect(lambda: self.change_main_frame(4))
        self.label5.clicked.connect(lambda: self.change_main_frame(5))

        # menubar and menus
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


    def change_main_frame(self, number):
        self.photoWithEffects.setPixmap(QPixmap(f"{self.framesDir}/{self.firstFrame + number -1}.png"))
        if number != 3:
            self.change_frames(number-3)


    def open_file(self):
        # Open file dialog
        fname = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*);;MP4 Files (*.mp4)")

        if fname:
            self.frames, self.framesDir, self.framesNumber = extract(fname[0])
            # self.update_new_video(fname[0])
            self.horizontalSlider.setMinimum(0)
            self.horizontalSlider.setMaximum(self.framesNumber)
            self.horizontalSlider.setValue(0)
            self.photoWithEffects.setPixmap(QPixmap(f"{self.framesDir}/0.png"))
            for idx, f in enumerate(self.slider_frames):
                f.setPixmap(QPixmap(f"{self.framesDir}/{self.firstFrame + idx}"))
        else:
            return
        """
    def update_new_video(self, filename):
        with open(filename) as f:
            self.frames = [frame for frame in f]
            for i in range(5):
                print(self.frames[i])
            
            for idx, _ in enumerate(self.slider_frames):
                self.slider_frames[idx].setPixmap(QPixmap(self.frames[idx]))
        """

    def slider_moved(self, place):
        self.firstFrame = min(place, self.framesNumber-5)
        self.show_frames()

    def show_frames(self):
        for idx, f in enumerate(self.slider_frames):
            f.setPixmap(QPixmap(f"{self.framesDir}/{self.firstFrame + idx}"))

    def change_frames(self, number):
        temp = self.firstFrame
        temp += number
        temp = max(min(temp, self.framesNumber-5), 0)
        if temp != self.firstFrame:
            self.firstFrame = temp
            self.horizontalSlider.setValue(self.firstFrame)
            self.show_frames()

    def button1_clicked(self):
        # could also be .information , .warning, .about
        ret = QMessageBox.critical(self, "Message title", "Critical Message!", QMessageBox.Ok | QMessageBox.Cancel)

        if ret == QMessageBox.Ok:
            print("User chose ok")
        else:
            print("User chose Cancel")

    def quit_app(self):
        self.app.quit()
