# -*- coding: utf-8 -*-
"""
Created on Sat Jun 14 13:24:22 2025

@author: Ayobami Adeyemo
"""

import cv2
import numpy as np


image = cv2.imread("C:/Users/Ayobami Adeyemo/Downloads/download.jpg")


Image_size = image.size
Image_type = image.dtype
if Image_type == "uint8":
    print("This image is decoded with the Unsigned Integer: {}".format(Image_type))
else:
    print("This image has some other decoded format: {}".format(Image_type))
    
Image_shape = image.shape
if len(Image_shape) == 3: 
    if Image_shape[2] == 3:
        print("This image has a 3-Color Layer: RGB")
        print("The image size {} implies that {} x {} is represented with {} vector-values each to give a total value size of {}".format(Image_size, Image_shape[0], Image_shape[1], Image_shape[2], Image_size))

        
elif len(Image_shape) == 2:
    print("The image has most likely a Grayscale Image")
    print("The image size {} implies that {} x {} is represented with one value each to give a total value size of {}".format(Image_size, Image_shape[0], Image_shape[1], Image_size))



print("See summary below")
print("Image_Type: {}".format(image.dtype))
print("Image_Shape: {}".format(image.shape))
print("Image_Size: {}".format(image.size))