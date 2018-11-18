# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 12:54:20 2018

@author: Leila
"""

from checkouttiers import checkouttiers

def test_checkout_returns_none():
    assert checkouttiers([],[],"normal") == None 
    
def test_checkout_returns_1000():
    assert checkouttiers(["Guitar"],[],"normal") == "The total is 1000"
    
def test_checkout_returns_1010():
    assert checkouttiers(["Guitar","Guitar Strings"],[],"normal") == "The total is 1010"
    
def test_checkout_returns_15():
    assert checkouttiers(["Pick Box","Pick Box", "Pick Box"],[],"normal") == "The total is 15"

def test_checkoutoptions_returns1000():
    assert checkouttiers(["Guitar"],[],"normal") == "The total is 1000"

    
def test_checkoutoptions_returnsNone():
    assert checkouttiers([],["Insurance"],"normal") == None
    assert checkouttiers([],[],"normal") == None    
    
def test_checkoutoptions_returns1005():   
    assert checkouttiers(["Guitar"],["Insurance"],"normal") == "The total is 1005"
    assert checkouttiers(["Guitar"],["Insurance","Insurance"],"normal") == "The total is 1005"
    
def test_checkouttiers_returns980():
    assert checkouttiers(["Guitar"],[],"silver") == "The total is 980.0"
    
def test_checkouttiers_returns954():
    assert checkouttiers(["Guitar"],["Insurance"],"gold") == "The total is 954.75"