# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 08:41:03 2025

@author: Ayobami Adeyemo
"""

data = {"100-90": 25, "42-01": 48, "55-09": 12, "128-64": 71, "002-22": 18, "321-54":19, "097-32": 33, "065-135": 64, "99-043": 80,\
        "111-99": 11, "123-019": 5, "109-890": 72, "132-123": 27, "32-908": 27, "008-09": 25, "055-967": 35, "897-99": 44,\
        "890-98": 56, "344-32": 65, "43-955": 59, "001-233": 9, "089-111": 15,  "090-090": 17, "56-777": 23, "44-909": 27, "13-111": 21,\
        "87-432": 15, "87-433": 14, "87-434": 23, "87-435": 11, "87-436": 12, "87-437": 16, "94-121": 15, "94-122": 35, "80-089": 10, "87-456": 8, "87-430": 40}

q = int(input("Enter desired discount age:"))
y = data.values()
z = len(y)
# print(z)
# print (y)

def count(integer, chars=[]):
    count = 0
    for i in integer:
        if i in chars:
            count += 1
    return count

special = list(range(1,q+1))
x = count(y,special)
#print(x)


#Standard Revenue 
if q == 18:
    x = 15
    Total_revenue = (z - 15) * 20 +  15 * 5
    print(Total_revenue)
#Discounted Revenue
elif q == q:
    Discount_revenue = (z - x) * 20 + x * 5
    print ("Total Revenue at discount age", q ,"is:", Discount_revenue)

Total_revenue = (z - 15) * 20 +  15 * 5
Percentange_Change = abs((Discount_revenue - Total_revenue)/Discount_revenue * 100)
print("Percentage Change in Revenue with Discount Age", q, "is", round(Percentange_Change),"%")