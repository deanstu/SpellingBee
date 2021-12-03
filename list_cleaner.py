"""
Created on Thu Dec  2 19:53:37 2021

@author: deanp
"""

in_file = open('words.txt', 'r')
out_file = open('spelling_bee_dict.txt', 'w')

for line in in_file:
    line = line.strip()
    if len(line) > 3 and "'" not in line and not line[0].isupper():
        out_file.write(line+"\n")
    
in_file.close()
out_file.close()