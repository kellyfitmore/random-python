#Stephen Duncanson
#Program to calculate molar mass
#version 1.0
#only 56 elements working so far LOL
#Add r for restart

#These lists hold the elements and their atomic masses
elements = [
    "H", "He","Li","Be","B","C","N","O","F","Ne",
    "Na","Mg","Al","Si","P","S","Cl","Ar","K","Ca",
    "Sc","Ti","V","Cr","Mn","Fe","Co","Ni","Cu","Zn",
    "Ga","Ge","As","Se","Br","Kr","Rb","Sr","Y","Zr","Nb",
    "Mo","Tc","Ru","Rh","Pd","Ag","Cd","In","Sn","Sb","Te",
    "I","Xe","Cs","Ba",
]
#element 43 has a mass of 0 in this list
atomic_mass = [
    1.008,4.00,6.94,9.01,10.81,12.01,14.01,16.00,19.00,20.18,
    22.99,24.31,26.98,28.09,30.97,32.06,35.45,39.95,39.10,40.08,
    44.96,47.87,50.94,52.00,54.94,55.85,58.93,58.69,63.55,65.38,
    69.72,72.63,74.92,78.97,79.90,83.80,85.47,87.62,88.91,91.22,
    92.91,95.95,0,101.07,102.91,106.42,107.87,112.41,114.82,118.71,
    121.76,127.60,126.90,131.29,132.91,137.33,
]

position = 0
element = ""


molar_mass = 0
factor = 1

while element != "m":
    element = input("Enter an atomic symbol or m to return mass: ")
    if element in elements:
        position = elements.index(element)
        
        factor = input("how many " + element + ": ")
        if factor == "":
            factor = 1
        else:
            factor = int(factor)
        molar_mass += factor * atomic_mass[position]

    elif element not in elements and element != "m":
        print("That's not an element.")
        
print(molar_mass, "g/mol")
