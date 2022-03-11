"""Отсортировать ['1', '11', '12', '22', '2', '13', '30', '33'] список по возрастанию числовых значений, исключив те, квадраты которых
являются нечетными числами"""

user_list = ['1', '11', '12', '22', '2', '13', '30', '33']
sorted_list = []

for i in user_list:
    sorted_list.append(int(i))

final_list = list(filter(lambda x: x*x % 2 == 0, sorted(sorted_list)))
print(final_list)