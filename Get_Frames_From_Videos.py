# -*- coding: utf-8 -*-
"""
Created on Fri Jul 25 05:11:20 2025

@author: Ayobami Adeyemo
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

#Get input and output folders
input_video = "C:/Users/Ayobami Adeyemo/Downloads/artuvia/output_folder/Video_frames1/foreground/foreground_only.mp4"
output_folder = "C:/Users/Ayobami Adeyemo/Downloads/artuvia/output_folder/Video_frames1/vehicles_video_frame"


#Read Video File
cap = cv2.VideoCapture(input_video)
os.makedirs(output_folder, exist_ok=True)

if cap.isOpened() == False:
    print("Could not open video file")
    
#Get video information
fps = int(cap.get(cv2.CAP_PROP_FPS))
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))


print(frame_count)
print(fps)

frame_index = 0
timestamps = []

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    cv2.imwrite(os.path.join(output_folder, "{:04d}.jpg".format(frame_index)), frame)
    
    frame_index += 1 

cap.release()
    

