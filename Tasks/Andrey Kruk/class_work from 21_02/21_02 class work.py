input_list = ['1','11','12','22','2','13','30','33']
int_list = list(map(int, input_list))
filtered_list = list(filter(lambda x:(x**2)%2==0, int_list))
output_list = list(map(str, sorted(filtered_list)))

print(output_list)