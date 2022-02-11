# 2. Написать программу для поиска наиболее часто встречающихся слов в тексте.
# Пользователь вводит текст, и количество элементов, которые он хотел бы увидеть в ответе.
# При совпадении частоты использования, слова должны выводиться в алфавитном порядке.

# (Python, PYTHON и python должны считаться одним и тем же словом)

# Пример:
# Текст:The Python Software Foundation (PSF) is a 501 non-profit corporation that holds the intellectual property rights behind the Python programming language. We manage the open source licensing for Python version 2.1 and later and own and protect the trademarks associated with Python. We also run the North American PyCon conference annually, support other Python conferences around the world, and fund Python related development with our grants program and by funding special projects.
# Элементы:3
# 'python' встречается 6 раза
# 'the' встречается 6 раза
from collections import Counter 
import operator 


userSt = input('Input your string text: ') 
elemNum = int(input('Input how many words you would like to see in output: ')) 
userSt = userSt.lower().replace('.','').replace('(','').replace(')','').replace('!','').replace('?','').replace(',',' ').replace(':','').replace(';','') 
wordDict = dict(Counter(userSt.split(' '))) 
tupList = sorted(wordDict.items(), key=operator.itemgetter(1))
t = ['time','times']#сортировка по возрастанию повторяющихся слов

lt = [] 
iter = 0 
for i in range(1,int(tupList[len(tupList)-1][1])+1): 
    l = [] 
    while iter < len(tupList) and tupList[iter][1] == i: 
        l.append(tupList[iter]) 
        iter += 1 
    lt.append(l) 
res = [] 
for listOfTup in lt: 
    for tuple in sorted(listOfTup, key=lambda tuple:tuple[0],reverse=True): 
        res.append(tuple) 
res = dict(res) #сортировка по алфавиту для элементов которые повторяются одинаковое количество 
#раз и закидывание их в словарь
 
if (len(res) < elemNum):
    print('You have entered big number of elements, you will get our full TOP of elements ')#предупреждение о
#том что пользователь ввел слишком большое кол-во символов которые ТОП которых он хочет увидеть в ответе
#и памятка что в таком случае будут выводится все символы и сколько раз они повторяются
while True:
    if ('' in res):
        del res['']
    else:
        break #при создании словаря возникали пары ключ которых содержал пустую строку, и чтоб это не 
              #выводилось в ответ, удаляем такой элемент

j = 0 
for i in reversed(res): 
    if j < elemNum-1:
        if res[i] == 1:
            s = f'Word or letter \'{i}\' repeats {res[i]} {t[0]}'
            print(s) 
            j += 1 
        else:
            s = f'Word or letter \'{i}\' repeats {res[i]} {t[1]}'
            print(s)
            j += 1  #вывод ответа с конца словаря
            