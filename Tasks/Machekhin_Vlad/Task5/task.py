# 1. Реализовать функцию check_str которая получает на вход непустую строку и выдаёт информацию о количестве букв в верхнем и нижнем регистре.
# check_str('The quick Brow Fox') -> '3 upper case, 12 lower case'

# 2. Реализовать функцию is_prime которая получает на вход любое число больше нуля и выдаёт True, если число является простым, и False, если нет.
# is_prime(787) -> True
# is_prime(777) -> False

# 3. Реализовать функцию get_ranges которая получает на вход непустой список неповторяющихся целых чисел, 
# отсортированных по возрастанию, и которая этот список “сворачивает”.

# get_ranges([0, 1, 2, 3, 4, 7, 8, 10])  ->  "0-4, 7-8, 10"
# get_ranges([4,7,10])  -> "4, 7, 10"
# get_ranges([2, 3, 8, 9])  -> "2-3, 8-9"

def check_str(s):
    small = 0
    large = 0
    if s == "":
        print("Enter your value.")
        return 
    for i in s:
        if i.isupper():
            large +=1
        elif i.islower():
            small +=1
        else:
           pass
    print(f'{large} upper case, {small} lower case.')
check_str('The quick Brow Fox')


def is_prime(n):
    if n <= 0:
        return "Please read the terms carefully."
    else:
        if n < 2:
            return False
        if n % 2 == 0:   # iterating over odd divisors if the number is not divisible by two
            return n == 2
        d = 3
        while d * d <= n and n % d != 0:
            d += 2
        return d * d > n 
print(is_prime(3))


def get_ranges(n):
    embryon = ""
    i = 0
    n.append('')
    while i < len(n)-1:
        sketch = []
        while n[i] + 1 == n[i+1]:
            sketch.append(n[i])
            i += 1
        else:
            if n[i] - 1 == n[i-1]:
                sketch.append(n[i])
            if len(sketch):
                embryon += f"{sketch[0]}-{sketch[-1]}, "
                i += 1
            else:
                embryon += f"{n[i]}, "
                i += 1
    embryon = embryon[:-2]  #cut off the excess
    return print(embryon)


get_ranges([0, 1, 2, 3, 4, 7, 8, 10])
get_ranges([4, 7, 10])
get_ranges([2, 3, 8, 9])




