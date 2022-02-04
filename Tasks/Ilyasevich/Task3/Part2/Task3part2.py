# 2. Написать программу для поиска наиболее часто встречающихся слов в тексте.
# Пользователь вводит текст, и количество элементов, которые он хотел бы увидеть в ответе.
# При совпадении частоты использования, слова должны выводиться в алфавитном порядке.
#
# (Python, PYTHON и python должны считаться одним и тем же словом)
#
# Пример:
# Текст:The Python Software Foundation (PSF) is a 501 non-profit corporation that holds the intellectual
# property rights behind the Python programming language. We manage the open source licensing for
# Python version 2.1 and later and own and protect the trademarks associated with Python. We also run the North American
# PyCon conference annually, support other Python conferences around the world, and fund Python related development with
# our grants program and by funding special projects.
# Элементы:3
# 'python' встречается 6 раза
# 'the' встречается 6 раза
# 'and' встречается 5 раза

from operator import itemgetter, attrgetter, methodcaller
enter_string = input('Input the string, use the words only, without spacebar: \n').lower()       # приводим все к нижнему регистру
enter_elements = input('Input the number of elements: \n')

while True:                                                            # выполняем проверку, можно упростить код, но пока так
    if enter_elements.isdigit() == True:
        break
    if enter_elements.isdigit() == False:
        enter_elements = input('Вы ввели букву)\n''Input the number of elements: \n')
enter_elements = int(enter_elements)
result = {i: enter_string.count(i) for i in enter_string}              # создаем словарь со значения к которому будем обращаться
i = 1                                                                  # решил, что словарь проще использовать чем иные коллекции
for key in sorted(result, key=result.get, reverse=True):               # проходим по словарю, ищем,сортируем,проверяем,сортируем и выводим.коротко и без переменных
    if i <= enter_elements and sorted(result.items(),key=lambda x: (x[1], x[0])):  # мы не проходили лямда-выражения но в процессе поиска нашел такой вариант
        print(f'{key} встречается {result[key]}')                                  # попробовал работает, надеюсь разберем домашку, а после прохождения темы
    i += 1                                                                         # лямда-выражения станет еще понятнее

# первую часть забыл прокомментить, прошу меня простить)
