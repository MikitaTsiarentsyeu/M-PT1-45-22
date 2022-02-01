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

user_sentence = input('Input your sentence here: ').lower() # do all symbol to lower case
while True:
    count_output_word = input ('How many word you want see? ')
    count_output_word = count_output_word.replace(' ', '')
    if not count_output_word.isdigit():
        print ('Please input correct digit')
        continue
    count_output_word = int(count_output_word)

    # delete unwanted symbol
    unwanted_symbol = [',','.','!','?','(',')',':', ';']
    for i in unwanted_symbol:
        user_sentence = user_sentence.replace(i,'')
    user_sentence = user_sentence.split(' ')

    d = {}

    # Make count of word
    for c in user_sentence:
        if d.get(c, '') == '':
            d[c] = 1
        else:
            d[c] += 1
       
    # fix out index
    if len(d.keys()) < count_output_word:
        print ('Incorrect count!')
        continue
    break

l = sorted(d.items()) # sort by alphabet 

# you sort write on our lesson <3
# make correct order by value
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