
goods = [["shirt", "clothes", 10, 5, 1], ["coat", "clothes", 50, 1, 2], ["jeans", "clothes", 25, 10, 3],
          ["ring", "jewelry", 3, 14, 4], ["necklace", "jewelry", 5, 7, 5], ["earring", "jewelry", 5, 0, 6],
         ["boots", "footwear", 40, 3, 7], ["shoes", "footwear", 38, 15, 8], ["socks", "accessories", 3.5, 5, 9],
         ["bag", "accessories", 27, 9, 10]]

shopping_cart = []


def show_category(category):
    """ Function to show items by category. Will raise an error if category is absent among all the goods.
    Makes a list of fitting items to manipulate."""
    product_list = []
    for item in goods:
        if category == item[1]:
            product_list.append(item)
    if not product_list:
        raise NameError
    else:
        return product_list


def show_all():
    return goods


def add_product(code):
    """ Function to add product to a shopping cart. Will raise an Error if product is out of stock. Decreases an amount
     of pieces in stock after adding one to a shopping cart."""
    for item in goods:
        if item[4] == int(code):
            if item[3] == 0:
                raise RuntimeError
            else:
                shopping_cart.append(item)
                item[3] -= 1
                return True


def place_order():
    if not shopping_cart:
        raise RuntimeError
    else:
        return shopping_cart


def shopping_card():
    return shopping_cart

