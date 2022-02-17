# Задание:

# 1. Реализовать функцию check_str которая получает на вход непустую строку и выдаёт информацию о количестве букв в верхнем и нижнем регистре.
# check_str('The quick Brow Fox') -> '3 upper case, 12 lower case'
# 2. Реализовать функцию is_prime которая получает на вход любое число больше нуля и выдаёт True, если число является простым, и False, если нет.
# is_prime(787) -> True
# is_prime(777) -> False
# 3. Реализовать функцию get_ranges которая получает на вход непустой список неповторяющихся целых чисел,
# отсортированных по возрастанию, и которая этот список “сворачивает”.
# get_ranges([0, 1, 2, 3, 4, 7, 8, 10, 11, 12])  ->  "0-4, 7-8, 10"
# get_ranges([4,7,10])  -> "4, 7, 10"
# get_ranges([2, 3, 8, 9])  -> "2-3, 8-9"

# ------------------------------------------------------------------------------------------------------------------ #

# Решение:

def check_str(string):
    """counts the number of uppercase and lowercase letters in a string"""
    return f"{sum(letter.isupper() for letter in string)} upper case, {sum(letter.islower() for letter in string)} lower case"


def is_prime(any_number):
    """returns True if the number is prime otherwise returns False"""
    if any_number == 1:
        return False
    for num in range(2, any_number):
        if any_number % num == 0:
            return False
    return True


def get_ranges(any_list):
    """collapses a list of non-repeating integers sorted in ascending order"""
    collapsed_list = []
    tmp = 0
    for num in range(len(any_list)-1):
        if any_list[num] + 1 == any_list[num + 1]:
            if any_list[num] - 1 == tmp:
                if collapsed_list[-1] != "-":
                    collapsed_list.append("-")
                tmp = any_list[num]
            else:
                collapsed_list.append(str(any_list[num]))
                collapsed_list.append("-")
                tmp = any_list[num]
        else:
            collapsed_list.append(str(any_list[num])), collapsed_list.append(", ")
    collapsed_list.append(str(any_list[-1]))
    return "".join(collapsed_list)

