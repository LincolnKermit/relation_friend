import os

relation = ["B"] #letter in order to work

#alphabet = [chr(i) for i in range(ord('A'), ord('Z')+1)]

file = open('r.txt', "r") # file

lines = file.readlines()

file.close()

def check(line):
    for letter in relation:
        if letter in line:
            print(f"Trouvé! La lettre '{letter}' est dans la ligne.")
            for l in line:
                if l.isalpha() and l != letter and l not in relation:
                    relation.append(l)
os.system("clear")
for line in lines:
    check(line) # main function

print(relation) # check the list