# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 17:57:18 2018

@author: Leila
"""

##You want to give more features to the user, so you decide that you will allow them to purchase an 
#insurance package on their purchase and also priority mail.  
#Consider that these two new services can only be purchase once per order.
##
##   1. Insurance: $5
##   2. Priority mail: $10
##
##   Modify your checkout function so it handles these cases correctly, 
#and add more tests that check your functionality.


def checkoutoptions(products_selection,options_selection):
    
    products = {"Guitar":1000,"Pick Box":5, "Guitar Strings":10}
    options = {"Insurance" : 5, "Priority mail" : 10}
    prices_in_cart = [] 
    used_options = []

    if products_selection == []:
        return None
    else:
        for i in products_selection: 
            prices_in_cart.append(products[i])
            for j in options_selection:
                if j not in used_options:
                    prices_in_cart.append(options[j])
                    used_options.append(j)
                
    return "The total is " + str(sum(prices_in_cart))