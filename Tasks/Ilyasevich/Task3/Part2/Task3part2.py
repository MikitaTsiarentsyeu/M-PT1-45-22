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
enter_string = "Python Software Foundation (PSF) is a 501 non-profit corporation that holds the intellectual property rights behind the Python programming language. We manage the open source licensing for Python version 2.1 and later and own and protect the trademarks associated with Python. We also run the North American PyCon conference annually, support other Python conferences around the world, and fund Python related development with our grants program and by funding special projects".lower().split(' ')
enter_elements = input('Input the number of elements: \n')

while True:
    if enter_elements.isdigit() == True:
        break
    if enter_elements.isdigit() == False:
        enter_elements = input('Вы ввели букву)\n''Input the number of elements: \n')
enter_elements = int(enter_elements)
result = {i: enter_string.count(i) for i in enter_string}
i = 1
for key in sorted(result, key=result.get, reverse=True):
    if i <= enter_elements and sorted(result.items(), key=lambda x: (x[1], x[0])):
        print(f'{key} встречается {result[key]}')
    i += 1

