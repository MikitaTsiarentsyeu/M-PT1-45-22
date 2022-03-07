from aiohttp import TraceRequestChunkSentParams


def do_twice(func):
    def wrapper():
        print("The first call:")
        func()
        print("The second call:")
        func()
    return wrapper

def hello():
    print("hello!")

hello = do_twice(hello)
hello()

def test_print():
    print("some test text: abcdefg ABCDEFG")

x = do_twice(test_print)
x()

test_print = do_twice(test_print)
test_print()

is_auth = True

def auth(func):
    def wrapper(x, y):
        if is_auth:
            return func(x, y)
    return wrapper

def do_twice_params(func):
    def wrapper(x, y):
        print("The first call:")
        print(func(x, y))
        print("The second call:")
        print(func(x, y))
    return wrapper

@auth
@do_twice_params
def sum_two_numbers(a, b):
    return a + b

# sum_two_numbers = auth(sum_two_numbers)
# sum_two_numbers = do_twice_params(sum_two_numbers)
sum_two_numbers(1,2)