def test_func(x: int, y: int) -> int:
    """a test function to sum int values
    argements:
        x: int
        y: int
    returns:
        int"""
    return x + y

# print(test_func("3", "4"))
# print(help(test_func))



def times(x, y):
    return x*y

print(times(3, 2))
print(times("test", 3))

def times_int(x, y):
    if isinstance(x, int) and isinstance(y, int):
        return x*y

print(times_int(3, 2))
print(times_int("test", 3))


def intersection(coll1, coll2):
    res = []
    for x in coll1:
        if x in coll2:
            res.append(x)
    return list(set(res))

print(intersection([1,2,3,4,5], [4,5,6,7,8]))
print(intersection("[1,2,3,4,5]", "[4,5,6,7,8]"))
print(intersection("[1,2,3,4,5]", ['4','5',6,7,8]))