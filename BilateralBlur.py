# -*- coding: utf-8 -*-
"""
Created on Sun Jun 15 19:55:55 2025

@author: Ayobami Adeyemo
"""

""" Bilateral Filtering
cv.bilateralFilter() is highly effective in noise removal while keeping edges sharp. But the operation is slower compared to other filters. We already saw that a Gaussian filter takes the neighbourhood around the pixel and finds its Gaussian weighted average. This Gaussian filter is a function of space alone, that is, nearby pixels are considered while filtering. It doesn't consider whether pixels have almost the same intensity. It doesn't consider whether a pixel is an edge pixel or not. So it blurs the edges also, which we don't want to do.

Bilateral filtering also takes a Gaussian filter in space, but one more Gaussian filter which is a function of pixel difference. The Gaussian function of space makes sure that only nearby pixels are considered for blurring, while the Gaussian function of intensity difference makes sure that only those pixels with similar intensities to the central pixel are considered for blurring. So it preserves the edges since pixels at edges will have large intensity variation.

The below sample shows use of a bilateral filter (For details on arguments, visit docs). """


import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("C:/Users/Ayobami Adeyemo/Downloads/download.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
assert image is not None, "file could not be read, check with os.path.exists()"

blur = cv2.bilateralFilter(image, 9, 75, 75)

plt.subplot(121), plt.imshow(image), plt.title("Original")
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(blur), plt.title("blur")
plt.xticks([]), plt.yticks([])
plt.show()

