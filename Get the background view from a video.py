# -*- coding: utf-8 -*-
"""
Created on Fri Jul 11 19:51:33 2025

@author: Ayobami Adeyemo
"""

import cv2
import numpy as np


video_path = "C:/Users/Ayobami Adeyemo/Downloads/Sample Video.mp4"
c = cv2.VideoCapture(video_path)
_,f = c.read()

avg1 = np.float32(f)
avg2 = np.float32(f)

while(1):
    _,f = c.read()
	
    cv2.accumulateWeighted(f,avg1,0.1)
    cv2.accumulateWeighted(f,avg2,0.01)
	
    res1 = cv2.convertScaleAbs(avg1)
    res2 = cv2.convertScaleAbs(avg2)

    cv2.imshow('img',f)
    cv2.imshow('avg1',res1)
    cv2.imshow('avg2',res2)
    k = cv2.waitKey(20)

    if k == 27:
        break

cv2.destroyAllWindows()
c.release()