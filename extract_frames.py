import os 
import numpy as np
import cv2
from PySide6.QtGui import QPixmap, QImage

from glob import glob

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


def extract(video_path):
    save_dir = f'vid'

    name = video_path.split("/")[-1].split(".")[0]
    save_path = os.path.join(save_dir, name)
    create_dir(save_path)

    cap = cv2.VideoCapture(video_path)
    idx = 0
    fps = cap.get(cv2.CAP_PROP_FPS)
    print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))
    frames = []

    while True:
        ret, frame = cap.read()
        
        if ret == False:
            cap.release()
            break
        frames.append(frame)
        idx += 1
    idx -= 1
    
    return frames, save_path, idx, fps
