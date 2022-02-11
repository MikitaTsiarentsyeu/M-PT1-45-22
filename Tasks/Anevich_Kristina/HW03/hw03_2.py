from xml.dom.minidom import Element


line = input("Введи строку:")
element = int(input("Сколько повторяющихся элементов ты хочешь увидеть?"))

dict = {}
sorted_dict = {}

line = line.lower()
line = line.split()

for i in line:
    s = dict.get(i, 0) 
    dict[i] = s + 1

dict_1 = sorted(dict, key=dict.get)

for i in dict_1:
    sorted_dict[i] = dict[i]

while element > 0:
    item = sorted_dict.popitem()
    print("{} встречается {} раз(а)".format(item[0], item[1]))
    element = element - 1

    if len(sorted_dict) < 1:
       break