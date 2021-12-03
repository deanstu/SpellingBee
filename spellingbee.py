"""
Created on Wed Dec  1 16:52:10 2021

@author: deanp
"""


letters = "noahtmp".lower()
li = set(())
for l in letters:
    li.add(l)

center = letters[0]

with open('spelling_bee_dict.txt') as file:
    dictionary = []
    alphabet = set(())
    
    for line in file:
        dictionary.append(line.strip())
        alphabet.add(line[0])
        
def solver(letters, center):
    
    good = []
    bad_letters = alphabet.difference(li)
    
    for word in dictionary:
        if center in word:
            contains_bad_letter = False
            for letter in word:
                if letter in bad_letters:
                    contains_bad_letter = True
                    
            if not contains_bad_letter:
                good.append(word)
                
    return good

words = solver(letters, center)
for word in words:
    print(word)