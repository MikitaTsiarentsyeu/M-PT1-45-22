# 1. Написать программу для поиска наиболее часто встречающихся элементов в строке.
# Пользователь вводит строку, и количество элементов, которые он хотел бы увидеть в ответе.

# Пример:
# Строка:lkseropewdssafsdfafkpwe
# Элементы:3
# 's' встречается 4 раза
# 'e' встречается 3 раза
# 'f' встречается 3 раза


from collections import Counter
import heapq

user_str = input ('\nEnter any characters below:\n')

user_val = int(input ('Enter the number of items you would like to see in the response:\n'))

if user_val >= len(user_str):# проверка на правильность ввода (превышение числа выводимых чисел над длиной строки)
    print ('\nYou overestimated your capabilities (the number of elements is less than the number you entered)!!!')
else:
    user_str = Counter(user_str) # создаем справочник
    elem_simb = heapq.nlargest(user_val, user_str, key=user_str.get)    # находим наиболее часто встречающийся
                                                                        # (первые user_val ключа c наибольшими значениями)  
    i = 0                                                               # находим значения этих ключей и выводим на печать
    while i <= user_val -1:
        elem_max = user_str[elem_simb[i]]
        elem_max_name = elem_simb[i]
        print ("""\n'""" + elem_max_name + """'""",'встречается', elem_max, 'раза')
        i = i + 1

print ('\nThe program has finished its work! \ncDThank you, goodbye!')