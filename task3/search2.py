from collections import Counter, OrderedDict
word=input("Введите символы=")
t=int(input("Количество элементов в ответе="))
lit=[]
word=word.split(" ")
for x in word:
    lit.append(x)
lit=sorted(lit)
new_lit= [y.lower() for y in lit]
dfs=Counter(new_lit)
s = (OrderedDict(sorted(dfs.items(), key=lambda t: t[1], reverse=True)))# сотрировка словаря по значению, по убыванию
srez3 = list(s)[0:t] # срез на t элементов
srez3.sort()
for key_srez in srez3:  # в словаре находим значения ключей
    print (key_srez, "встречается ", dfs.get(key_srez),"раза") 
