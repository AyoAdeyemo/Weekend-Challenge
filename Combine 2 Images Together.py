# -*- coding: utf-8 -*-
"""
Created on Wed Jun 25 23:37:48 2025

@author: Ayobami Adeyemo
"""

#Add 2 Images Demo
import cv2
import matplotlib.pyplot as plt

image_1 = cv2.imread("C:/Users/Ayobami Adeyemo/Downloads/download.jpg")
im_1 = cv2.cvtColor((image_1), cv2.COLOR_BGR2GRAY)
print (im_1.shape)

image2 = cv2.imread("C:/Users/Ayobami Adeyemo/Downloads/artuvia/output_folder/video_frames1/1260.jpg")
im = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
im_2 = im[0:183, 0:275]
print (im_2.shape)

pix1 = im_1/2 
pix2 = im_2/2
image = cv2.add(im_1, im_2)
new_image = cv2.addWeighted(im_1, 0.5, im_2, 0.5, 0)
#cv2.imshow("Add_image", image)
cv2.imshow("Add_image", new_image)
cv2.waitKey(100000)
cv2.destroyAllWindows()
