# 1. Написать программу для поиска наиболее часто встречающихся элементов в строке.
# Пользователь вводит строку, и количество элементов, которые он хотел бы увидеть в ответе.

# Пример:
# Строка:lkseropewdssafsdfafkpwe
# Элементы:3
# 's' встречается 4 раза
# 'e' встречается 3 раза
# 'f' встречается 3 раза

stroka = input("Enter your string. ")
number = int(input("Enter the number of elements. "))

char_frequency = {}

for char in stroka:
    if char == " ": #to skip spaces
        continue
    elif char in char_frequency:
        char_frequency[char] += 1 
    else:
        char_frequency[char] = 1


char_frequency_sorted = sorted(char_frequency.items(), key=lambda ky: ky[1], reverse=True)

for i in range(number):
    print(f'The {char_frequency_sorted[i][0]} element occurs {char_frequency_sorted[i][1]} time(s).')

