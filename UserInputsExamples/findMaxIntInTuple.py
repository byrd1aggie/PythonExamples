# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 07:15:07 2020

@author: byrd
"""
# The tuple para for findMaxIndex
testTuple = (0,11,2,3,400,5,6,70)

# Creates a function to find the max number in a tuple, take one tuple
def findMaxIndex(*numTuple):
    # Store the max number
    max = 0
    # Store the index of max number
    maxIndex = 0
    for i in range(0,len(numTuple)):
        if numTuple[i] > max:
            max = numTuple[i]
            maxIndex = i
    return maxIndex

# print the return value for testTuple
print(findMaxIndex(*testTuple))
