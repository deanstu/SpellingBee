"""
Created on Wed Dec  1 16:52:10 2021

@author: deanp
"""

import pickle 

in_file = open('changing_dictionary.pkl', 'rb')
dictionary = pickle.load(in_file)
in_file.close()
 
alphabet = set(())   
for word in dictionary:
    alphabet.add(word[0])
        
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