from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QToolBar, QMessageBox, QFileDialog, QCheckBox, QSizePolicy
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QPixmap, QImage
from ui_MainWindow import Ui_MainWindow
from extract_frames import extract
from effect import Effect
from custom_thread import CustomThread
import cv2
import copy

import numpy as np
from LoadingWindow import Ui_LoadingWindow
import os
import ffmpeg
from PySide6.QtCore import (QCoreApplication)

from PySide6.QtGui import (QPixmap)

from PySide6.QtWidgets import (QMainWindow)
NO_THREADS = 1
FPS_SAVE = 25
block_size = (8, 8, 8)




class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, app):
        super().__init__()
        self.setupUi(self)
        self.app = app
        self.setWindowTitle("Custom MainWindow")
        self.effects = Effect()
        # self.mainwindow.resize(1600, 900)
        self.changedFrame = 0
        self.mainFrame = 0
        self.currentMainNumber = -1
        self.applyFromFrame = 0
        self.applyToFrame = 0
        self.framesNumber = 0
        self.previousFramesNumber = 0
        self.baseFramesNumber = 0
        self.frames = []
        self.qImages = []
        self.changedFrames = []
        self.previousFrames = []  #to revert changes
        self.slider_frames = [self.label1, self.label2, self.label3, self.label4, self.label5]
        self.check_boxes = [self.checkBox, self.checkBox_2, self.checkBox_3, self.checkBox_4, self.checkBox_5, self.checkBox_6]
        self.firstFrame = 0
        self.actionSave_file_as.triggered.connect(self.save_video_as)
        self.actionOpen_file.triggered.connect(self.open_file)
        self.photoWoEffects.setScaledContents(True)
        self.framesDir = ""
        self.fps = 30
        self.widget1.setFixedWidth(180)
        
        #choose filter widget
        for check_box in self.check_boxes:
            check_box.stateChanged.connect(self.check_if_boxes_checked)

        self.check_boxes[0].setText("grayscale")
        self.check_boxes[1].setText("Gaussian Blur")
        self.check_boxes[2].setText("Edge detection")
        self.check_boxes[3].setText("sepia")
        self.check_boxes[4].setText("vignette")
        self.check_boxes[5].setText("brightness")
        self.pushButtonVideo.clicked.connect(self.apply_effects_to_video)
        self.pushButtonFrame.clicked.connect(self.apply_effects_to_frame)
        self.pushButtonFrom.clicked.connect(self.select_from_frame)
        self.pushButtonTo.clicked.connect(self.select_To_frame)
        self.pushButtonFrames.clicked.connect(self.apply_effects_to_part)
        self.pushButtonCut.clicked.connect(self.cut_frames)
        self.pushButtonRevert.clicked.connect(self.revert_changes)
        #frame choice widget 
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
    def save_video_as(self):
        fname = QFileDialog.getSaveFileName(self, "Save file", "","MP4 Files (*.mp4);;AVI Files (*.avi);;MOV Files (*.mov)")
        height, width = self.changedFrames[0].shape[0],self.changedFrames[0].shape[1]
        frame_size = (int(width), int(height))
        if(self.changedFrames[0].ndim == 2): 
            output = cv2.VideoWriter(fname[0], cv2.VideoWriter_fourcc(*'mp4v'), FPS_SAVE, frame_size,isColor=False)
        else:
            output = cv2.VideoWriter(fname[0], cv2.VideoWriter_fourcc(*'mp4v'), FPS_SAVE, frame_size)
    
        for frame in self.changedFrames:
            output.write(frame)
        
        output.release()

    
    def select_from_frame(self):
        self.applyFromFrame = self.currentMainNumber
        self.pushButtonFrom.setText(QCoreApplication.translate("MainWindow", u"From: {}".format(self.applyFromFrame+1), None))

    
    def select_To_frame(self):
        self.applyToFrame = self.currentMainNumber
        self.pushButtonTo.setText(QCoreApplication.translate("MainWindow", u"To: {}".format(self.applyToFrame+1), None))
        
        
    def apply_effects_to_part(self):
        self.previousFrames = copy.deepcopy(self.changedFrames)
        if self.applyFromFrame > self.applyToFrame:
            (self.applyFromFrame, self.applyToFrame) = ( self.applyToFrame, self.applyFromFrame)
            self.pushButtonTo.setText(QCoreApplication.translate("MainWindow", u"To: {}".format(self.applyToFrame+1), None))
            self.pushButtonFrom.setText(QCoreApplication.translate("MainWindow", u"From: {}".format(self.applyFromFrame+1), None))
        if self.check_boxes[0].isChecked():
            self.effects.grayscale(self.changedFrames[self.applyFromFrame:self.applyToFrame+1])
        if self.check_boxes[1].isChecked():
            self.effects.gaussian_blur(self.changedFrames[self.applyFromFrame:self.applyToFrame+1])
        if self.check_boxes[2].isChecked():
            self.effects.edge_detection(self.changedFrames[self.applyFromFrame:self.applyToFrame+1])
        if self.check_boxes[3].isChecked():
            self.effects.sepia(self.changedFrames[self.applyFromFrame:self.applyToFrame+1])
        if self.check_boxes[4].isChecked():
            self.effects.vignette(self.changedFrames[self.applyFromFrame:self.applyToFrame+1])
        if self.check_boxes[5].isChecked():
            self.effects.brightness(self.changedFrames[self.applyFromFrame:self.applyToFrame+1])
        self.update_qImages()
        self.show_frames()

    def apply_effects_to_video(self):
        self.previousFrames = copy.deepcopy(self.changedFrames)
        if self.check_boxes[0].isChecked():
            self.effects.grayscale(self.changedFrames)
        if self.check_boxes[1].isChecked():
            self.effects.gaussian_blur(self.changedFrames)
        if self.check_boxes[2].isChecked():
            self.effects.edge_detection(self.changedFrames)
        if self.check_boxes[3].isChecked():
            self.effects.sepia(self.changedFrames)
        if self.check_boxes[4].isChecked():
            self.effects.vignette(self.changedFrames)
        if self.check_boxes[5].isChecked():
            self.effects.brightness(self.changedFrames)
        self.update_qImages()
        self.show_frames()

        
    def apply_effects_to_frame(self):
        self.previousFrames = copy.deepcopy(self.changedFrames)
        self.changedFrames[self.firstFrame+2] = self.changedFrame
        self.update_qImages()
        self.show_frames()
    def check_if_boxes_checked(self):   #check if check boxes are checked, if so call appropriate function
        self.changedFrame  = self.mainFrame
        grid_size = ((self.frames.shape[0] - 1) // block_size[0] + 1, (self.frames.shape[1] - 1) // block_size[1] + 1, (self.frames.shape[2] - 1) // block_size[2] + 1)
        if self.check_boxes[0].isChecked():
            self.changedFrame = self.effects.grayscale_preview(self.changedFrame, grid_size)[0]
            self.change_affected_frame(self.changedFrame)
        if self.check_boxes[1].isChecked():
            self.changedFrame = self.effects.gaussian_blur_preview(self.changedFrame,grid_size)[0]
            self.change_affected_frame(self.changedFrame)
        if self.check_boxes[2].isChecked():
            self.changedFrame = self.effects.edge_detection_preview(self.changedFrame,grid_size)[0]
            self.change_affected_frame(self.changedFrame)
        if self.check_boxes[3].isChecked():
            self.changedFrame = self.effects.sepia_preview(self.changedFrame,grid_size)[0]
            self.change_affected_frame(self.changedFrame)
        if self.check_boxes[4].isChecked():
            self.changedFrame = self.effects.vignette_preview(self.changedFrame,grid_size)[0]
            self.change_affected_frame(self.changedFrame)
        if self.check_boxes[5].isChecked():
            self.changedFrame = self.effects.brightness_preview(self.changedFrame,grid_size)[0]
            self.change_affected_frame(self.changedFrame)

    def change_affected_frame(self, frame):
        self.photoWithEffects.setPixmap(QPixmap(self.convert_to_qimage(frame)))
    def change_main_frame(self, number):
        self.currentMainNumber = self.firstFrame + number -1

        self.mainFrame = self.changedFrames[self.currentMainNumber]

        self.photoWoEffects.setPixmap(QPixmap(self.convert_to_qimage(self.mainFrame)))
        self.check_if_boxes_checked()
        if number != 3:
            self.change_frames(number-3)    
    
    def convert_to_qimage(self, frame):
        height, width = frame.shape[0],frame.shape[1]
        bytesPerLine = 3 * width
        
        return QImage(frame.data, width, height, bytesPerLine, QImage.Format_BGR888)
    
    def set_video_info(self,fname):
        image_data = ffmpeg.probe(fname)["streams"]  
        self.infoWidget.setTitle(QCoreApplication.translate("MainWindow", "Details: "+os.path.basename(fname),None))
        self.vid_time_total.setText("video length: " + str(int(float(image_data[0]['duration'])))+str(" s"))
        self.video_current_frame.setText("total frames:"+ str(self.framesNumber))
        self.video_frame_rate.setText("frame rate: "+str(self.fps)+"/s")
        self.vid_height.setText("frame width: "+ str(self.frames[0].shape[0])+" px" )
        self.vid_width.setText("frame width: "+ str(self.frames[0].shape[1])+" px" )
        self.vid_codec_name.setText("video codec: "+ image_data[0]['codec_name'])
        self.pix_format.setText("pixel format: "+image_data[0]['pix_fmt'])
        self.bit_rate.setText("video bit rate: "+image_data[0]['bit_rate'])
        #self.color_space.setText("color space: " + image_data[0]['color_space']) not working for avi and mov files
        if(len(image_data)>1):
            self.audio_codec_name.setText("audio codec: " + image_data[1]['codec_name'])
            self.sample_rate.setText("audio freq: " + image_data[1]['sample_rate'] +"hz")
    def open_file(self):
        # Open file dialog
        
        fname = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*);;MP4 Files (*.mp4);;MOV Files (*.mov);;AVI Files (*.avi)")
        if fname:
            self.frames, self.framesDir, self.framesNumber,self.fps = extract(fname[0])
            self.baseFramesNumber = self.framesNumber
            self.previousFramesNumber = self.framesNumber
            self.pushButtonFrom.setText(QCoreApplication.translate("MainWindow", u"From: 1", None))
            self.pushButtonTo.setText(QCoreApplication.translate("MainWindow", u"To: {} ".format(self.framesNumber), None))
            minute = int((self.framesNumber/self.fps) / 60)
            second = int(self.framesNumber/self.fps) % 60
            self.changedFrames = copy.deepcopy(self.frames)
            self.previousFrames = copy.deepcopy(self.frames)
            self.update_qImages()
            self.set_video_info(fname[0])
            self.mainFrame = self.frames[2]
            self.horizontalSlider.setMinimum(0)
            self.horizontalSlider.setMaximum(self.framesNumber)
            self.horizontalSlider.setValue(0)
            self.photoWoEffects.setPixmap(QPixmap(self.convert_to_qimage(self.mainFrame)))
            self.show_frames()

        else:
            return


    def cut_frames(self):
        self.previousFrames = copy.deepcopy(self.changedFrames)
        self.previousFramesNumber = self.framesNumber
        if self.applyFromFrame > self.applyToFrame:
            (self.applyFromFrame, self.applyToFrame) = ( self.applyToFrame, self.applyFromFrame)
            self.pushButtonTo.setText(QCoreApplication.translate("MainWindow", u"To: {}".format(self.applyToFrame+1), None))
            self.pushButtonFrom.setText(QCoreApplication.translate("MainWindow", u"From: {}".format(self.applyFromFrame+1), None))
        self.changedFrames[self.applyFromFrame:] = self.changedFrames[self.applyToFrame+1:]
        self.framesNumber = self.framesNumber - (self.applyToFrame - self.applyFromFrame)
        self.video_current_frame.setText("total frames:"+ str(self.framesNumber))
        self.horizontalSlider.setMaximum(self.framesNumber)
        self.horizontalSlider.setValue(self.applyFromFrame)
        self.applyToFrame = self.applyFromFrame
        self.pushButtonTo.setText(QCoreApplication.translate("MainWindow", u"To: {}".format(self.applyToFrame+1), None))
        self.update_qImages()
        self.show_frames()

    def revert_changes(self):
        self.changedFrames = copy.deepcopy(self.previousFrames)
        self.previousFrames = copy.deepcopy(self.frames)
        self.framesNumber = self.previousFramesNumber
        self.video_current_frame.setText("total frames:"+ str(self.framesNumber))
        self.horizontalSlider.setMaximum(self.framesNumber)
        self.previousFramesNumber = self.baseFramesNumber
        self.update_qImages()
        self.show_frames() 


    def slider_moved(self, place):
        self.firstFrame = min(place, self.framesNumber-5)
        self.show_frames()

    def show_frames(self):
        minute = int((self.firstFrame/self.fps) / 60)
        second = int(self.firstFrame/self.fps) % 60
        self.video_current_frame.setText("current frame: "+ str(self.firstFrame+3))
        if(self.framesNumber != 0):
            self.vid_time.setText("currenttly at: "+str(minute)+":"+str(second))
        for idx, f in enumerate(self.slider_frames):
            f.setPixmap(QPixmap(self.qImages[self.firstFrame + idx]))  #f"{self.framesDir}/{self.firstFrame + idx}"



    def change_frames(self, number):
        temp = self.firstFrame
        temp += number
        temp = max(min(temp, self.framesNumber-5), 0)
        if temp != self.firstFrame:
            self.firstFrame = temp
            self.horizontalSlider.setValue(self.firstFrame)
            self.show_frames()


    def update_qImages(self):   #updating images to show in the application to the ones with effects
        self.qImages.clear()
        for frame in self.changedFrames:
            self.qImages.append(self.convert_to_qimage(frame))
        #self.firstFrame = 0
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
