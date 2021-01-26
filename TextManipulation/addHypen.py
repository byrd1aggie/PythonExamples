# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


# Create a tuple of preffixes and word suffixes
preffixes = ("anti","auto","de,""dis","down","extra","hyper","il","im","in","ir","inter","mega","mid","mis","non","over","out","post","pre","pro","re","semi","sub","super","tele","trans","ultra","un","under","up")
suffixes =("age","al","ance","ence","dom","ee","er","or","hood","ism","ist","ity","ty","ment","ness","ry","ship","sion","ion","xion","able","ible","en","ese","ful","i","ic","ish","ive","ian","less","ly","ous","y","ate","ify","ise","ize","ward","wards","wise")

#Function to evulated the word and determine where to place the hypen 



def addHypenInWord(wordToHypen):
    for pre in preffixes:
        if pre in wordToHypen:
            if wordToHypen[0:len(pre)].lower() == pre.lower():
                return (wordToHypen[0:len(pre)] + "-" + wordToHypen[len(pre):])
    for suf in suffixes:
        if suf in wordToHypen:
            if wordToHypen[len(suf)+1:].lower() == suf.lower():
                return (wordToHypen[0:len(suf)+1] + "-" + wordToHypen[len(suf)+1:])
    return wordToHypen[0:len(wordToHypen)//2] + "-" + wordToHypen[(len(wordToHypen)//2):]

print(addHypenInWord("drive"))
    
                          