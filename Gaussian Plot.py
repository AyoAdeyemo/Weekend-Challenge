# -*- coding: utf-8 -*-
"""
Created on Fri May 30 01:58:26 2025

@author: Ayobami Adeyemo
"""
import cv2
import numpy as np
from numpy import random
from scipy.stats.kde import gaussian_kde
import matplotlib.pyplot as plt


image = cv2.imread("C:/Users/Ayobami Adeyemo/Downloads/download.jpg", 0)
image = image/255
x, y = image.shape


mean = 0
var = 0.01
sigma = np.sqrt(var)
n1 = np.random.normal(loc=mean, scale=sigma, size=(x, y))

kde = gaussian_kde(n1.reshape(int(x*y)))
dist_space = np.linspace(np.min(n1), np.max(n1), 100)


plt.subplot(2, 2, 1)
plt.plot(dist_space, kde(dist_space))
plt.xlabel("Noise pixel value")
plt.ylabel("Frequency")
plt.show()

mean = 0
var = 0.1
sigma = np.sqrt(var)
n2 = np.random.normal(loc=mean, scale=sigma, size=(x, y))

kde = gaussian_kde(n2.reshape(int(x*y)))
dist_space = np.linspace(np.min(n2), np.max(n2), 100)


cv2.imshow("var=0.01", n1)
cv2.imshow("var=0.1", n2)
cv2.waitKey(10000)
cv2.destroyAllWindows()


plt.subplot(2, 2, 2)
plt.plot(dist_space, kde(dist_space))
plt.xlabel("Noise pixel value")
plt.ylabel("Frequency")
plt.show()