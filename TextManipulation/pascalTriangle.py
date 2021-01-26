# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 21:52:23 2021

@author: byrd
"""


#function to create a pascal's trangle
def pascalTrangle(numberOfLevels):
    thisRowNumbers = []
    lastRowNumbers =[]
    pascalTrangle=[]
    # computes the row for the trangle
    for rowLength in range(0,numberOfLevels):
        for n in range(0,rowLength):  
            # Add a one at the start and end of the row
            if n == 0 or n == rowLength-1:
                thisRowNumbers.append(1)
            # cal ths number if it is not the start or the end of the row by using the last row
            else:
                thisRowNumbers.append(lastRowNumbers[n-1] + lastRowNumbers[n])
        # Setup the print for each row. Will need to save all rows for formating
        pascalTrangleRow=""
        for ele in range(0,len(thisRowNumbers)):
            if ele == len(thisRowNumbers)-1:
                pascalTrangleRow += (str(thisRowNumbers[ele]))
            else:
                pascalTrangleRow += (str(thisRowNumbers[ele])+ " ")
        pascalTrangle.append(pascalTrangleRow)
        
        
        # to print take the length of the last row divide by 2 and then place the middle of the current row in the middle of the last row. 
        # e.g. if the last row is 51 char long then then one need to add 22 space to the start and end of the 4 row to make the space at char(4) be at space 26
        lastRowSpace = len(pascalTrangle[-1])
        for row in pascalTrangle:
            print(row.center(lastRowSpace," "))
        # print(pascalTrangle[rowLength])
        lastRowNumbers.clear()
        lastRowNumbers = thisRowNumbers[:]
        thisRowNumbers.clear()

        
pascalTrangle(15)
    