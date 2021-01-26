# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 21:26:47 2020

@author: byrd
"""
import random

suit = ("clubs","diamonds","hearts","spades")
numberOfCard = ("Ace","1","2","3","4","5","6","7","8","9","10","Jack","Queen","King")
cardDeck = []

for i in suit:
    for j in numberOfCard:
        cardDeck.append(j + " of " + i)

cardDeck = random.sample(cardDeck, len(cardDeck))

print(cardDeck)