# import some_external_module as sem

# sem.danger_func()

l = [12]

try:
    print(l[0])
    # 10/0
except IndexError:
    print("there is no such index in the list")
except NameError:
    print("there is no such object")
except:
    print("something went wrong")

print("after error")




try:
    raise NameError("the name is wrong")
except NameError:
    print("The name error occured!")



# for i in range(10):
#     if i % 2 == 0:
#         print(i)
#     else:
#         continue

for i in range(10):
    try:
        if i % 2 != 0:
            raise ValueError("the value must be even")
    except ValueError as er:
        print(er)
        continue
    print(i)

l = [1,2,3,4,5]

try:
    print(l)
    # 10/0
finally:
    print("this is finally")
    # print(n)
    del l
    l = []

print(l)

with open("test.txt", "w") as f:
    f.write("test")

try:
    f = open("test.txt", "w")
    f.write("test")
finally:
    f.close()


def test():
    try:
        10/0
    except ZeroDivisionError:
        print("Zero Division")
        return True
    finally:
        print("finally")
        

test()