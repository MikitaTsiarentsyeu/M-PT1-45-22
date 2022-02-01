# 1. Написать программу для поиска наиболее часто встречающихся элементов в строке.
# Пользователь вводит строку, и количество элементов, которые он хотел бы увидеть в ответе.

# Пример:
# Строка:lkseropewdssafsdfafkpwe
# Элементы:3
# 's' встречается 4 раза
# 'e' встречается 3 раза
# 'f' встречается 3 раза

s = input('Input your sentence here: ')
while True:
    count_output_elem = input ('How many element you want see? ')
    
    count_output_elem = count_output_elem.replace(' ', '')
    if not count_output_elem.isdigit():
        print ('Please input correct digit')
        continue
    count_output_elem = int(count_output_elem)

    d = {}

    # Make count of elem
    for c in s:
        if d.get(c, '') == '':
            d[c] = 1
        else:
            d[c] += 1

    # fix out index
    if len(d.keys()) < count_output_elem:
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
for i in range(count_output_elem):
    print (f"'{l[j][0]}' встречается {l[j][1]} раза")
    j += 1
