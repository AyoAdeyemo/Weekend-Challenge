# -*- coding: utf-8 -*-
"""
Created on Sun Jun  8 13:50:59 2025

@author: Ayobami Adeyemo
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("C:/Users/Ayobami Adeyemo/Downloads/artuvia/Research Files/The-famous-Lena-image-often-used-as-an-example-in-image-processing.png", cv2.IMREAD_COLOR)

def draw_grid(img, grid_shape, color=(0), thickness=1):
    h, w, _ = img.shape
    rows, cols = grid_shape
    dy, dx = h / rows, w / cols
    
    #draw vertical lines
    for x in np.linspace(start=dx, stop=w-dx, num=cols-1):
        x = int(round(x))
        cv2.line(img, (x,0), (x, h), color=color, thickness=thickness)
        
    
    #draw horizontal lines
    for y in np.linspace(start=dy, stop=h-dy, num=rows-1):
        y = int(round(y))
        cv2.line(img, (0, y), (w, y), color=color, thickness=thickness)
        
    return img

grid_shape = (15, 15)
h, w, _ = image.shape
rows, cols = grid_shape
dy, dx = h / rows, w / cols


image_with_grid = draw_grid(image.copy(), grid_shape)

plt.figure(figsize=(6,6))
plt.imshow(image_with_grid)
plt.xlabel("Columns")
plt.ylabel("Rows")
plt.axis("off")

#Target cell
row, col = 4, 7
center_x = int((col + 0.5) * dx)
center_y = int((row + 0.5) * dy)

label_x = center_x - 180
label_y = center_y - 180


plt.annotate(
    "", 
    xy = (center_x, center_y),
    xytext = (label_x, label_y),
    arrowprops=dict(arrowstyle="->", color="green", linewidth=2)
)

plt.text(
    label_x, label_y - 10,
    "Pixel Intensity Value = f(x, y)",
    fontsize=13,
    fontweight="bold",
    color="black",
    ha="center",
    va="bottom",
    bbox=dict(facecolor="white", edgecolor="white", boxstyle="round, pad=0.3")
)


plt.tight_layout()
plt.show()