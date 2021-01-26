# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 21:08:44 2020

@author: byrd
"""
import re

userInput = ""
wordList =[]

while userInput != "quit":
    print("Please input a word to add to the list, anything with special charators or number will not be taken. Anything after a space will not be recored. Type quit to stop")
    userInput = input().lower().split(" ")[0]
    if not re.findall("[0-9]|[^A-Za-z0-9]", userInput):
        if userInput != "quit":
            if not userInput in wordList:
                wordList.append(userInput)
        else:
            print(wordList if wordList else "User did not add a valid input" )
    else:
        print("Numbers and special chartors are not accteped")