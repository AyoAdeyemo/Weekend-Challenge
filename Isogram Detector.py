# -*- coding: utf-8 -*-
"""
Created on Sun Mar 23 20:19:46 2025

@author: Ayobami Adeyemo
"""

word = str(input("Enter your desired word:"))
clean_word = word.lower()
def is_isogram(string):
    
    chars = []
    for letter in string:
        if letter.isalpha():
            if letter in chars:
                return "Not Isogram"
            chars.append(letter)
            
    return "Isogram"

x = is_isogram(clean_word)
print(x)
