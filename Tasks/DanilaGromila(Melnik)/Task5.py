import math


def check_str(string):
    string = string.replace(" ", "")
    string = [x for x in string]
    uppers = 0
    lowers = 0
    for i in string:
        if i.isupper():
            uppers += 1
        else:
            lowers += 1
    print(f"{uppers} upper case, {lowers} lower case")


check_str('The quick Brow Fox')


def is_prime(number):
    i = 2
    while i <= math.sqrt(number):
        if number % i == 0:
            return print("False")
        i += 1
    print("True")


is_prime(787)
is_prime(777)


def get_ranges(l):
    ranged = ""
    l.append('') 
    i = 0
    while i < len(l)-1:
        intermediate = []
        while l[i] + 1 == l[i+1]:
            intermediate.append(l[i])
            i += 1
        else:
            if l[i] - 1 == l[i-1]:
                intermediate.append(l[i])
            if len(intermediate):
                ranged += f"{intermediate[0]}-{intermediate[-1]}, "
                i += 1
            else:
                ranged += f"{l[i]}, "
                i += 1
    ranged = ranged[:-2]  
    return ranged


print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))
print(get_ranges([4, 7, 10]))
print(get_ranges([2, 3, 8, 9]))
