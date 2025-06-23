# -*- coding: utf-8 -*-
"""
Created on Mon Jun 23 23:47:13 2025

@author: Ayobami Adeyemo
"""

# Use zip to create a dictionary cast that uses names as keys and heights as values.

cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]

for cast_name, cast_height in zip(cast_names, cast_heights):
    print("'{}': {}".format(cast_name, cast_height))

cast = dict(zip(cast_names, cast_heights))

print (cast)