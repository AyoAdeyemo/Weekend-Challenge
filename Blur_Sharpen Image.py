# -*- coding: utf-8 -*-
"""
Created on Wed May 28 23:41:14 2025

@author: Ayobami Adeyemo
"""

#Blurring an Image
import cv2
import numpy as np
import matplotlib.pyplot as plt

original_image = cv2.imread("C:/Users/Ayobami Adeyemo/Downloads/download.jpg", 0)

M = 3
blur_kernel = np.ones((M,M)) * 1/(M*M)


sharpen_kernel = np.array([[0, -1, 0],
                            [-1, 5, -1],
                            [0, -1, 0]], 
                          dtype=np.float32)

#apply the convolution
blur_image = cv2.filter2D(src=original_image, 
                          ddepth=-1,
                          kernel=blur_kernel)


cv2.imshow("blur_image", blur_image)
cv2.waitKey(10000)
cv2.destroyAllWindows()


sharpen_image = cv2.filter2D(src=original_image, 
                              ddepth=-1, 
                              kernel=sharpen_kernel)

#display all
cv2.imshow("image", original_image)
cv2.imshow("blur_image", blur_image)
cv2.imshow("sharpen_image", sharpen_image)
cv2.waitKey(10000)
cv2.destroyAllWindows()