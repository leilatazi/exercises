# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 13:40:10 2018

@author: Leila
"""

#Our e-shop sells the following products:
#   1. Guitar: $1000
#   2. Pick box: $5
#   3. Guitar Strings: $10
#   Create a function named checkout that takes a list that represents a shopping cart and returns the total cost of it.  This function should check that the shopping cart must not be empty.
#   Create also some tests for the function.  Try to think of the corner cases.
#   Hint: you can represent a product as a dictionary with a name and a price.

#%%
prices = {"Guitar":1000,"Pick Box":5, "Guitar Strings":10}
mycart = ["Guitar","Guitar Strings","Guitar Strings","Guitar"]
prices_in_cart = []

def checkout(cart):
    if cart == []:
        return None
    else:
        for i in cart: 
            prices_in_cart.append(prices[i])
        return "The total is " + str(sum(prices_in_cart))

checkout(mycart)