import math

l_1 = ['1','11','12','22','2','13','30','33']
l_2 = []
l_3 = []
def l_str_int(l,val):
    if val == 1:
        for i in l:
            i = int(i)
            l_2.append(i)
        return l_2 
    if val == 2:
        for i in l:
            i = str(i)
            l_3.append(i)
        return l_3

def del_sqr(n):
    if (math.pow(n,2))%2 == 1:
        return -1
    if (math.pow(n,2))%2 == 0:
        return n
    
l_str_int(l_1,1)
l_2 = list(map(del_sqr,l_2))
l_2 = list(sorted(filter(lambda x: x > 0,l_2)))
l_str_int(l_2,2)
print(l_3)



