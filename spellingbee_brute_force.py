# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 20:28:28 2021

@author: deanp
"""

from enchant import Dict

dic = Dict("en_US")

#letters = "noahtmp".lower()
#center = letters[0]

def words4(letters, center):
    print("4 letter words")
    nletterwords = []
    for a in range(7):
        for b in range(7):
            for c in range(7):
                for d in range(7):
                    word = letters[a] + letters[b] + letters[c] + letters[d]
                    if word not in nletterwords and center in word and dic.check(word):
                        nletterwords.append(word)
                        print(word)


def words5(letters, center):
    print("5 letter words")
    nletterwords = []
    for a in range(7):
        for b in range(7):
            for c in range(7):
                for d in range(7):
                    for e in range(7):
                        word = letters[a] + letters[b] + letters[c] + letters[d] + letters[e]
                        if word not in nletterwords and center in word and dic.check(word):
                            nletterwords.append(word)
                            print(word)


def words6(letters, center):
    print("6 letter words")
    nletterwords = []
    for a in range(7):
        for b in range(7):
            for c in range(7):
                for d in range(7):
                    for e in range(7):
                        for f in range(7):
                            word = letters[a] + letters[b] + letters[c] + letters[d] + letters[e] + letters[f]
                            if word not in nletterwords and center in word and dic.check(word):
                                nletterwords.append(word)
                                print(word) 
                                
                                
def words7(letters, center):
    print("7 letter words")
    nletterwords = []
    for a in range(7):
        for b in range(7):
            for c in range(7):
                for d in range(7):
                    for e in range(7):
                        for f in range(7):
                            for g in range(7):
                                word = letters[a] + letters[b] + letters[c] + letters[d] + letters[e] + letters[f] + letters[g]
                                if word not in nletterwords and center in word and dic.check(word):
                                    nletterwords.append(word)
                                    print(word)                                   
                            
  
def words8(letters, center):
    print("7 letter words")
    nletterwords = []
    for a in range(7):
        for b in range(7):
            for c in range(7):
                for d in range(7):
                    for e in range(7):
                        for f in range(7):
                            for g in range(7):
                                for h in range(7):
                                    word = letters[a] + letters[b] + letters[c] + letters[d] + letters[e] + letters[f] + letters[g] + letters[h]
                                    if word not in nletterwords and center in word and dic.check(word):
                                        nletterwords.append(word)
                                        print(word)                             
                                
                            
                            
def solver(letters, center):
    words4(letters, center)
    words5(letters, center)
    words6(letters, center)
    words7(letters, center)
    words8(letters, center)
    

                        
                            
def main():
    
    letters = input("what are the letters? ").lower()
    center = letters[0]
    solver(letters, center)
                           
                            
main()              
                            
                            
                            
                            
