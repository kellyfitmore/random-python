
new_dna = ""
dna = input("Enter some dna: ")

for x in dna:
    if x == "G" or x == "g":
        new_dna += "C"
    elif x == "C" or x == "c":
        new_dna += "G"
    elif x == "A" or x == "a":
        new_dna += "T"
    elif x == "T" or x == "t":
        new_dna += "A"
    else:
        print(dna)
print(new_dna)
