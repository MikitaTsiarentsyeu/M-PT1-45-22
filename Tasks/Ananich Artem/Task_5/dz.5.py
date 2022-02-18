# 1. Реализовать функцию check_str которая получает на вход непустую строку и 
# выдаёт информацию о количестве букв в верхнем и нижнем регистре.
# check_str('The quick Brow Fox') -> '3 upper case, 12 lower case'

# 2. Реализовать функцию is_prime которая получает на вход 
# любое число больше нуля и выдаёт True, если число является простым, и False, если нет.
# is_prime(787) -> True
# is_prime(777) -> False

# 3. Реализовать функцию get_ranges которая получает на вход непустой список 
# неповторяющихся целых чисел, 
# отсортированных по возрастанию, и которая этот список “сворачивает”.

# get_ranges([0, 1, 2, 3, 4, 7, 8, 10])  ->  "0-4, 7-8, 10"
# get_ranges([4,7,10])  -> "4, 7, 10"
# get_ranges([2, 3, 8, 9])  -> "2-3, 8-9"

#1
def checkStr(s):
    '''type(s) = str;
        type(result) = str;'''
    upper = 0
    lower = 0
    for i in s:
        if (ord(i) >= 65 and ord(i) <= 96) or (ord(i) >= 1040 and ord(i) <= 1071):
            upper += 1
        if (ord(i) >= 97 and ord(i) <= 122) or (ord(i) >= 1072 and (ord(i) <= 1103)):
            lower += 1
    print(f'{upper} upper case, {lower} lower case')

checkStr('I Like Watch Films About Programmers')

#2
def isPrime(num):
    '''type(num) = int;
       type(num) = str;
       type(result) = str;'''
    if (type(num) == float) or (num <= 1):
        print('Enter another NUMBER!')
        return
    num = int(num)
    if (num == 2) or (num == 3):
        print('True! (Number is simple)')
        return
    elif ((num**2)%24 == 1):
        print('True! (Number is simple)')
    else:
        print('False! (Number id not simple)')

isPrime(757)

#3
def get_ranges(input_lis):
    output = ""
    i = 0
    while i < len(input_lis):
        if i != 0:
            output += ","
        if i == len(input_lis) - 1:
            output += f" {input_lis[i]}"
            break
        if input_lis[i + 1] - input_lis[i] == 1:
            output += f" {input_lis[i]}"
            for j in range(i, len(input_lis)):
                if j == len(input_lis) - 1:
                    output += f" - {input_lis[j]}"
                    i += 2
                    break
                if input_lis[j + 1] - input_lis[j] != 1:
                    output += f" - {input_lis[j]}"
                    i += 1
                    break
                i += 1
        else:
            output += f" {input_lis[i]}"
            i += 1
    print(output)


lis = [1, 3, 7, 12, 13, 14, 15, 19, 21, 22, 23, 24, 27, 28, 54]
get_ranges(lis)


