# -*- coding: utf-8 -*-
"""
Created on Sun Mar  9 18:56:59 2025

@author: Ayobami Adeyemo
"""

colors = int(input("Enter the number of colors needed:"))

def cost_painting_project(num_colors, other_cost):
    total_color_cost = 5 * num_colors                                  #num_colors: number colors needed for painting project
    final_cost_without_tax = total_color_cost + other_cost             #other cost includes the cost of canvas and brushes
    final_cost_with_tax = 1.1 * final_cost_without_tax                 #10% tax on total price
    
    return final_cost_with_tax

constant = 40
x = cost_painting_project(colors, constant)
print("The final cost of Painting Project is:", round(x))
