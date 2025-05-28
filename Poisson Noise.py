# -*- coding: utf-8 -*-
"""
Created on Wed May 28 23:09:50 2025

@author: Ayobami Adeyemo
"""

#Noisy image poisson 

import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.util import random_noise

image = cv2.imread("C:/Users/Ayobami Adeyemo/Downloads/download.jpg", 0)
image = image/255

#poisson
x, y = image.shape
mean = 0
var = 0.05
sd = np.sqrt(var)


p = np.random.normal(loc=mean, scale=sd, size= (x,y))

#Poisson Noisy Image
g = image + p

cv2.imshow("poisson_noised_image", g)
cv2.waitKey(10000)
cv2.destroyAllWindows()