# # -*- coding: utf-8 -*-
# """
# Created on Tue Oct  8 21:52:08 2024

# @author: Ayobami Adeyemo
# """

# # Write a function program to Sum up Two Numbers
# def sum_two_numbers(num1, num2):
#     n = num1 + num2
#     return n

# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter another number: "))

# result = sum_two_numbers(num1, num2)
# print("The Sum of Two Numbers", num1, "and", num2, "is", result)


# # Program that checks if a number is even or odd
# Number = int(input("Enter your desired number: "))

# if Number % 2 == 0:
#     print("The Number you entered", Number, "is an even number")
    
# else:
#     print("The Number you entered", Number, "is an odd number")
    

# # Loop that prints the first 10 positive integers
# for i in range(1, 11):
#     print (i)
    
# #2 Loop that prints the first 10 positive integers
# start_num = int(input("Enter your desired starting number: "))

# for i in range(start_num, start_num + 10):
#     print(i)
    
# #3 Loop that prints the first 10 positive integers
# def positive_integers(n):
#     for i in range (n, n + 10):
#         print (i)
        
        
# n = int(input("Enter a starting number"))
# positive_integers(n)

# Match Case write a code to determine whether a value  is (Interger, float or string)
def value_type():
    match value:
        case int():
            print ("Integer")
        case float():
            print ("Float")
        case str():
            print ("String")
        case _:
            print("Invalid Entry")

value = input("Enter the first thing that comes to your mind: integer, float or string: ")

value_type()

def numbers():
    match num:
        case 1:
            print("One")
        case 2:
            print ("Two")
        case 3:
            print ("Three")
        case _:
            print ("Invalid")
            
num = int(input("Enter a number between 1,2 and 3: "))

numbers()
        
        
    