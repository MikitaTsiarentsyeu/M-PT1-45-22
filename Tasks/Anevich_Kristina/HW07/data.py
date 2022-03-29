catalog = { 
            1 : ["Pomade", ["Cosmetiks"], 15, 5, 1], 
            2 : ["Powder", ["Cosmetiks"], 17, 8, 2],
            3 : ["Mascara", ["Cosmetiks"], 20, 8, 3], 
            4 : ["Sneakers", ["Shoes"], 80, 7, 4],
            5 : ["Loafers", ["Shoes"], 90, 5, 5],
            6 : ["Boots", ["Shoes"], 70, 5, 6], 
            7 : ["Dress", ["Clothes"], 50, 11, 7],
            8 : ["Shirt", ["Clothes"], 45, 10, 8],
            9 : ["Trousers", ["Clothes"], 40, 10, 9],
}
cart = {}

def get_all():
    return catalog.values()

def get_all_category():
    category = []
    for z in catalog.values():
        for i in z[1]:
            if i not in category:
                category.append(i)
    return category

def choose_category(name):
    category = get_all_category()
    try:
        choosen_category = category[name - 1]
    except IndexError:
        return False
    products = filter(lambda x: choosen_category in x[1], catalog.values())
    return products

def get_name(code):
    return catalog[code][0]

def add_to_cart(code, total): 
        try:
            if cart.get(code):
                cart[code][3] += total
            else:
                cart[code] = catalog[code].copy()
                cart[code][3] = total
            return True
        except:
            return False
        
def get_all_codes():
    return catalog.keys() 
      
def show_cart():
    return cart

def get_price_all():
    price = 0
    for f in cart.values():
        price += f[2] * f[3]
    return price

def buy():
    global cart
    cart = {}