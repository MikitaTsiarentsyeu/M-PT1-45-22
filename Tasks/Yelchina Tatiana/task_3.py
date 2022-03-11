'''1. Написать программу для поиска наиболее часто встречающихся элементов в строке.
Пользователь вводит строку, и количество элементов, которые он хотел бы увидеть в ответе.

Пример:
Строка:lkseropewdssafsdfafkpwe
Элементы:3
's' встречается 4 раза
'e' встречается 3 раза
'f' встречается 3 раза'''

string = input('Enter the string: ')
number = int(input('Enter the number of elements: '))

dict = {}
for i in string:
    if i in dict:
        dict[i] += 1 
    else:
        dict[i] = 1 

sorted_element = sorted(dict, key=dict.get, reverse=True)

for x in sorted_element[0:number]:   
    for j in dict.keys():
        if x == j:
            print (f"'{x}' встречается {dict[j]} раз")

'''2. Написать программу для поиска наиболее часто встречающихся слов в тексте.
Пользователь вводит текст, и количество элементов, которые он хотел бы увидеть в ответе.
При совпадении частоты использования, слова должны выводиться в алфавитном порядке.

(Python, PYTHON и python должны считаться одним и тем же словом)

Пример:
Текст:The Python Software Foundation (PSF) is a 501 non-profit corporation that holds the intellectual property rights behind the Python programming language. We manage the open source licensing for Python version 2.1 and later and own and protect the trademarks associated with Python. We also run the North American PyCon conference annually, support other Python conferences around the world, and fund Python related development with our grants program and by funding special projects.
Элементы:3
'python' встречается 6 раза
'the' встречается 6 раза
'and' встречается 5 раза'''

text = input('Enter the text: ')
elements = int(input('Enter the number of elements: '))

replace_value = {".":"", ",":"", "(":"", ")":"", "+":"", "!":"", "/":"", "*":"", "?":"", ";":"", ":":"", "    ":" "}
for x, y in replace_value.items():
    text = text.replace(x, y)        #replace all characters

text_list = (text.lower()).split(' ')

dict = {}
for i in text_list:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1

sorted_word = sorted(sorted(dict), key = dict.get, reverse=True)

for i in sorted_word[0:elements]:
    for j in dict.keys():
        if i == j:
            print (f"'{i}' встречается {dict[j]} раз")