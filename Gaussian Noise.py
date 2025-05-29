# -*- coding: utf-8 -*-
"""
Created on Thu May 29 23:57:41 2025

@author: Ayobami Adeyemo
"""

#Noise in Images
import cv2
import numpy as np
from scipy.stats.kde import gaussian_kde
import matplotlib.pyplot as plt 

#original image 
image = cv2.imread("C:/Users/Ayobami Adeyemo/Downloads/download.jpg", 0)
image = image/255

cv2.imshow("Original Imgae", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#create gaussian noise
x, y = image.shape
mean = 0
var = 0.01
sigma = np.sqrt(var) #gives the standard deviation which is mathematically the square root of variance
n = np.random.normal(loc=mean, scale = sigma, size=(x, y))

cv2.imshow("Gaussioan Noise", n)
cv2.waitKey(0)
cv2.destroyAllWindows()


#display the probability desnsity function
kde = gaussian_kde(n.reshape(int(x*y))) # creates the frequency from random number of gaussian noise
dist_space = np.linspace(np.min(n), np.max(n), 100) 


#create the noisy image
g = image + n

cv2.imshow("Noisy image", g)
cv2.waitKey(0)
cv2.destroyAllWindows()

#display all windowa
cv2.imshow("Original Imgae", image)
cv2.imshow("Gaussioan Noise", n)
cv2.imshow("Noisy image", g)

cv2.waitKey(0)
cv2.destroyAllWindows()

print (image.shape)
print (g.shape)


plt.figure(figsize=(10, 10))
plt.subplot(2, 2, 1)
plt.title("Image")
plt.imshow(image, "gray")
plt.subplot(2, 2, 2)
plt.title("Noisy image noise")
plt.imshow(g, "gray")
plt.subplot(2, 2, 3)
plt.title("Image Profile")
plt.plot(image[:, 100])
plt.subplot(2, 2, 4)
plt.title("Noisy image profile")
plt.plot(g[:, 100])

print("Synthetic image mean: {}".format(image[:,1].mean()))
print("Synthetic image variance: {}".format(image[:,1].var()))    
print("Noisy image mean: {}".format(g[:,1].mean()))
print("Noisy image variance: {}".format(g[:,1].var()))

