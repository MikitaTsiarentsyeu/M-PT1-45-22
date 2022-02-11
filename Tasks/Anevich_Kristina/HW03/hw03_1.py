line = input("Введите строку:")
element = int(input("Сколько повторяющихся элементов ты хочешь увидеть?"))

count_dict = {}

for i in line:
    count = 0
    for s in line:
        if s == i:
            count +=1
            continue
    if i not in count_dict:
        count_dict.update({i: count})
        
sorted_dict = {} 
       
sorted_desc = sorted(count_dict, key=count_dict.get, reverse= True)

for i in sorted_desc:
    sorted_dict[i] = count_dict[i]

Rez = 0
for i in sorted_dict:
    if  Rez < element:
        print(f"{i} повторяется {sorted_dict[i]} раз(а)")
        Rez +=1