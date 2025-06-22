# -*- coding: utf-8 -*-
"""
Created on Sun Jun 22 23:03:43 2025

@author: Ayobami Adeyemo
"""

import cv2
import matplotlib.pyplot as plt
im = cv2.imread("C:/Users/Ayobami Adeyemo/Downloads/download.jpg");

img = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
red_im  = im[:, :, 1]
print (red_im.shape) #to read the shape of an image [width, height, channels/layers]
print(im.shape)
print (im.size)  #to read the size of an image this gives the area of an image [width x breadth]
print (im.dtype) #to read the image type
px = im[25, 26]  #to read the size at this specific location in the pixel [row, col, layer] here using ":" in the position of row or column or both,
#implies that I want to read the pixel value throughout the rows or columns or both and specify the layer implies that one want to read the Intensity of either the Red, Green, Blue 
#intensity in the image.
print (px)
cv2.imshow("red_image", red_im)
cv2.waitKey(100000)
cv2.destroyAllWindows()
plt.plot(px, "r")
plt.title("Intensity of Pixel in BGR")
plt.xlabel("Color Index")
plt.ylabel("Pixel Intensity")
plt.grid(True)
plt.show()
