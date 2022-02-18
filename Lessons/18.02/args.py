x = "global value"

def test_func(x):
    print(x)

def another_test_func(x):
    print(x)

def change_int(x):
    x += 2

def change_list(x):
    x[0] += 2

test_func("test")
another_test_func("another")

test_int = 4
change_int(test_int)
print(test_int)

test_list = [4]
change_list(test_list)
print(test_list)

# print(1,2,3,4,5,6,7,8,9, sep=',', end='.')

def evaluate(x, y, z):
    return x + y * z

print(evaluate(1,2,3))
print(evaluate(z=1,x=2,y=3))
print(evaluate(1, 2, z=3))

def change_case(text, upper_case=True):
    return text.upper() if upper_case else text.lower()

change_case("some text")
print(change_case(change_case("some text"), False))

def sum(*args):
    print(type(args), args)
    res = 0
    for i in args:
        res += i
    return res

print(sum(1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1))
print(sum(*[1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1]))
# print(sum([1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1]))

def sum_values(**kwargs):
    res = 0
    for k, v in kwargs.items():
        print(k, v)
        res += v
    return res

d = {"one":1, "two":2, "three":3}
print(sum_values(one=1, two=2, three=3))
print(sum_values(**d))
# print(sum_values(**{1:"one"})) error

def my_print(x, y, z=0, *args, **kwargs):
    print(x, y, z)
    print(*args, sep=kwargs['sep'], end=kwargs['end'])

my_print(1,2,3,4,sep=',',end='.')