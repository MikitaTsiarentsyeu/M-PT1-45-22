import data

def get_all():
    product = data.get_all()
    return '\n'.join([f"{(x[4])}.{', '.join(x[1])}: {(x[0])} - {x[2]}$, in quantity {x[3]}, product code {x[4]}" for x in product])

def get_all_category():
    category = data.get_all_category()
    return "\n".join([f"{i + 1}. {category[i]}" for i in range(0, len(category))])

def choose_category(name):
    choose = data.choose_category(name)
    if choose:
        return "\n".join(
            [f"{x[0]}. Product code - {x[4]}. Price - {x[2]}$." for x in choose])
    else:
        return "There is no such category."
    
def add_to_cart(code, total):
    products = data.get_all_codes()
    if code not in products:
        return 'There is no product with this product code.'
    elif data.add_to_cart(code, total):
        return f'{data.get_name(code)} add to you cart.'
    
def show_cart():
    cart = data.show_cart()
    if cart == {}:
        return "Your shopping cart is empty."
    cart_values = cart.values()
    return "In your cart:\n" + '\n'.join(
        [f"{x[0]}. {','.join(x[1])}. Product code - {x[4]}. Number of items in cart - {x[3]}" for x in
         cart_values])

def get_price_all():
    return f'Total price is {data.get_price_all()}$'

def buy():
    summ = data.get_price_all()
    data.buy()
    return f'Total cost - {summ}$'