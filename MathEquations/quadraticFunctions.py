import math
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 22:11:56 2021

@author: byrd
"""

def quad(a,b,c,x):
    return a*pow(x, 2)+b*x+c

def root(a,b,c):
    
    try: 
        discriminant = math.sqrt(pow(b,2)-4*a*c)
    except:
        discriminant = -1
    if discriminant <= 0:
        return print("None")
    answer = (((-b + discriminant)/(2*a)),((-b-discriminant)/(2*a)))
    
    return print(sorted(answer))
    