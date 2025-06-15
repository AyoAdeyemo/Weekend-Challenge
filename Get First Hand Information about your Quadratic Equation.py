# -*- coding: utf-8 -*-
"""
Created on Sun Jun 15 12:01:40 2025

@author: Ayobami Adeyemo
"""

import numpy as np

def quadratic_equation(a, b, c):
    value = (b ** 2) - (4 * a * c)
    if value < 0:
        print("We will have a complex solution, I am not designed to solve that yet. I am still a work in progress")
        
    else:
        positive = (-b + np.sqrt(b**2 - (4 * a * c)))/ 2 * a
        negative = (-b - np.sqrt(b**2 - (4 * a * c)))/ 2 * a
        
        return positive, negative

x = int(input("Enter the value of a= "))
y = int(input("Enter the value of b= "))
z = int(input("Enter the value of c= "))


Answer = quadratic_equation(x, y, z)
print(Answer)
