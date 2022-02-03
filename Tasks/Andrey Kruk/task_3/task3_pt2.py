print('Enter your text:')
string = input()
print('Enter the number of most frequently occurring words you want to see:')
n = int(input())

string = string.lower()

result_string = ''
# lets pray that user use dashes for punctuation and hyphens for words
for i in range(len(string)):
    if string[i].isalpha() or string[i] == ' ' or string[i] == '-':
        result_string += string[i]

l = result_string.split(' ')

words = []
occurrences = []

for i in l:
    if i not in words:
        words.append(i)
        occurrences.append(l.count(i))
# when i split by ' ' i had extra spaces in my string so next line is removing it
words.remove('')

l = list(zip(words, occurrences))

# sorting by alphabet
def key_func_1(item_1):
    return item_1[0]


l.sort(key=key_func_1)

# sorting by number of occurrences
def key_func_2(item_2):
    return item_2[1]


l.sort(key=key_func_2, reverse=True)

for i in range(n):
    print(f'слово {l[i][0]} встречается {l[i][1]} раз(а)')
