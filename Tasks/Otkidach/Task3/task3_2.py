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

from operator import itemgetter 

v = input("Введите строку: ")
e = int(input("Введите желаемое количество отображаемых элементов: "))

v = v.lower() #нижний регистр для выравнивания и сравнения всех элементов

replacements = (',', '-', '!', '?','(',')') #разбивка на значения
for r in replacements:
    v = v.replace(r, ' ')
words = v.split()
print(words)

i = {} #счетчик использования значений

for element in words:
    if element not in i:
        i[element] = 1
    else:
        i[element]+=1
print(i)


ellist = [] #слорварь в список для подсчета

for key, value in i.items():
    ellist.append([key,value])
print(ellist)


ellist = sorted(ellist, key=itemgetter(1), reverse=True) #сортировка по значениям использования
print(ellist)

for e in range(e):
    print(f'Слово "{ellist[e][0]}" используется {ellist[e][1]} раз(а)')


#у меня не получилось по алфавиту с одинаковыми значениями
#у меня уже вторую задачу складывается ощущение, что из списка в словарь и обратно это как-то тупо...но ничего лучше пока придумать не получилось,не осуждайте женщину за такие гадости...

