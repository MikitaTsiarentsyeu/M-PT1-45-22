def canonical_multiplication(x, y):
    res = 0
    if y < 0:
        x = -x
        y = -y
    for i in range(y):
        res += x

    return res

print(canonical_multiplication(2,-3))