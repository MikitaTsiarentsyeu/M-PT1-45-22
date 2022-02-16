"""1. Реализовать функцию check_str которая получает на вход непустую строку и выдаёт информацию о количестве букв в верхнем и нижнем регистре.
check_str('The quick Brow Fox') -> '3 upper case, 12 lower case'"""

import string
import random

def check_str(user_str):
    """Creating dict with info about number of letters in uppercase and lowercase
    
    Parameters:
        user_str: string
            user string from input
    Returns:
        count_dict: dict
            dict with number of counts lowercase and uppoercase letters"""
    count_dict = {"uppercase": 0, "lowercase": 0}
    for i in range(len(user_str)):
        if user_str[i].islower():
            count_dict["lowercase"] += 1
        else:
            count_dict["uppercase"] += 1
    return count_dict


variable_str = ''.join((random.choice(string.ascii_letters) for x in range(random.randint(1, 50))))  #generating random string with uppercase and lowercase letters
output = (check_str(variable_str))
print(f'Initial string: {variable_str}')
print(f'{output["uppercase"]} letters in uppercase, {output["lowercase"]} letters in lowercase')