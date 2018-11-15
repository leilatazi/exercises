# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 21:19:59 2018

@author: Leila
"""

#%% White Belt

import math

def volume_cilinder (r,h):
    return math.pi*(r**2)*h

volume_cilinder (3,5)

#%% Blue Belt

names = ['pass',"proficiency",'excellence', 'honours']
values = [0.15, 0.35, 0.35, 0.15]

plt.bar(names, values)

plt.xlabel('Grade')
plt.ylabel('% of Students')
plt.title('Grading on a Curve IE')

#%% Create the following packages:
#- a utils package, containing a functions module.  The functions module should contain a function area_triangle that calculates the area of a triangle.
#- a data package, containing a triangles module that declares a variable triangle_definitions with a list of 10 triangle definitions.  Each triangle definition should be a dictionary like:

#{"base": 10, "height":2}

#- a main.py file that will use utils.functions.area_triangle and data.triangles.triangle_definitions to print the areas of all triangles



