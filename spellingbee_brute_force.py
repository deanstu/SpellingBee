"""
Created on Thu Dec  2 20:28:28 2021

@author: deanp
"""
'''
from enchant import Dict

dic = Dict("en_US")
'''

import pickle

in_file = open('changing_dictionary.pkl', 'rb')
dictionary = pickle.load(in_file)
in_file.close()

def check(word):
    return word in dictionary

def words4(letters, center):
    print("4 letter words")
    nletterwords = []
    for a in range(7):
        for b in range(7):
            for c in range(7):
                for d in range(7):
                    word = letters[a] + letters[b] + letters[c] + letters[d]
                    if word not in nletterwords and center in word and check(word):
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
                        if word not in nletterwords and center in word and check(word):
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
                            if word not in nletterwords and center in word and check(word):
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
                                if word not in nletterwords and center in word and check(word):
                                    nletterwords.append(word)
                                    print(word)                                   
                            
  
def words8(letters, center):
    print("8 letter words")
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
                                    if word not in nletterwords and center in word and check(word):
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
    
    response = input("any edits to the dictionary(y/n)? ").lower()
    if response == 'y':
        
        delete = input("remove any words from the dictionary(y/n)? ").lower()
        while delete == 'y':
            deletion = input("word to be removed: ").lower()
            try:
                dictionary.remove(deletion)
            except:
                print(deletion, " not in dictionary")
            delete = input("any more removals(y/n)? ").lower()
        
        add = input("any additions to the dictionary(y/n)? ").lower()
        while add == 'y':
            addition = input("word to be added: ").lower()
            if addition not in dictionary:
                dictionary.append(addition)
            else:
                print("word already in dictionary")
            add = input("any more additions(y/n)? ").lower()
        
          
        pickle.dump(dictionary, open("changing_dictionary.pkl", "wb"))                 
                            
main()       
    
                            
                            
                            
                            
