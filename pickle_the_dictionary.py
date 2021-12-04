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
        word = word.lower().strip()
        if dic.check(word) and "'" not in word and '-' not in word and len(word) > 3 and '.' not in word and word not in words:
            if word[0] != letter:
                letter = word[0]
                print(letter)
            words.append(word)


    
pickle.dump(words, open("changing_dictionary.pkl", "wb"))
    
    


    
    
    
    
    
    
    
