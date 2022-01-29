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

s = input('Input your sentence here: ').lower() # do all symbol to lower case
count_output_word = int(input ('How many word you want see? '))

# delete unwanted symbol
unwanted_symbol = [',','.','!','?','(',')']
for i in unwanted_symbol:
    s = s.replace(i,'')
s = s.split(' ')

d = {}

# init key in dictionary
for c in s:
    d[c] = 0 
# count the number of word
for c in s: 
    d[c] += 1 

# fix out index
if len(d.keys()) < count_output_word:
    print ('Incorrect count!')
else:
    l = sorted(d.items()) # sort to alphabet 

    # you sort write on our lesson <3
    for i in range(len(l)):
        m = i
        j = i + 1
        while j < len(l):
            if l[j][1] > l[m][1]: 
                m = j
            j += 1
        l[i], l[m] = l[m], l[i]
    
    # Output
    j = 0
    for i in range(count_output_word):
        print (f"'{l[j][0]}' встречается {l[j][1]} раза")
        j += 1