string = input("Type your string here:")
el_num = int(input("How much repeating symbols do you want to see?"))

count_dict = {}

for i in string:
    count = 0
    for j in string:
        if j == i:
            count +=1
            continue
    if i not in count_dict:
        count_dict.update({i: count})

sorted_dict = {}
sorted_keys = sorted(count_dict, key=count_dict.get, reverse= True)

for i in sorted_keys:
    sorted_dict[i] = count_dict[i]

flag = 0
for i in sorted_dict:
    if flag < el_num:
        print(f"sybal {i} repeats {sorted_dict[i]}")
        flag +=1