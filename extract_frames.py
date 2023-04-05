import os 
import numpy as np
import cv2
import threading
import sys
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QProgressBar, QVBoxLayout

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, QProcess, QStringListModel,  QIODevice, QByteArray)

from glob import glob
import LoadingWindow
import time


idx = 0

def create_dir(path):
    try:
        if not os.path.exists(path):
            os.makedirs(path)
    except OSError:
        print(f"ERROR: creating directory with name {path}")

"""
def extract(video_path):
    save_dir = f'vid'
    print("elo")
    print("elo")
    print("elo")
    name = video_path.split("/")[-1].split(".")[0]
    save_path = os.path.join(save_dir, name)
    create_dir(save_path)

    cap = cv2.VideoCapture(video_path)
    # Enable CUDA acceleration
    cap.set(cv2.CAP_PROP_CONVERT_RGB, int(False))
    # Get the total number of frames
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frames = []
    # Iterate over all the frames
    for i in range(total_frames):
        # Grab the next frame
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)
        cv2.imshow("frame", frame)

    # Release the video capture object
    cap.release()


    return frames, save_path, total_frames
"""

def send_data(p, no_frames):
    global idx
    while idx != no_frames:
        #QIODevice.waitForReadyRead()
        QIODevice.write(p, QByteArray(f'{idx}'))
        #p.write(f'{idx}')
        #p.closeWriteChannel()
        #sys.stdout.write(f'{idx}\n')
        time.sleep(0.01)
        #data = sys.stdout.readline()
        #info = QIODevice.read(p)
        #print(info)
    #print(data)

def extract(video_path):
    save_dir = f'vid'

    name = video_path.split("/")[-1].split(".")[0]
    save_path = os.path.join(save_dir, name)
    create_dir(save_path)

    cap = cv2.VideoCapture(video_path)
    global idx
    no_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    fps = cap.get(cv2.CAP_PROP_FPS)
    print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))
    frames = []

    p = QProcess()
    p.start("python", ['LoadingWindow.py', f'{int(no_frames)}'])
  
    thread = threading.Thread(target=send_data, args=(p, no_frames))
    thread.start()
    while True:
        ret, frame = cap.read()
        
        if ret == False:
            cap.release()
            break
        frames.append(frame)
        idx += 1
    thread.join()
    idx -= 1
    
    return frames, save_path, idx, fps
