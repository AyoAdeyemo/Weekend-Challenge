# -*- coding: utf-8 -*-
"""
Created on Sat Mar  1 22:17:24 2025

@author: Ayobami Adeyemo
"""

write_up = str(input("Enter your desired sentence(s):"))

def count_vowels(string, chars=[]):
    count = 0
    for i in string:
        if i in chars:
            count += 1
    return count



special = "AEIOUaeiou"
x = count_vowels(write_up,special)
print("The number of vowels in the sentence is:", x)

