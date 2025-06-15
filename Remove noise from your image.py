# -*- coding: utf-8 -*-
"""
Created on Sun Jun 15 20:44:09 2025

@author: Ayobami Adeyemo
"""

import cv2
import numpy as np

img = cv2.imread("C:/Users/Ayobami Adeyemo/Downloads/download.jpg")
im = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


#Add noise to the image
x, y = im.shape
mean = 0
sigma = 50
sd = np.sqrt(sigma)
noise = np.random.normal(loc=mean, scale=sd, size=(x,y)).astype(np.float32)

#convert image to float32 fpor safe addition
im_float = im.astype(np.float32)

#Add noise
noisy_image = im_float + noise

#clip to 0-255 and convert back to uint8
noisy_image_clipped = np.clip(noisy_image, 0, 255).astype(np.uint8)

# Now apply a Gaussian filter to smooth out the noise
img_ = cv2.GaussianBlur(noisy_image_clipped, (5,5), 2)


# Note: You may need to pkg load image;
cv2.imshow("noise", noise)
cv2.imshow("image", img_)
cv2.imshow("Original Image", im)
#cv2.imshow("Gaussian Filter", noisy_image)