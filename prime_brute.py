#Stephen Duncanson
#Brute force prime finder - takes 16 seconds to sum primes below 2 million
#Also a sqrt function


def sqrt(n):
    root = int(n ** 0.5) #Raising a number ^1/2 is the same as taking root
    return root


def is_prime(n):
    for x in range(2,sqrt(n)+1):
        if n % x == 0 and n != x:
            return False
    return True


def sum_list(sumlist):
    total = 0
    for x in sumlist:
        total +=x
    return total


prime_list = []


for x in range(2,2000001):
    if is_prime(x):
        prime_list.append(x)
        
print(sum_list(prime_list))
