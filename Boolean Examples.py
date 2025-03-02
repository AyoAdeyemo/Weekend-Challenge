# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 16:31:07 2024

@author: Ayobami Adeyemo
"""

# a = 7
# b = 5

# #equal to operator
# print("a == b is", a == b)

# #not-equal-to operator
# print("a != b is", a != b)

# #greater-than operator
# print("a > b is", a > b)

# #less-than operator
# print("a < b is", a < b)

# #greater-than or equal-to operator
# print("a >= b is", a >= b)

# #less-than or equal-to operator
# print("a <= b is", a <= b)

# #Decision on Weather
# is_raining = int(input("is it raining:"))

# if is_raining == 1:
#     print("Take an Umbrella")
# else:
#     print("Enjoy the weather")
    
# #Decision based on Age
# my_age = int(input("What is your age: "))

# if my_age > 12 and my_age < 20:
#     print("I am a Teenager, I am only", my_age, "years old")
    
# elif my_age > 20 and my_age < 40:
#     print("I am a Young Adult, I am", my_age, "years old")
    
# else:
#     print("You are either too young, growing old or very old")
    
    
# age = 15
# teen = age > 12 and age < 20
# print(teen)

# age = 15
# not_teen = not (age > 12 and age < 20)
# print (not_teen)

# my_pet = '"I like my dog\'s house so much"'
# print(my_pet)

# Conc = "0"+"5"
# print(Conc)

# name = "Ayobami Adeyemo"
# print(name.islower())
# number_a = name.count("A")
# print("my name has", number_a, "A\'s")

# Age = 28
# lives_in = "Hamburg"
# country = "Germany"
# citizen = "Nigerian"

# print("Ayobami Adeyemo is {} years old. He lives in {}, {} and he is {}".format(Age, lives_in, country, citizen))

# print("the man has {} cars".format(29))

# about_me = "Mein lieblingsplatz ist {}, weil/denn es ist {} und {}"
# print(about_me.format("Paris", "aufregend", "wunderbar"))


# def car_name(car_1, car_2):
#     car_1 = car_1.count("e")
#     car_2 = car_2.count("e")
#     if car_1 == 3 and car_2 == 1:
#         print("car_1 and car_2 could be Mercedes and Volkswagen respectively")
#     else:
#         print("now it is difficult to say maybe KIA, Toyota, Honda, etc")
        
# x = "KIA"
# y = "Volkswagen"
# car_name(x,y)


# new_str = "The cow jumped over the moon."
# print(new_str.split())

# #using the sep = separtor as a space and maxsplit set to 3, then we have
# print(new_str.split(" ", 3))

# #using "." or period as a seperator
# print(new_str.split("."))

# #using no separators but having a maxsplit argument
# print(new_str.split(None, 3))

# verse = "If you can keep your head when all about you\n Are losing theirs and blaming it on you,\n If you can trust yourself when all men doubt you,\n But make allowance for their doubting too;\n If you can wait and not be tired by waiting,\n Or being lied about, don’t deal in lies,\n Or being hated, don’t give way to hating,\n And yet don’t look too good, nor talk too wise:"
                        
# length_verse = len(verse)
# position_and = verse.find("and")
# #position_waiting = verse.find("waiting")
# #position_doubting = verse.find("doubting")
# #position_you = verse.find("you", 186, 248)
# position_you = verse.rfind("you") #uses reverse find i.e rfind
# occ_you = verse.count("you")

# print("The length of the string variable verse is:", length_verse)
# #print(position_waiting, position_doubting)
# print("The index of the first occurence of the word 'and':", position_and)
# print("The index of the last occurence of the word 'you':", position_you)
# print("The count of occurence of the word 'you':", occ_you)

# greeting = "Hello"
# print(greeting.capitalize()) #an exxample of error synthax error occurs before the start showing that there is an error with\ code computation while exception errors occur when the code is running

# chars = "supercalifragilisticexpialidocious"
# print(len(chars)) #with the given variable in len() this error occurs "TypeError: len() takes exactly one argument (0 given)"

Months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
# print(Months[-1])
# print(Months[0])

# list_of_random_things = [1, 2.5, 'a ball', True]
# print(list_of_random_things[len(list_of_random_things) - 1])
# print(list_of_random_things[-2])
# print(list_of_random_things[-3])

# j_months = Months[5:7]
# print(j_months)

# first_half = Months[:6]
# second_half = Months[6:]

# print(first_half)
# print(second_half)

# print('sunday' not in Months, 'sunday' in Months)
# print('fragilistic' in chars, 'fragilistic' not in chars)

# print("ring" in 'this is a string')
# print('three' not in "There are three of them")

# Months[4] = 'Friday'
# print(Months)     #TypeError: 'str' object does not support item assignment

# # greeting[1] = "b"
# # print(greeting) #TypeError: 'str' object does not support item assignment

# flat_owners = ['Ayobami', 'Waseem', 'Okemakinde', 'Ifemide', 'Dimeji', 'Joseph'] #names of flat owners accordingly
# owner_1 = flat_owners[0]
# print("the owner of the first flat is:", owner_1)


# days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# state = int(input("what month do you want to know its date?"))
# month = state + 1
# print("the numbers of days in", Months[state - 1], "is", days_in_month[month])


# def days_in_the_month(name_1):
#     if name_1 == str(input("Enter the month you want ot know its number of days")):
#         result_1 = Months.index(name_1)
#         print("the number of days in", name_1, "is", days_in_month[result_1])
#     else:
#         new = name_1 + 1
#         print("the numbers of days in", Months[name_1 - 1], "is", days_in_month[new])
        
# x = "December"
# days_in_the_month(x)
    

eclipse_dates = ['June 21, 2001', 'December 4, 2002', 'November 23, 2003',
                 'March 29, 2006', 'August 1, 2008', 'July 22, 2009',
                 'July 11, 2010', 'November 13, 2012', 'March 20, 2015',
                 'March 9, 2016']

print(eclipse_dates[-3:])
print(eclipse_dates[7:])

statement = "I am surprised that you came" #can be ordered but immutable
#statement_1 = print(statement.split())
statement_2 = ["I", "am", "surprised", "that", "you", "came"] #mutable and can be ordered

print(statement[24:27])
statement_2[0:2] = "She", "is"
print(statement_2)


name = "Jim"
student = name
student = "Tim"

print(name)
print(student)

scores = ["B", "C", "A", "D", "B", "A"]
grades = scores

print(scores)
print(grades)

scores[4] = "G"
print(scores)
print(grades)

num = [1, 10, 45, 20, 89]
print(len(num))
print(max(num))
print(min(num))
print(sorted(num))
print(sorted(num, reverse = True))

food = ["Apple", "Bread", "Kartoffeln", "Mehl", "Eis"]
print(max(food))
print(min(food))
print("the number of food items here is", len(food))
print(sorted(food))
print(sorted(food, reverse = True))

positions = ["North", "East", "South", "West"]
print("\n".join(positions))
print(" ".join(positions))

statement = "My father has a big yard"
state_1 = statement.split()
print(state_1)
state_1[1] = "Mother"
print(" ".join(state_1))

trial ="1234"
print(trial.split())

positions = ["North", "East", "South", "West"]
positions.append("North-east")
print(positions)


lat, long = 21.4123, 105.456
print("Ibadan's latitude is {}".format(lat))
print("Ibadan's long is {}".format(long))

length, breadth, height = 10, 23, 45
print("The dimesion of the cuboid is {}x{}x{}".format(length, breadth, height))

angle, direction = 30, "North-East"
print("The house is at {} degrees {}".format(angle, direction))

product = ("hp", 230.657)
print(type(product))
print("My laptop is {} series of version {}".format(product[0], product[1]))

bible_names = ["Genesis", "Exodus", "Leviticus", "Numbers", "Deteuronomy", "Joshua", "Judges", "Ruth", "Samuel", "Samuel", "Kings", "Kings", "Chronicles", "Chronicles", "Ezra"]
print(len(bible_names))
print(bible_names[:10])

bible_names = set(bible_names)
print(len(bible_names))
print(sorted(bible_names, reverse = True)) #sort elements in reverse alphabetical order
print("Ruth" in bible_names) #check for element
print("Habakkuk" not in bible_names) #check for element

# print(bible_names.pop())
# print(bible_names.pop())

bible_names_1 = bible_names.add("Nehemiah")
print(bible_names_1)

a = [1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
b = set(a)
print(len(a) - len(b)) #difference
b.add(5)
b.pop()
print(b)

print(a + a)


set_a = {1, 2, 3, 4}
set_b = {2, 4, 6, 8}

#Union of Sets
union_set = set_a.union(set_b)
union_set = set_a | set_b
print(union_set)

#Intersection of sets
intersection_set = set_a.intersection(set_b)
intersection_set = set_a & set_b
print(intersection_set)

#difference of sets
difference_set = set_a.difference(set_b)
union_set = set_a - set_b
print(difference_set)

#Dictionaries and Identity Operators
#Dictionaries
elements = {"hydrogen": 1, "helium": 2, "lithium": 3, "Boron": 4, "Carbon":6}
print(len(elements))
y = elements.values()
print(y)
print(sum(y))
print(elements.values())
print(elements.keys())
print(elements["Carbon"]) #this prints the value mapped to carbon
elements["Berylium"] = 5
print(elements)
print("Carbon" not in elements)
print(sorted(elements))
print(elements.get("Sulphur"))

#identity operators
x = elements.get("Sulphur")
null = x is None
not_null = x is not None

print(null)
print(not_null)

population = {"Shanghai":17.8, "Istanbul": 13.3, "Karachi": 13.0, "Mumbai": 12.5}
print("The population of Shanghai is", population["Shanghai"], "Millions")
print(population["Istanbul"])
#rint(population["Bangkok"])
y = population.get("Bangkok")
null = y is None
not_null = y is not None

print(population.get("Bangkok", "This element does not exist"))

animals = {"dogs": [3, 6, 9, 12], "cats": [2, 4, 6, 8], "rabbits": [1, 2, 3, 5], "frogs": [7, 11, 13, 17]}


#while True: print("Hello World")