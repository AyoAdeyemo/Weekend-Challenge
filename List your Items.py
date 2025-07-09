# -*- coding: utf-8 -*-
"""
Created on Wed Jul  9 23:48:51 2025

@author: Ayobami Adeyemo
"""

lessons = ["Biology", "Chemistry", "Mathematics", "Geography", "History"]

def my_enumerate(iterable, start=0):
    # Implement your generator function here
    k = 1
    for element in iterable:
        yield k, element
        k += 1


for i, lesson in my_enumerate(lessons, 1):
    print("Lesson {}: {}".format(i, lesson))