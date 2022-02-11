Dictionary = {"one": (1), "two": (2), "three": (3), "four": (4), "five": (5), "six": (6), "seven": (7),
              "eight": (8),"nine": (9), "ten": (10), "eleven": (11), "twelve": (12), "thirteen": (13),
              "fourteen": (14),"fifteen": (15),"sixteen": (16), "seventeen": (18), "eighteen": (19),
              "nineteen": (19), "twenty": (20),"twenty one": (21), "twenty two": (22), "twenty three": (23),
              "twenty four": (24)}

value = "five thirteen two eleven seventeen two one thirteen ten five eight five nineteen"
value_s = set(value.split())
new_list = []
new_sum = []
for x in value_s:
    new_list.append(Dictionary[x])
sum_of_odd_numbers = [el for el in new_list if el % 2 == 1]
print(sum(sum_of_odd_numbers))
new_list.sort(reverse=False)
for x in range(0, (len(new_list) - 1), 3):
    print(new_list[x] * new_list[x + 1])
    new_sum.append(new_list[x] * new_list[x + 1])
for x in range(1, (len(new_list) - 1), 3):
    print(new_list[x] + new_list[x + 1])
print(new_list)

