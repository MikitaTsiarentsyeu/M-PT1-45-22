catalog = { 1: ["Toys", "lego", 101, 20.25, 20],
            2: ["Toys", "pazl", 102, 5.10, 10],
            3: ["Toys", "barbie", 103, 52.50, 30],
            4: ["Sport", "ball", 201, 10.20, 15],
            5: ["Sport", "mats", 202, 14.44, 5],
            6: ["Sport", "bags", 203, 22.80, 3],
            7: ["Bath", "spray", 301, 13.00, 15],
            8: ["Bath", "cream", 302, 14.49, 5],
            9: ["Bath", "soap", 303, 8.80, 3]            
            }
cart = []

def get_all():
    return catalog.values()

def add_cart(id, count): 
    for x in catalog.values():
        price = 0
        if x[2] == id:           
            if (x[4] - count) < 0: 
                raise RuntimeError(f"Please, change quantity of items in the cart. Only {x[4]} units left in stock")
            else:
                price = round((count * x[3]), 2)
                x[4] -= count
                cart.extend([[x[1], id, count, price, x[4]]])
                return True 
    raise NameError("The item with such id was not found")

def show_cart():
    if not cart:
        raise RuntimeError("The cart is empty")
    return cart

def make_order():
    if not cart:
        raise RuntimeError("The cart is empty")
    sum = 0
    for item in cart:
        sum += item[3]
    return sum