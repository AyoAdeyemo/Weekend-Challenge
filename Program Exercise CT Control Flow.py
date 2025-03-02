# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 09:55:37 2024

@author: Ayobami Adeyemo
"""
# #n = int(input(3).strip())
# n = int(input("Enter your desire value of n:"))

# if n % 2 != 0:
#     print("Weird")
# elif n % 2 == 0 and n == [2,5]:
#         print("Not Weird")
# elif n % 2 == 0 and 6 <= n <= 20:
#         print("Weird")
# else:
#         print("Not Weird")


phone_balance = 6
bank_balance = 54

if phone_balance < 5 and bank_balance > 50:
    phone_balance += 10
    bank_balance -= 10
    
    print("Your current phone account balance is {}".format(phone_balance))
    print("Your current bank account balance is {}".format(bank_balance))
    
    
elif phone_balance > 5 and bank_balance < 50:
    print ("You have enough balance to go around but please top up your bank account to be more than 50")

elif phone_balance < 5 or bank_balance < 50:
    print("Your need to top up your bank balance to keep this service functional")

else:
    print("Your phone account balance is {}, this is good. Hahaha".format(phone_balance))
    print("Your bank account balance is {}, you are rich enough".format(bank_balance))
    
n = 5

if n % 2 == 0:
    print("Number" + str(n) + "is even")
else:
    print("Number" + str(n) + "is odd")
    
    
season = "spring"

if season == "spring":
    print("plant the garden")
elif season == "summer":
    print("wet the garden")
elif season == "fall":
    print("harvest the garden")
elif season == "winter":
    print("please stay indoors")
else:
    print("cannot specify what season is it")