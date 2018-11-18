# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 12:52:27 2018

@author: Leila
"""

# You want to add a new feature to your ecommerce, 
# you want to create three different tiers of customers:
#
#   - normal: No added benefits
#   - silver: 2% discount on products from the ecommerce
#   - gold: 5% discount on everything
#
#   Modify the checkout function to accept another parameter with the 
#   tier of the customer and apply the discounts as needed.
#
#   Implement this feature in the checkout function and add tests 
#   that prove that your implementation is correct.

def checkouttiers(products_selection,options_selection,tier):
    
    products = {"Guitar":1000,"Pick Box":5, "Guitar Strings":10}
    options = {"Insurance" : 5, "Priority mail" : 10}
    tiers = {"normal":0,"silver":0.02,"gold":0.05}
    before_discount = [] 
    used_options = []

    if products_selection == []:
        return None
    else:
        for i in products_selection: 
            before_discount.append(products[i])
            for j in options_selection:
                if j not in used_options:
                    before_discount.append(options[j])
                    used_options.append(j)
                    
    final_price = sum(before_discount) * (1-tiers[tier])
                
    return "The total is " + str(final_price)