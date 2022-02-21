"""2. Реализовать функцию is_prime которая получает на вход любое число больше нуля и выдаёт True, если число является простым, и False, если нет.
is_prime(787) -> True
is_prime(777) -> False"""

import random

def is_prime(x):
    """Returns True if number is prime, or False if number is nonprime.

    Parameters:
        x: integer
            user integer value
    Returns:
        Boolean
            True or False in case prime and nonprime value"""
    if x % 2 == 0:      #obviously if number divides for 2 it is nonprime, if it not 2
        return x == 2
    div = 3 #taking only odd elenets
    while div * div <= x and x % div != 0: #nonprime number has own div that does not exceed the square root of x (not 1)
        div += 2
    return (div * div > x)


value = random.randint(1, 1000)   #generating random integer value 
print(f'Number {value} is prime: {is_prime(value)}')
