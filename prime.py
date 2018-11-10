#Stephen Duncanson


def factorial(number):
    fact = 1
    '''
    This function calculates the factorial of the argument and returns it.
    '''
    for n in range(number,1,-1):
        fact *= n
    return fact



def calc_e(decimal_place):
    '''
    This function calculates the value of e (Euler's constant) to the decimal place of
    the argument. Also fills a list with the digits of e as int.
    '''
    e = 1
    for n in range(1,decimal_place):
        e += (1/factorial(n))
    return e



print(calc_e(100000))
