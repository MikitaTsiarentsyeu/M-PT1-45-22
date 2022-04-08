exmpl_list =[1, 2, [2, 4, [[7, 8], 4, 6]]]


def sum_list(some_list):
    sum = 0
    for i in some_list:
        if isinstance(i, int):
            sum += i
        else:
            sum += sum_list(i)
    return sum


print(sum_list([1, 2, [2, 4, [[7, 8], 4, 6]]]))


def fib_num(n):
    if n in {0,1}:
        return n
    return fib_num(n-2) + fib_num(n-1)


l=[str(fib_num(i)) for i in range(10)]


print(','.join(l))
