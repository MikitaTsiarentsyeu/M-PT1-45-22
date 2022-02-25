m=['1','11','12','22','2','13','30','33']
sorted_int=list(sorted(map(int,m)))
Filter=list(filter(lambda x:(x**2)%2==0 , sorted_int))
result=list(map(str,Filter))
print (result)
