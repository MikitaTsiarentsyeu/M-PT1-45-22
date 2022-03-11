
def sort_number(num_str):
    result = sorted([int(x) for x in num_str]) 
    result = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, result)))
    return result

num_str = ['1','11','12','22','2','30','33']

print(num_str)
print(sort_number(num_str))
