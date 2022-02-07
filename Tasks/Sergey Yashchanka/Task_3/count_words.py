# Задание:

# 2. Написать программу для поиска наиболее часто встречающихся слов в тексте.
# Пользователь вводит текст, и количество элементов, которые он хотел бы увидеть в ответе.
# При совпадении частоты использования, слова должны выводиться в алфавитном порядке.
#
# (Python, PYTHON и python должны считаться одним и тем же словом)
#
# Пример:
# Текст:The Python Software Foundation (PSF) is a 501 non-profit corporation that holds the intellectual
# property rights behind the Python programming language. We manage the open source licensing for Python
# version 2.1 and later and own and protect the trademarks associated with Python. We also run the North
# American PyCon conference annually, support other Python conferences around the world, and fund Python related
# development with our grants program and by funding special projects.
# Элементы:3
# 'python' встречается 6 раза
# 'the' встречается 6 раза
# 'and' встречается 5 раза

# ------------------------------------------------------------------------------------------------------------------ #

# Решение:

text = input("please input your text | ")
elements = int(input("please input amount of elements | "))

sings = r"[](){}-+=!?@#$%'\,|./^*:;'_1234567890"  # characters to be removed from the text
for i in text:
    if i in sings:
        text = text.replace(i, "").lower()  # get text without characters and in lower case

count_dict = {}
for c in text.split(" "):  # get a dictionary with the number of repetitions of each element
    if c in count_dict:
        count_dict[c] += 1
    else:
        count_dict[c] = 1

sorted_values = sorted(count_dict.values())[::-1]  # sort elements by value

sorted_dict = {}
for i in sorted_values:  # get a sorting dictionary  with help 'sorted_values'
    for key in sorted(count_dict.keys()):
        if count_dict[key] == i:
            sorted_dict[key] = count_dict[key]

sorted_list = list(sorted_dict.items())  # put the dict in the list to access the elements by index

words = ["встречается", "раз", "раза"]
count = 0
while elements != 0 and count != len(sorted_list):  # print the output on screen
    end = str(sorted_list[count][-1])[-1]
    if 11 < int(sorted_list[count][1]) < 15:
        print(f"'{sorted_list[count][0]}' {words[0]} {sorted_list[count][1]} {words[1]}")
    elif 1 < int(end) < 5:
        print(f"'{sorted_list[count][0]}' {words[0]} {sorted_list[count][1]} {words[2]}")
    else:
        print(f"'{sorted_list[count][0]}' {words[0]} {sorted_list[count][1]} {words[1]}")
    elements -= 1
    count += 1
