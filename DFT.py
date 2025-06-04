# -*- coding: utf-8 -*-
"""
Created on Wed Jun  4 09:32:09 2025

@author: Ayobami Adeyemo
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("C:/Users/Ayobami Adeyemo/Downloads/download.jpeg")

cv2.imshow("picture", image)
cv2.waitKey(10000)
cv2.destroyAllWindows()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Compute the discrete Fourier Transform of the image
fourier = cv2.dft(np.float32(gray), flags=cv2.DFT_COMPLEX_OUTPUT)

#shift the zero-frequency component to the center of the spectrum
fourier_shift = np.fft.fftshift(fourier)

#calculate the magnitude of the fourier transform
magnitude = 20*np.log(cv2.magnitude(fourier_shift[:,:,0], fourier_shift[:,:,1]))

#scale  the magnitude for display
magnitude = cv2.normalize(magnitude, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8UC1)

#Display the magnitude of the Fourier Transform
cv2.imshow("Fourier Transform", magnitude)
cv2.waitKey(10000)
cv2.destroyAllWindows()


plt.plot(magnitude)
plt.show()
