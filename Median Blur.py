# -*- coding: utf-8 -*-
"""
Created on Sun Jun 15 19:48:16 2025

@author: Ayobami Adeyemo
"""

""" Median Blurring
Here, the function cv.medianBlur() takes the median of all the pixels under the kernel area and the central element is replaced with this median value. This is highly effective against salt-and-pepper noise in an image. Interestingly, in the above filters, the central element is a newly calculated value which may be a pixel value in the image or a new value. But in median blurring, the central element is always replaced by some pixel value in the image. It reduces the noise effectively. Its kernel size should be a positive odd integer.

In this demo, I added a 50% noise to our original image and applied median blurring. Check the result: """

import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("C:/Users/Ayobami Adeyemo/Downloads/download.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
assert image is not None, "file could not be read, check with os.path.exists()"

median = cv2.medianBlur(image, 5)

plt.subplot(121), plt.imshow(image), plt.title("Original")
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(median), plt.title("Median Blur")
plt.xticks([]), plt.yticks([])
plt.show()