'''2. Написать программу для поиска наиболее часто встречающихся слов в тексте.
Пользователь вводит текст, и количество элементов, которые он хотел бы увидеть в ответе.
При совпадении частоты использования, слова должны выводиться в алфавитном порядке.

(Python, PYTHON и python должны считаться одним и тем же словом)

Пример:
Текст:The Python Software Foundation (PSF) is a 501 non-profit corporation that holds the intellectual property rights behind the Python programming language. We manage the open source licensing for Python version 2.1 and later and own and protect the trademarks associated with Python. We also run the North American PyCon conference annually, support other Python conferences around the world, and fund Python related development with our grants program and by funding special projects.
Элементы:3
'python' встречается 6 раза
'the' встречается 6 раза
'and' встречается 5 раза
'''

def element_num(n, d):
    word_dict = {}
    for i in range(len(d)):
        d[i] = d[i].lower()
        if d[i].isdigit():
            continue
        if d[i] in word_dict:
          word_dict[d[i]] += 1
        else:
            word_dict[d[i]] = 1
    tmp_list = list(word_dict.items())  # it is possible to solve this task in same way as previous (with OrderedDict)
    tmp_list.sort()
    tmp_list.sort(key=lambda i: i[1], reverse=True)
    if n > len(tmp_list): # if lenght of symbols that should be shown are more than number of words
        n = len(tmp_list)
    for i in range(n):
        print(f'Word "{tmp_list[i][0]}" used {tmp_list[i][1]} times.')
    return()

while True:
    s = [str(i) for i in input("Please enter your text here: ").replace("(", "").replace(")", "").replace(",", "").replace(".", "").replace("!", "").replace("?", "").replace("/", "").replace("+", "").replace(":", "").replace(";", "").split()]
    if len(s) == 0:
        print("Please enter valid text!")
        continue
    break

while True:
    n = (input("Please enter number of most used words in your text: "))
    if not n.isdigit():
        print("Number that you entered does not contain proper digits!")
        continue
    n = int(n)
    break

element_num(n, s)
