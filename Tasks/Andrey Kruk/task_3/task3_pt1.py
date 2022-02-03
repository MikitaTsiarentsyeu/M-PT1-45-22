print('Enter your string:')
string = input()
print('Enter the number of most frequently occurring items you want to see:')
n = int(input())

characters = []
occurrences = []

for i in string:
    if i not in characters:
        characters.append(i)
        occurrences.append(string.count(i))

l = list(zip(characters, occurrences))

# sorting by number of occurrences(i know i can use loop from the class work)
def key_func(item):
    return item[1]


l.sort(key=key_func, reverse=True)

for i in range(n):
    print(f'элемент {l[i][0]} встречается {l[i][1]} раз(а)')
