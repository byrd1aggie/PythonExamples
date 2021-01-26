# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 09:53:17 2020

@author: byrd
"""
# var for Each standard US coin

coinValue = {"halfDollar":50, "quater":25,"dime":10,"nickle":5,"pennies":1}
coinReturn = {"halfDollar": 0, "quater": 0,"dime": 0,"nickle": 0,"pennies": 0}
# halfDollar = 5
# quater = 25
# dime = 1
# nickle = 5
# pennies =1

correctInput =False
while (not correctInput):
    print("Please input a number between 1 and 99")
    try:
        coinAmount = float(input())
        if 0 < coinAmount < 100: 
            correctInput = True
        else:
            print("Please input a value between 1 and 99")
        
    except:
        print("Please input a number between 1 and 99")
        
for key in coinValue:
    value = coinValue.get(key)
    numberOfCoin = int(coinAmount/value)
    if numberOfCoin > 0:
        coinReturn[key] = numberOfCoin
        coinAmount = coinAmount - numberOfCoin*value
print("Coins to return " )
print(coinReturn.items())