# -*- coding: utf-8 -*-
"""
Created on Sun Mar 16 23:40:16 2025

@author: Ayobami Adeyemo
"""

price_pesos = int(input("Enter Price in Pesos"))
price_dollars = int(input("Enter Prices in Dollars"))

def calculate_price(pesos, dollars):
    pesos_in_hand = pesos
    dollar_rate = pesos_in_hand * 0.02
    dollar_in_hand = dollars
    
    if dollar_rate < dollar_in_hand:
        return "Pesos"
    elif dollar_in_hand < dollar_rate:
        return "Dollars"
    else:
        return "Dollars or Pesos"
    
dollars = price_dollars
x = calculate_price(price_pesos, price_dollars)
print("The best price", x)
    