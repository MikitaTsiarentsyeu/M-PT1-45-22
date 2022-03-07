import time

_time_amout = 0

def set_current_amount(ca):
    global _time_amout
    _time_amout = ca

def keeper(func):
    def wrapper(a, b):
        start = time.time()
        res = func(a, b)
        set_current_amount(time.time() - start)
        return res
    return wrapper

@keeper
def sum(x, y):
    for i in range(100000):
        i+1
    return x+y

x = sum(3, 4)
print(x, _time_amout)

y = sum(2, 5)
z = sum(6, 7)
t = sum(y, z)
print(t, _time_amout)