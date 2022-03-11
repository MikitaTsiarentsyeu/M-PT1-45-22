
def rec_sum(l, sum=0):
    for i in l:
        if isinstance(i, int):
            sum += i
        else:
            sum += rec_sum(i)
    return sum


print(rec_sum([1, 2, [2, 4, [[7, 8], 4, 6]]]))


def fib_num(n):
    if n == 0:
        return 0
    elif n in (1, 2):
        return 1
    else:
        return fib_num(n - 2) + fib_num(n - 1)


def fib(n):
    for i in range(n):
        print(fib_num(i), end=" ")
    print("\n")  # for nice output


fib(5)
fib(7)
fib(10)


li = ['1', '11', '12', '22', '2', '13', '30', '33']
print(list(map(lambda x: str(x), sorted(list(filter(lambda x: x*x % 2 == 0, map(lambda x: int(x), li)))))))
# looks ugly to me but one line code is one line code
# better looking way:

l_int = [int(x) for x in li]
sorted_li = sorted(list(filter(lambda x: x*x % 2 == 0, l_int)))
result = [str(x) for x in sorted_li]
print(result)