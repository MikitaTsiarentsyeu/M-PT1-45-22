Dictionary_football = [["form kit", 120, 10, 1], ["balls", 50, 7, 2],["football paraphernalia", 30, 12, 3]]
Dictionary_hockey = [["skates", 80, 10, 1], ["hockey stick", 20, 10, 2],["protective equipment", 340, 5, 3]]
Dictionary_tennis = [["racket", 85, 20, 1], ["tennis balls", 10, 100, 2],["form kit", 75, 5, 3]]
Dictionary_other = [["skiing", "price:90$", 6, 1], ["parachutes", 230, 3, 2]]

basket = []

def get_all_1():
    return Dictionary_football

def get_all_2():
    return Dictionary_hockey

def get_all_3():
    return Dictionary_tennis

def get_all_4():
    return Dictionary_other

def add_basket_1(code):
    for x in Dictionary_football:
        if x[3] == int(code):
            if x[2] > 0:
                basket.append(x)
                x[2] -= 1
                return True

def add_basket_2(code):
    for x in Dictionary_hockey:
        if x[3] == int(code):
            if x[2] > 0:
                basket.append(x)
                x[2] -= 1
                return True

def add_basket_3(code):
    for x in Dictionary_tennis:
        if x[3] == int(code):
            if x[2] > 0:
                basket.append(x)
                x[2] -= 1
                return True

def add_basket_4(code):
    for x in Dictionary_other:
        if x[3] == int(code):
            if x[2] > 0:
                basket.append(x)
                x[2] -= 1
                return True

def show_basket():
    return basket

def buy():
    if not basket:
        raise RuntimeError
    else:
        return basket
