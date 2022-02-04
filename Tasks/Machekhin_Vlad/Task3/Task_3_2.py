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

stroka = input("Enter your text. ")
number = int(input("Enter the number of elements. "))


stroka = stroka.lower()

char_frequency = {}

for char in stroka.split(" "):
    if char in char_frequency:
        char_frequency[char] += 1 
    else:
        char_frequency[char] = 1


char_frequency_sorted = sorted(char_frequency.items(), key=lambda ky: ky[1], reverse=True)

for i in range(number):
    print(f'{char_frequency_sorted[i][0]} occurs {char_frequency_sorted[i][1]} time(s).')


