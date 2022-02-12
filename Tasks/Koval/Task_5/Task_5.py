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

from math import floor

def check_str (s):
    if s == '':
        return
    upper = 0
    lower = 0
    for c in s:
        if c.isupper():
            upper += 1
            continue
        if c.islower():
            lower += 1
    return f'{upper} upper case, {lower} lower case'

print('******************************* check_str *******************************')
print(check_str('The quick Brow Fox'))

def is_prime(num):
    for i in range(2, floor(num**(1/2))):
        if num % i == 0:
            return False

    return True

print('******************************* is_prime *******************************')

l = [13,15,21,23,27,123,113,131,333,523]

for i in l:
    print(f'{i} - {is_prime(i)}')

def is_sequence(start, end):
    if start != end:
        return f'{start}-{end}'
    return start

def get_ranges(l):
    out = []
    helper = False
    start, end = l[0], l[0]
    for i in range(len(l)-1):
        if l[i]+1 == l[i+1]:
            if helper == False:
                start = l[i]
                end = l[i+1]
                helper = True
                # case when last is sequence
                if end == l[-1]:
                    out.append(is_sequence(start,end))
            else:
                end = l[i+1]
        else:
            out.append(is_sequence(start,end))
            start,end = l[i+1], l[i+1]
            # case when last no sequence
            if end == l[-1]:
                out.append(is_sequence(start,end))
            helper = False          
    return out

print('******************************* get_ranges *******************************')

print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))
print(get_ranges([4,7,10]))
print(get_ranges([2, 3, 8, 9]))