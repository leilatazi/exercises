# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 00:15:50 2018

@author: Leila
"""

#Exercise 3
#Migrate the music store program we created to an OOP approach.  
#You can use classes for modelling products, services, customer tier, the shopping cart...
#
#Products have name and price.
#Services have price.
#Customer tier have a discount.
#Shopping cart has:
#a list of products
#a list of services
#and a method to add new products and another for services
#a checkout method that receives a customer tier and calculates the price

#%%

class Product:
    
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
guitar = Product("guitar",1000)   
pick_box = Product("pick box",5) 
guitar_strings = Product("guitar strings",10)

class Service:
    
    def __init__(self, name, price):
        self.name = name
        self.price = price

insurance = Service("insurance",5)
priority_mail = ("priority mail", 10)
        
class Tier:
    
    def __init__(self, discount):
        self.discount = discount
        
    def apply_discount(self,total):
        return total * (1 - (self.discount))
        
normal = Tier(0)
silver = Tier(0.02)
gold = Tier(0.05)

class ShoppingCart:
    
    products_list = []
    services_list = []
       
    def __init__(self,customer_tier):
        self.customer_tier = customer_tier
        
    def add_product(self,product):
        self.products_list.append(product.price)
    
    def add_service(self,service):
        if service not in self.services_list:
            self.services_list.append(service.price)
            
    def checkout(self):
        total = (sum(self.products_list) + sum(self.services_list))
        checkout_value = Tier.apply_discount(self.customer_tier,total)
        print("The total is " + str(checkout_value))
       
        
my_cart = ShoppingCart(silver)
my_cart.add_product(guitar)
my_cart.add_service(insurance)

my_cart.checkout()

    #%%    
        

#def checkouttiers(products_selection,options_selection,tier):
#    
#    products = {"Guitar":1000,"Pick Box":5, "Guitar Strings":10}
#    options = {"Insurance" : 5, "Priority mail" : 10}
#    tiers = {"normal":0,"silver":0.02,"gold":0.05}
#    before_discount = [] 
#    used_options = []
#
#    if products_selection == []:
#        return None
#    else:
#        for i in products_selection: 
#            before_discount.append(products[i])
#            for j in options_selection:
#                if j not in used_options:
#                    before_discount.append(options[j])
#                    used_options.append(j)
#                    
#    final_price = sum(before_discount) * (1-tiers[tier])
#                
#    return "The total is " + str(final_price)