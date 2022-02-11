# Задание:

# 1. Написать программу для поиска наиболее часто встречающихся элементов в строке.
# Пользователь вводит строку, и количество элементов, которые он хотел бы увидеть в ответе.
#
# Пример:
# Строка:lkseropewdssafsdfafkpwe
# Элементы:3
# 's' встречается 4 раза
# 'e' встречается 3 раза
# 'f' встречается 3 раза

# ------------------------------------------------------------------------------------------------------------------ #

# Решение:

string = input("please input your text | ")
elements = int(input("please input amount of elements | "))
count_dict = {}

for c in string.replace(" ", ""):  # get a dictionary with the number of repetitions of each element
    if c in count_dict:
        count_dict[c] += 1
    else:
        count_dict[c] = 1

sorted_values = sorted(count_dict.values())[::-1]  # sort elements by value
sorted_dict = {}
for i in sorted_values:  # get a sorting dictionary  with help 'sorted_values'
    for key in count_dict.keys():
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
