# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 17:56:28 2018

@author: Leila
"""

from checkout import checkout

def test_checkout_returns_none():
    assert checkout([]) == None 
    
def test_checkout_returns_1000():
    assert checkout(["Guitar"]) == "The total is 1000"
    
def test_checkout_returns_1010():
    assert checkout(["Guitar","Guitar Strings"]) == "The total is 1010"
    
def test_checkout_returns_15():
    assert checkout(["Pick Box","Pick Box", "Pick Box"]) == "The total is 15"