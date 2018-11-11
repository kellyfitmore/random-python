#Stephen Duncanson
#Euler 10 part 2

def sieve(n):
    '''
    The Sieve of Eratosthenes, accepts an int arg and returns a list of all prime
    numbers below that number. Not good for things that are very large...
    '''
    test_list = []
    for i in range(2,n+1):
        test_list.append(i)
    prime_list = []
    while test_list != []:
        prime = test_list[0]
        for test_number in test_list:
            if test_number % prime == 0:
                test_list.remove(test_number)
        prime_list.append(prime)
    print(prime_list)
    return prime_list

def sum_list(sumlist):
    '''
    returns the sum of all items in a list
    '''
    total = 0
    for x in sumlist:
        total +=x
    return total

print(sum_list(sieve(2000)))

