import bl

def show_message(message):
    print(message + ".")

def get_value(message, end=":\n"):
    return input(message + end)

def user_login():
    """"register or login"""
    value = get_value('Enter user ID to login or 0 to register')
    if value == '0' :
        show_message(bl.register())
    else:
        show_message(bl.login(value) )

def show_user():
    """show all information about user, including
    cart and orders """
    show_message(bl.show_user())

def show_items():
    """select category and show items"""
    show_message(bl.show_catecories())
    value = get_value('Choose a category')
    show_message(bl.show_items(value))

def show_cart():
    """show user's cart"""
    show_message(bl.show_cart())

def show_order():
    """show current order"""
    show_message(bl.show_order())

def select_order():
    """select another order order"""
    value = get_value('Input order ID')
    show_message(bl.select_order(value))

def to_cart():
    """put the item to the cart"""
    value = get_value('input item ID')
    show_message(bl.to_cart(value))

def from_cart():
    """remove the item from the cart"""
    value = get_value('input item ID')
    show_message(bl.from_cart(value))

def clear_cart():
    """clear user's cart"""
    value = get_value('input 1 if you want to clear your shopping cart')
    if value == '1':
        show_message(bl.clear_cart())

def make_order():
    """make new order using items from cart"""
    value = get_value('input 1 if you want to make order')
    if value == '1':
        show_message(bl.make_order())

def cancel_order():
    """cancel current order"""
    value = get_value('input order ID to cancel')
    show_message(bl.cancel_order(value))

def exit_func():
    value = get_value('input 1 if you want to exit')
    if value == '1':
        show_message("Goodbye")
        exit()

# user-accessible functions and their menu names
func_dict = {'0': ("Exit",exit_func), '1': ("Show items", show_items), '2': ("Show your cart", show_cart),
            '3': ("Add item to cart", to_cart), '4': ("Delete item from cart", from_cart),
            '5' : ("Clear your cart", clear_cart), '6' : ("Make order",make_order), '7': ("cancel order",cancel_order),
            '8' : ("Show user profile", show_user)
            }

menu = "Choose your action:\n"
for key, value in func_dict.items():  #menu creation
    menu += "{}.  {} \n".format(key, value[0])

def main_flow():
    #repeat untill login or register
    while (not bl.user_id):
        user_login()

    while True:
        # select and evaluate function
        choosen_value = get_value(menu, end='')
        if choosen_value in func_dict.keys():
            func_dict[choosen_value][1]()