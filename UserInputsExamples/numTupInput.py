# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


userInput = 0
numTup = ()


while userInput > -1:
    print("Please input whole int, when done input a negative number")
    correctInput = False
    while not correctInput:
        try:
            userInput = int(input())
            correctInput = True
        except:
            print("Please input a int")
    if userInput > -1:
        numTup = numTup + (userInput,)
    
print(numTup)