# 2. Написать программу для поиска наиболее часто встречающихся слов в тексте.
# Пользователь вводит текст, и количество элементов, которые он хотел бы увидеть в ответе.
# При совпадении частоты использования, слова должны выводиться в алфавитном порядке.

# (Python, PYTHON и python должны считаться одним и тем же словом)

# Пример:
# Текст:The Python Software Foundation (PSF) is a 501 non-profit corporation that holds the intellectual property rights behind the Python programming language. We manage the open source licensing for Python version 2.1 and later and own and protect the trademarks associated with Python. We also run the North American PyCon conference annually, support other Python conferences around the world, and fund Python related development with our grants program and by funding special projects.
# Элементы:3
# 'python' встречается 6 раза
# 'the' встречается 6 раза
# 'and' встречается 5 раза

from collections import Counter
import heapq

user_str = input ('\nEnter any characters below:\n').lower() #переводим весь текст в нижний регистр

user_val = int(input ('\nEnter the number of items you would like to see in the response:\n'))

if user_val >= len(user_str): # проверка на правильность ввода (превышение числа выводимых чисел над длиной строки)
    print ('\nYou overestimated your capabilities (the number of elements is less than the number you entered)!!!')
else:

    simb_str = [',','.','!','?','(',')', ':']       #       избавляемся от знаков препинания
    for i in simb_str:
        user_str = user_str.replace(i,'')

user_str=sorted(user_str.split())                   #       сортируем строку по алфавиту и разбиваем на слова
user_str = Counter(user_str)                        #       создаем справочник
elem_simb = heapq.nlargest(user_val, user_str, key=user_str.get) # находим наиболее часто встречающиеся

i = 0                                               #       организуем цикл для вывода в нужном нам порядке
while i <= user_val -1:
    elem_max = user_str[elem_simb[i]]
    elem_max_name = elem_simb[i]
    print ("""\n'""" + elem_max_name + """'""",'встречается', elem_max, 'раза')
    i = i + 1

print ('\nThe program has finished its work! \ncDThank you, goodbye!\n')