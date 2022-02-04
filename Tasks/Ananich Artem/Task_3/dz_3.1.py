# 1. Написать программу для поиска наиболее часто встречающихся элементов в строке.
# Пользователь вводит строку, и количество элементов, которые он хотел бы увидеть в ответе.

# Пример:
# Строка:lkseropewdssafsdfafkpwe
# Элементы:3
# 's' встречается 4 раза
# 'e' встречается 3 раза
# 'f' встречается 3 раза
from collections import Counter 
import operator


user_str = input('Enter your string: ') 
elem_num = int(input('Enter how much elements you would like to see in output: ')) 
slov = dict(Counter(user_str))#Создание словаря где ключ - символ, а знаечние - сколько раз он повторяется
t = ['time','times']

if len(slov) <= elem_num:
    print('You have entered big number of elements, you will get our full TOP of elements ')#предупреждение о
#том что пользователь ввел слишком большое кол-во символов которые ТОП которых он хочет увидеть в ответе
#и памятка что в таком случае будут выводится все символы и сколько раз они повторяются

sorted_d = dict(sorted(slov.items(), key=operator.itemgetter(1), reverse=True))#сортировка словаря
#в порядке убывания ключа чтоб было проще выводить ответ

counter = 0 
for i in sorted_d: 
    if counter < elem_num: 
        if sorted_d[i] == 1:
            s = f'Element \'{i}\' repeats {sorted_d[i]} {t[0]}'
            counter += 1
            print(s)
        else:
            s = f'Element \'{i}\' repeats {sorted_d[i]} {t[1]}'
            counter += 1
            print(s) #вывод ответа

        

