def counter(n):
    count = 0
    def result_func():
        nonlocal count
        count +=1
        return n+count
    return result_func

# def counter(n):
#     def result_func():
#         nonlocal n
#         n +=1
#         return n
#     return result_func

start_1 = counter(1)
start_100 = counter(100)

for i in range(10):
    print(start_1(), start_100())