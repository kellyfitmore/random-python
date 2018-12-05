#Stephen Duncanson

total = 0
primes = []


def sqrt(number):
    root = number**.5
    return root

def is_prime(number):
    for z in range(2,int(sqrt(number))):
        if number % z == 0:
            return False
    return True

dirt = open('prime_paydirt.txt')
for line in dirt:
    line = int(line)
    primes.append(line)
dirt.close()

for num in primes:
    if not is_prime(num):
        primes.remove(num)

print(len(primes))
