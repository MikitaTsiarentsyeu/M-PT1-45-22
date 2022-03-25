from unicodedata import name


class X:

    name = "X"

class Y:

    name = "Y"

class Z:

    name = "Z"

class A(X, Y):

    name = "A"

class B(Y, Z):

    name = "B"

class M(B, A, Z):

    name = "M"

print(M.mro())
