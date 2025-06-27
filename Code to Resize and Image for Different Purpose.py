# -*- coding: utf-8 -*-
"""
Created on Fri Jun 27 22:08:40 2025

@author: Ayobami Adeyemo
"""


import cv2


input_image = cv2.imread("C:/Users/Ayobami Adeyemo/Downloads/Prova.jpg")

#Resizing an image

def resize_image(image):
    image_shape = image.shape
    image_grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    new_size = (140, 140)
    grayscale_shape = image_grayscale.shape
    if grayscale_shape != new_size:
        print("Need to resize image, please see resized")
        image_resize = cv2.resize(image, new_size)
    else:
        image_resize = image
    return image_resize

my_image = resize_image(input_image)


cv2.imshow("My resized image", my_image)