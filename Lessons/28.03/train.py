CART_LENGTH = 10

class FreightTrain:

    def __init__(self, cart_count) -> None:
        self.cart_count = cart_count

    def __str__(self) -> str:
        return f"a very long train of {self.cart_count} carts, choo-choo!"

    def __int__(self):
        return self.cart_count

    def __add__(self, other):
        return FreightTrain(self.cart_count+other.cart_count)

    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o, FreightTrain):
            return False
        return self.cart_count == __o.cart_count

    def __len__(self):
        return self.cart_count * CART_LENGTH

shorty = FreightTrain(3)

long = FreightTrain(10)

print(shorty)
print(str(long))
print(int(long) + int(shorty))

new_train = shorty + long
print(new_train)
print(shorty == long)
print(new_train == shorty + long)

print(len(new_train))