x = "global value"

def func():
    # global x
    x = "some value from func"
    print(x)
    def inner_func():
        # nonlocal x
        global x
        x = "some value from inner func"
        print(x)
    inner_func()
    print(x)

def func_2():
    x = 202
    print(x)

def func_3(change_value):
    x = 303
    print(x)
    x += change_value
    print(x)

def func_4(x):
    print(x)

func()
func_2()
print(x)
func_3(1)
func_3(2)
func_3(3)
print(x)

func_4(4)
func_4("local value")