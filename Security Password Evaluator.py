# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 15:08:42 2025

@author: Ayobami Adeyemo
"""
password = str(input("Enter your desired password:"))

def count_ascii(string, chars=[]):
    count = 0
    for i in string:
        if i in chars:
            count += 1
    return count



special = "!\"£$%&/()='?^+*[]{}#@-_.:,;" 
x = count_ascii(password,special)
#print("The count of special characters in your password is:", x)

def count_num(string, chars=[]):
    count = 0
    for k in string:
        if k in chars:
            count += 1
    return count

numbers = "0123456789"
y = count_num(password,numbers)
#print("The count of numbers in your password is:", y)
if len(password) < 7:
     print("Password not complete enter more than 7 Characters or More")
elif x < 2 and y < 2:
     print("Weak")
elif x < 2 or y < 2:
     print("Weak")
else:
     print("Strong")
