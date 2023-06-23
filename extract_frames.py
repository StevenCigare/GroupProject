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
from LoadingWindow import create_loading_window
from shared_mem import MemoryManager
from multiprocessing import shared_memory
import time


idx = 0

def create_dir(path):
    try:
        if not os.path.exists(path):
            os.makedirs(path)
    except OSError:
        print(f"ERROR: creating directory with name {path}")


def extract(video_path, frames):
    save_dir = f'vid'

    name = video_path.split("/")[-1].split(".")[0]
    save_path = os.path.join(save_dir, name)
    create_dir(save_path)

    cap = cv2.VideoCapture(video_path)
    global idx 
    idx = 0
    no_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    fps = cap.get(cv2.CAP_PROP_FPS)
    print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))
    manager = MemoryManager(name='mymemory', to_create=True)
    p = create_loading_window(no_frames=no_frames)
    
    while True:
        ret, frame = cap.read()
        
        if ret == False:
            cap.release()
            break
        
        frames.append(frame)
        #np.append(frames, frame)
        idx += 1
        manager.put(idx)
    
    manager.block.close()
    manager.block.unlink()
 
    #p.kill()
    idx -= 1
    
    return save_path, idx, fps
