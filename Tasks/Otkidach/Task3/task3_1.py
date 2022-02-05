# 1. Написать программу для поиска наиболее часто встречающихся элементов в строке.
# Пользователь вводит строку, и количество элементов, которые он хотел бы увидеть в ответе.

# Пример:
# Строка:lkseropewdssafsdfafkpwe
# Элементы:3
# 's' встречается 4 раза
# 'e' встречается 3 раза
# 'f' встречается 3 раза

from operator import itemgetter 


v = input("Введите строку: ")
e = int(input("Введите желаемое количество отображаемых элементов: "))


el = {} #для подсчета элементов

for element in v:
    if element not in el:
        el[element] = 1
    else:
        el[element] += 1
print(el)


ellist = [] #слорварь в список

for key, value in el.items():
    ellist.append([key,value])
print(ellist)

ellist = sorted(ellist, key=itemgetter(1), reverse=True) #сортировка по значениям использования
print(ellist)

for e in range(e):
    print(f'Символ "{ellist[e][0]}" используется {ellist[e][1]} раз(а)')


