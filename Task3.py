# 1. Написать программу для поиска наиболее часто встречающихся элементов в строке.
 # Пользователь вводит строку, и количество элементов, которые он хотел бы увидеть в ответе.
 #
 # Пример:
 # Строка:lkseropewdssafsdfafkpwe
 # Элементы:3
 # 's' встречается 4 раза
 # 'e' встречается 3 раза
 # 'f' встречается 3 раза

string = input("Введите строку:")
numb = int(input("Введите какое количество элементов вы хотите увидеть в ответе?"))

dict_1 = {}

for i in string:
     count = 0
     for y in string:
         if y == i:
             count +=1
             continue
     if i not in dict_1:
         dict_1.update({i: count})

dict_2 = {}
keys_1 = sorted(dict_1, key=dict_1.get, reverse= True)

for i in keys_1:
     dict_2[i] = dict_1[i]

flag = 0
for i in dict_2:
     if flag < numb:
         print(f"sybal {i} repeats {dict_2[i]}")
         flag +=1 

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

print("Введите текст")
string = input()
print("Введите какое количество элементов вы хотите увидеть в ответе?")
a = int(input())

string = string.lower()

string_2 = ''
for i in range(len(string)):
     if string[i].isalpha() or string[i] == ' ' or string[i] == '-':
         string_2 += string[i]

l = string_2.split(' ')

q = []
w = []
for i in l:
     if i not in q:
         q.append(i)
         w.append(l.count(i))

l = list(zip(q, w))

def kf_1(item_1):
     return item_1[0]

l.sort(key=kf_1)

def kf_2(item_2):
     return item_2[1]

l.sort(key=kf_2, reverse=True)

for i in range(a):
     print(f"слово {l[i][0]} встречается {l[i][1]} раз(а)")
