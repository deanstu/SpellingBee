"""
Created on Wed Dec  1 16:52:10 2021

@author: deanp
"""

import pickle 

in_file = open('changing_dictionary.pkl', 'rb')
dictionary = pickle.load(in_file)
in_file.close()
 
alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet = set(alphabet_list)  
        
def solver(letters, center):
    
    good = []
    bad_letters = alphabet.difference(letters)
    
    for word in dictionary:
        if center in word:
            contains_bad_letter = False
            for letter in word:
                if letter in bad_letters:
                    contains_bad_letter = True
                    
            if not contains_bad_letter:
                good.append(word)
                
    return good



letters = input("what are the letters? ").lower()
center = letters[0]
words = solver(letters, center)
for word in words:
    print(word)
    
response = input("any edits to the dictionary(y/n)? ").lower()
if response[0] == 'y':
        
    delete = input("remove any words from the dictionary(y/n)? ").lower()
    
    if delete[0] == 'y':
        deletion = input("word to be removed: ").lower()
        while deletion != "":
            try:
                dictionary.remove(deletion)
            except:
                print(deletion, " not in dictionary")
            deletion = input("word to be removed: ").lower()
        
    add = input("any additions to the dictionary(y/n)? ").lower()
    if add[0] == 'y':
        addition = input("word to be added: ").lower()
        while addition != "":
            if addition not in dictionary:
                dictionary.append(addition)
            else:
                print("word already in dictionary")
            addition = input("word to be added: ").lower()
        
    
    pickle.dump(dictionary, open("changing_dictionary.pkl", "wb"))
    
print("thanks for playing")  