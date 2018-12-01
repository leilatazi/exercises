# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 00:01:25 2018

@author: Leila
"""

#%%

#Create a Polyhedron class, and two classes Triangle and Circle that inherit from it.
#Make Triangle and Circle have an area method that return their respective areas

import math

class Polygon:
        
    def area(self):
        pass

# Triangl & Circle are subclasses of Polygon

class Triangle(Polygon):
    
    def __init__(self,base,height):
       self.base = base
       self.height = height
       
        
    def area(self):
        return self.base * self.height / 2
        
class Circle(Polygon):
    
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return math.pi * self.radius ** 2
    
Circle(3).area()

# useful if you are creating a list of Circles and Triangles, 
# they are not from the same class but both inherit the area function form Polygon

shapes = [
        Circle(3),
        Triangle(2,3),
        Circle(5)]

for shape in shapes:
    print(shape.area())
