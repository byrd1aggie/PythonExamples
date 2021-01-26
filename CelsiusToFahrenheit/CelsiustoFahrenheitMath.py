# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 23:14:51 2020

@author: byrd
"""

print("Please choice you mesaurement unit, Type F for Fahrenheit or C for Celsius")

# Set a var for when user input is incorrect
correctInput = False
# ask for user input until user input a c or f
while(not correctInput):
    measuermentType = input().upper()
    if(measuermentType == "C" or  measuermentType== "F"):
        correctInput = True
    else:
        print("Incorrect input please, Type F for Fahrenheit or C for Celsius")
      
# Ask for user input of a float will continue to ask when input is not a float
print("Please type the temperature")
correctInput = False

while(not correctInput):
    try:
        measuerment = float(input())
        correctInput = True
    except:
        print("Incorrect input please type a number")

# Computes either C or F depending on user input
if(measuermentType == "C"):
    print("F = " + str(measuerment*(9/5)+32))
else:
    print("C = " + str(measuerment-32*(5/9)))