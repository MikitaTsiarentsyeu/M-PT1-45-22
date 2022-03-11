l = ['1','11','12','22','2','13','30','33']
int_l = sorted([int(i) for i in l])
l_res = list(filter(lambda x: x*x % 2 == 0, int_l))
print([str(i) for i in l_res])
