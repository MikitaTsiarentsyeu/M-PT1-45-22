def outer(n):
    def inner(x):
        print(f"{n} and {x}")
    return inner

f = outer("cat")
f("dog")

d = outer("dog")
d("fish")