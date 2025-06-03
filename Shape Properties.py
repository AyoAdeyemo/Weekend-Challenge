# -*- coding: utf-8 -*-
"""
Created on Tue Jun  3 23:36:06 2025

@author: Ayobami Adeyemo
"""

def volume_of_cylinder(height, radius):
    pi = 3.142
    return (pi * (radius ** 2) * height )

volume = volume_of_cylinder(10, 7)
print(volume)

def area_of_cylinder(height, radius):
    pi = 3.142
    print(((2 * pi * (radius)) * height) + 2 * (radius)**2)
area_of_cylinder(10, 7)



print ("Let's determine the size of the water tank")
Water_tank = area_of_cylinder(7, 2)
print("This is done")
print("This function returns: {}".format(Water_tank))
print("Now let's have another result")
Tank_volume = volume_of_cylinder(7, 2)
print("While this function return: {}".format(Tank_volume))