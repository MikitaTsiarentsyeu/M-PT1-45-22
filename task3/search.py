from collections import Counter, OrderedDict
word=input("Введите символы=")
t=int(input("Количество элементов в ответе="))
lit=[]
for x in word:
    lit.append(x)
lit=sorted(lit)
count=Counter(lit)
dfs=count
s = (OrderedDict(sorted(dfs.items(), key=lambda t: t[1], reverse=True)))
srez3 = list(s)[0:t] # срез
for key_srez in srez3:  # в словаре находим значения ключей
     print (key_srez, "встречается ", dfs.get(key_srez),"раза")
