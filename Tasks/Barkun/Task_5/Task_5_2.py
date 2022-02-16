# 2. Реализовать функцию is_prime которая получает на вход любое число больше нуля и выдаёт True, 
# если число является простым, и False, если нет.
# is_prime(787) -> True
# is_prime(777) -> False

from math import sqrt
 
number = int(input('Enter any integer below: \n'))

def is_prime(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    nam_sqrt = sqrt(num)
    i = 2
    while i <= nam_sqrt:
        if num % i == 0:
            return False
        i += 1
    return True

print(is_prime(number))
