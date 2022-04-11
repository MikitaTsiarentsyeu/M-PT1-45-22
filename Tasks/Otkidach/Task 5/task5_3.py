# 3. Реализовать функцию get_ranges которая получает на вход непустой список неповторяющихся целых чисел, 
# отсортированных по возрастанию, и которая этот список “сворачивает”.

# get_ranges([0, 1, 2, 3, 4, 7, 8, 10])  ->  "0-4, 7-8, 10"
# get_ranges([4,7,10])  -> "4, 7, 10"
# get_ranges([2, 3, 8, 9])  -> "2-3, 8-9"

def get_ranges(l):
    fin_l = []
    out = ""
    for i in range(len(l)- 1):
        if l[i] + 1 == l[i + 1]:
            if l[i] - 1 == l[i - 1]:
                continue
            else:
                fin_l.append(str(l[i]))
                fin_l.append("-")
        else:
            fin_l.append((l[i]))
            fin_l.append(", ")
    fin_l.append(str(l[-1]))
    out = "".join(map(str, fin_l))
    return out

print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))
print(get_ranges([4, 7, 10]))
print(get_ranges([2, 3, 8, 9]))