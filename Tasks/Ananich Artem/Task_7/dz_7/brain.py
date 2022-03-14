import heart


def get_all():
    items = heart.get_all_items()
    comma = ','
    return '\n'.join([f'{i[0]} - {comma.join(i[1])}' for i in items])


def add_to_basket(n):
    basket = heart.add_to_basket()
    basket.append(heart.katalog[n][0])
    return basket


def show_basket():
    basket = heart.add_to_basket()
    return '\n'.join([f'{i}' for i in basket])


def if_basket_is_empty():
    basket = heart.add_to_basket()
    if not basket:
        return False
    else:
        return True


def input_customer():
    try:
        name = input('What in your name?\n')
        if name.isdigit():
            raise ValueError
        city = input('What is your city?\n')
        street = input('What is your street?\n')
        house = input('What is number of your house?\n')
        house = int(house)
        flat = input('What is your flat?\n')
        flat = int(flat)
    except ValueError:
        print("Incorrect user data")
        return False
    phone = input('What is your phone?\n')
    try:
        phone = int(phone)
        if not (999999 < phone < 10000000):
            raise RuntimeError("Phone number must have 7 digits")
    except ValueError:
        print("Incorrect user data")
        return False
    except RuntimeError as er:
        print(er)
        return False
    heart.order.append(name)
    heart.order.append(city)
    heart.order.append(street)
    heart.order.append(house)
    heart.order.append(flat)
    heart.order.append(phone)
    return heart.order


def show_data():
    data = heart.make_order()
    comma = ','
    return comma.join([f'{i}' for i in data])


def make_order():
    order = input_customer()
    return order