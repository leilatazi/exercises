# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 18:02:40 2018

@author: Leila
"""
from checkoutoptions import checkoutoptions

def test_checkout_returns_none():
    assert checkoutoptions([],[]) == None 
    
def test_checkout_returns_1000():
    assert checkoutoptions(["Guitar"],[]) == "The total is 1000"
    
def test_checkout_returns_1010():
    assert checkoutoptions(["Guitar","Guitar Strings"],[]) == "The total is 1010"
    
def test_checkout_returns_15():
    assert checkoutoptions(["Pick Box","Pick Box", "Pick Box"],[]) == "The total is 15"

def test_checkoutoptions_returns1000():
    assert checkoutoptions(["Guitar"],[]) == "The total is 1000"

    
def test_checkoutoptions_returnsNone():
    assert checkoutoptions([],["Insurance"]) == None
    assert checkoutoptions([],[]) == None    
    
def test_checkoutoptions_returns1005():   
    assert checkoutoptions(["Guitar"],["Insurance"]) == "The total is 1005"
    assert checkoutoptions(["Guitar"],["Insurance","Insurance"]) == "The total is 1005"