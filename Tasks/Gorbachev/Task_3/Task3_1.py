'''1. Написать программу для поиска наиболее часто встречающихся элементов в строке.
Пользователь вводит строку, и количество элементов, которые он хотел бы увидеть в ответе.

Пример:
Строка:lkseropewdssafsdfafkpwe
Элементы:3
's' встречается 4 раза
'e' встречается 3 раза
'f' встречается 3 раза'''
from collections import OrderedDict

def symbols(n, s):  
    value_list = {}
    for i in range(0, len(s), 1):
            if s[i] in value_list:
                value_list[s[i]] += 1
            else:
                value_list[s[i]] = 1
    value_list = (OrderedDict(sorted(value_list.items(), key=lambda t: t[1], reverse=True)))

    if n > len(value_list): # if lenght of symbols that should be shown are more than lenght of string
        n = len(value_list)
    symbol_count = list(value_list)[0:n] 

    for key in symbol_count:
        print(f'Symbol "{key}" used {value_list[key]} times.')
    return()

while True:
    s = str(input("Please enter your string: "))
    if len(s) == 0:
        print("Please enter valid string!")
        continue
    break

while True:
    n = (input("Please enter number of most used symbols in your string: "))
    if not n.isdigit():
        print("Number that you entered does not contain proper digits")
        continue
    n = int(n)
    break

symbols(n, s)
