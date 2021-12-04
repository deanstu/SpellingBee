"""
Created on Fri Dec  3 14:52:35 2021

@author: deanp
"""

import pickle
from enchant import Dict

dic = Dict("en_US")

words = []
letter = ""
with open('words.txt', 'r') as wordfile:
    for word in wordfile:
        if word.lower()[0] != letter:
            letter = word[0].lower()
            print(letter)
        if dic.check(word.lower()):
            words.append(word.lower())



    
pickle.dump(words, open("changing_dictionary.pkl", "wb"))
    
    


    
    
    
    
    
    
    
