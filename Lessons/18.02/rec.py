# def print_10_times(text):
#     i = 0
#     while True:
#         if i == 10:
#             break
#         print(text)
#         i += 1

def print_10_times(text, i=0):
    if i == 10:
        return
    print(text)
    print_10_times(text, i+1)

print_10_times("TO INFINITY AND BEYOND!!!")

1
1
1*2
1*2*3
1*2*3*4
1*2*3*4*5

def factorial(n):
    print(n)
    if n == 1:
        return 1
    c = factorial(n-1)
    print(c)
    return n*c

print(factorial(10))


def digit_sum_str(num, i=0, res=0):
    str_num = str(num) if isinstance(num, int) else num
    if i == len(str_num):
        return res
    res += int(str_num[i])
    c = digit_sum_str(num, i+1, res)
    print(c)
    return c

print(digit_sum_str(2345))

def digit_sum_rem(num):
    if num == 0:
        return 0
    rem = num % 10
    sum = digit_sum_rem(num//10)
    print(rem, sum)
    return rem + sum

print(digit_sum_rem(2345))

def level1():
    print("level 1 started")
    level2()
    print("the end of level 1")

def level2():
    print("level 2 started")
    level3()
    print("the end of level 2")

def level3():
    print("level 3 started")
    level4()
    print("the end of level 3")

def level4():
    print("level 4 started")
    print("the end of level 4")

level1()