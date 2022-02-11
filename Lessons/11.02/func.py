def test_func():
    print("hello from test func")

test_func()

x = test_func

flag = False
# if flag:
#     def test_func():
#         print("it's true!")
# else:
#     def test_func():
#         print("it's not!")

def test_func():
    if flag:
        print("it's true!")
    else:
        print("it's not!")

test_func()
x()

# old_input = input
# def input():
#     print("it's print now!!!")

# input()
# old_input("the old one")

# x = 4
# x = input
# x = "test"

def args_test(x, y):
    print(f"x:{x} y:{y}")

args_test(2, 3)
args_test("test", 7.7)

def list_test(x):
    x[0] = 444

def int_test(x):
    x += 2

l = [1,2,3,4,5]
list_test(l)
print(l)

i = 10
int_test(i)
print(i)

def return_test():
    return
    for i in range(10):
        print(i)
        if i == 5:
            return

print(return_test())