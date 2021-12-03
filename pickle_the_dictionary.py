"""
Created on Fri Dec  3 14:52:35 2021

@author: deanp
"""

import pickle
from enchant import Dict

dic = Dict("en_US")
letters = "abcdefghijklmnopqrstuvwxyz"

def words4(words):
    print("4 letter words")
    for a in range(26):
        for b in range(26):
            for c in range(26):
                for d in range(26):
                    word = letters[a] + letters[b] + letters[c] + letters[d]
                    if dic.check(word) and word not in words:
                        words.append(word)
        print(a)
    return words


def words5(words):
    print("5 letter words")
    for a in range(26):
        for b in range(26):
            for c in range(26):
                for d in range(26):
                    for e in range(26):
                        word = letters[a] + letters[b] + letters[c] + letters[d] 
                        word += letters[e]
                        if dic.check(word) and word not in words:
                            words.append(word)
        print(a)                            
    return words

def words6(words):
    print("6 letter words")
    for a in range(26):
        for b in range(26):
            for c in range(26):
                for d in range(26):
                    for e in range(26):
                        for f in range(26):
                            word = letters[a] + letters[b] + letters[c] + letters[d] 
                            word += letters[e] + letters[f]
                            if dic.check(word) and word not in words:
                                words.append(word)
        print(a)    
    return words               
                                
def words7(words):
    print("7 letter words")
    for a in range(26):
        for b in range(26):
            for c in range(26):
                for d in range(26):
                    for e in range(26):
                        for f in range(26):
                            for g in range(26):
                                word = letters[a] + letters[b] + letters[c] + letters[d] 
                                word += letters[e] + letters[f] + letters[g]
                                if dic.check(word) and word not in words:
                                    words.append(word)                 
        print(a)
    return words
                 
  
def words8(words):
    print("8 letter words")
    for a in range(26):
        for b in range(26):
            for c in range(26):
                for d in range(26):
                    for e in range(26):
                        for f in range(26):
                            for g in range(26):
                                for h in range(26):
                                    word = letters[a] + letters[b] + letters[c] + letters[d] 
                                    word += letters[e] + letters[f] + letters[g] + letters[h]
                                    if dic.check(word) and word not in words:
                                        words.append(word)        
        print(a)
    return words

  
def words9(words):
    print("9 letter words")
    for a in range(26):
        for b in range(26):
            for c in range(26):
                for d in range(26):
                    for e in range(26):
                        for f in range(26):
                            for g in range(26):
                                for h in range(26):
                                    for i in range(26):
                                        word = letters[a] + letters[b] + letters[c] + letters[d] 
                                        word += letters[e] + letters[f] + letters[g] + letters[h]
                                        word += letters[i]
                                        if dic.check(word) and word not in words:
                                            words.append(word)
        print(a)
    return words

def words10(words):
    print("10 letter words")
    for a in range(26):
        for b in range(26):
            for c in range(26):
                for d in range(26):
                    for e in range(26):
                        for f in range(26):
                            for g in range(26):
                                for h in range(26):
                                    for i in range(26):
                                        for j in range(26):
                                            word = letters[a] + letters[b] + letters[c] + letters[d] 
                                            word += letters[e] + letters[f] + letters[g] + letters[h]
                                            word += letters[i] + letters[j]
                                            if dic.check(word) and word not in words:
                                                words.append(word)
        print(a)
    return words


def main():
    words = []
    words = words4(words)
    words = words5(words)
    words = words6(words)
    words = words7(words)
    words = words8(words)
    words = words9(words)
    words = words10(words)
    pickle.dump(words, open("changing_dictionary.pkl", "wb"))
    
    
    
main()

    
    
    
    
    
    
    
