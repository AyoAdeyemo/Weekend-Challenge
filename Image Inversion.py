# -*- coding: utf-8 -*-
"""
Created on Mon Jul 14 11:29:11 2025

@author: Ayobami Adeyemo
"""

import cv2

def inverte(imagem, name):
    imagem = (255-imagem)
    cv2.imshow(name, imagem)
    
image = cv2.imread("C:/Users/Ayobami Adeyemo/Downloads/Test1.jpg")
img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
inverte(image, "inverted")
