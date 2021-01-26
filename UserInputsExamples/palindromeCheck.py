# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 22:01:29 2020

@author: byrd
"""
import re

print("Input a phase to check if it is Palindromes")

userInput = re.sub("[^a-zA-Z0-9]","",input().lower())

if userInput[::-1] == userInput:
    print("It's a Palindromes")
else:
    print("It's not a Palindromes")
