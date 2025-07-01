# -*- coding: utf-8 -*-
"""
Created on Mon Jun 30 14:42:15 2025

@author: Ayobami Adeyemo
"""

import cv2


video_path = ("C:/Users/Ayobami Adeyemo/Downloads/video_40_41.mp4")

cap = cv2.VideoCapture(video_path)

if cap.isOpened():
    
    fps = cap.get(cv2.CAP_PROP_FPS)
    
    frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    
    duration = frame_count / fps
    
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    
    print(f"FPS: {fps},\nDuration: {duration}s,\nResolution: {width}x{height},\nFRAME COUNT:{frame_count}")
    
else:
    
    print("Cannot open vide0")