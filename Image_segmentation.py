# -*- coding: utf-8 -*-
"""
Created on Thu Jul  3 12:08:47 2025

@author: Ayobami Adeyemo
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt
 
img = cv2.imread("C:/Users/Ayobami Adeyemo/OneDrive/Documents/Udacity Class/Images/download.jpg")
assert img is not None, "file could not be read, check with os.path.exists()"
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
cv2.imshow("Image", thresh)
cv2.imshow("O_Image", img)