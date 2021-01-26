# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 17:16:04 2020

@author: byrd
"""
# x is the user input and the number that the sqaure will be guess
# square will be guessed to .000001 
# g will hold the last guess and newG will hold the new guess

correctInput = False
while not correctInput:
    print("Please input a postive number")
    try:
        x = float(input())
        if x > 0:
            correctInput = True
    except:
        ("Your input must be a postive number")

g = x/2
newG = 0
toFarOff = True

while toFarOff:
    newG = (g +x/g)/2
    if g - newG < .000001: break
    g = newG

print(f'The estimated sqaure of {x} is {newG}')