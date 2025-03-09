# -*- coding: utf-8 -*-
"""
Created on Sun Mar  9 18:56:59 2025

@author: Ayobami Adeyemo
"""

colors = int(input("Enter the number of colors needed:"))

def cost_painting_project(num_colors, tax):
    total_color_cost = 5 * num_colors
    final_cost_without_tax = total_color_cost + tax
    final_cost_with_tax = 1.1 * final_cost_without_tax
    
    return final_cost_with_tax

constant = 40
x = cost_painting_project(colors, constant)
print("The final cost of Painting Project is:", round(x))