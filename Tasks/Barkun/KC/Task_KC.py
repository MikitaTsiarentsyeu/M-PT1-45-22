from posixpath import split


setnum = 'five thirteen two eleven seventeen two one thirteen ten four eight five nineteen'

# разбиваем на элементы и формируем строку

setnum = setnum.split ()

print (setnum)

#создаем справочник

dict_set_num = {'one' : 1, 'two' : 2, 'three' : 3, 'four' : 4, 'five' : 5, 'six' : 6, 'seven' : 7, 'eight' : 8, 'nine' : 9, 'ten' : 10,
'eleven' : 11, 'twelve' : 12, 'thirteen' : 13, 'fourteen' : 14, 'fifteen' : 15, 'sixteen' : 16, 'seventeen' : 17, 'eighteen' : 18, 'nineteen' : 19, 'twenty' : 20,}

# преобразуем в числа 

set_num_val = []
for v in setnum:
    set_num_val.append(dict_set_num[v])
print (set_num_val)

# сортируем и исключаем дубликаты

set_num_val = list(set(sorted(set_num_val))) #list(set(sorted(set_nam_val))) - применять ли дополнительную фукцию?
print (set_num_val)

# преобразуем в последовательность натуральных чисел

[int(set_num_val) for set_num_val in set_num_val]
print(set_num_val)

# найходим произведение первого и второго числа, сумму второго и третьего, произведение третьего и четвертого и т.д.

set_num_val_sm = set_num_val
for i in range(len(set_num_val_sm) - 1): 
    if  i %2 != 0:
        set_num_val_sm[i] = (set_num_val_sm[i]) + (set_num_val_sm[i+1])
    elif i % 2 ==0:
         set_num_val_sm[i] = ( set_num_val_sm[i] * set_num_val_sm[i+1])
print ( set_num_val_sm)

# выводим полную сумму всех нечетных чисел

set_num_val = [set_num_val for set_num_val in set_num_val  if set_num_val % 2]
print(set_num_val) # все нечетные числа
set_num_val = sum(set_num_val)
print(set_num_val)
