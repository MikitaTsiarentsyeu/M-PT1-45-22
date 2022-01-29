# 1. Написать программу для поиска наиболее часто встречающихся элементов в строке.
# Пользователь вводит строку, и количество элементов, которые он хотел бы увидеть в ответе.

# Пример:
# Строка:lkseropewdssafsdfafkpwe
# Элементы:3
# 's' встречается 4 раза
# 'e' встречается 3 раза
# 'f' встречается 3 раза

s = input('Input your sentence here: ')
count_output_elem = int(input ('How many element you want see? '))

d = {}

# init key in dictionary
for c in s:
    d[c] = 0 
# count the number of elem
for c in s: 
    d[c] += 1 

# fix out index
if len(d.keys()) < count_output_elem:
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
    for i in range(count_output_elem):
        print (f"'{l[j][0]}' встречается {l[j][1]} раза")
        j += 1
