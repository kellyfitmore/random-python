#Stephen Duncanson
#This program generates a lot of numbers into a text file
#These numbers can then be sifted for primes


#Euler's function: f(n) = n^2 + n + 41
#Mills g(n) = int(1.3064^3^n)

#prime_paydirt = open('prime_paydirt.txt', 'w')

#minimum = int(input("What is the minimum: "))
#maximum = int(input("What is the maximum: "))

#for n in range(minimum, maximum):

import math

def is_prime(number):
    for z in range(2,int(math.sqrt(number))):
        if number % z == 0:
            return False
    return True



n = int(input("Test: "))
y = (n**2)+n+41

if is_prime(y):
    print("Is prime!")
    print(y)
else:
    print("Is not prime")

#    prime_paydirt.write(y + '\n')

#prime_paydirt.close()
