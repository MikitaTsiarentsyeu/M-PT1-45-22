import data
user_id = ''  #  global variable, current user ID
order_id = ''  # global variable, current order ID

def validate_id(value):
    """ validate number(str) ID """
    if not value.isdigit():
        raise RuntimeError("value must contain numbers")


def decorator_validate_id(func):
    """decorate functions with argument and validation"""
    def maker(id):
        try:
            validate_id(id)
            result = func(id)
        except (RuntimeError, NameError) as err:
            return str(err)
        except:
            return "Something went wrong"
        return result

    return maker

def decorator(func):
    """decorate functions without argument and validation"""
    def maker():
        try:
            result = func()
        except (RuntimeError, NameError) as err:
            return str(err)
        except:
            return "Something went wrong"
        return result

    return maker

@decorator_validate_id
def login(value):
    """find existing ID, logs user"""
    global user_id
    if data.search_user(value):
        user_id = value
        return "Welcome. Your profile\n" + show_user()
    else:
        raise RuntimeError("user ID doesn't exist")
@decorator
def register():
    """register user, creates new ID"""
    global user_id
    user_id = data.register_user()
    return f"Welcome, user #{user_id}"

def show_item(item_id):
    """show item information"""
    item = data.get_item(item_id)
    return f' ID :{item_id} CATEGORY: { item["category"] } NAME: {item["name"]}\
    PRICE: {item["price"]} QUANTITY IN STOCK: {item["quantity"]}'

@decorator
def show_catecories():
    """show categories"""
    cat_dict = data.categories()
    return '\n'.join([x for x in cat_dict]) if cat_dict else 'Sorry, our store is empty'

def show_items(category):
    """show items in the category"""
    try:
        cat_dict = data.categories()
        if category in cat_dict:
            items_list = f'{category} contains:\n'
            for i in cat_dict[category]:
                items_list += f"{show_item(i)} \n"
            return items_list[:-1]
        else:
            raise NameError("There is no such category")
    except NameError as err:
        return str(err)
    except:
        return "Something went wrong"

@decorator
def show_cart():
    """show current user's cart"""
    cart = data.show_user(user_id)['cart']
    if cart:
        items_list = f'Your cart contains:\n'
        for k, v in cart.items():
            items_list += f"{show_item(k)} ----> QUANTITY {v} \n"
        return items_list[:-1]
    else:
        raise RuntimeError("your cart is empty")

@decorator
def show_user():
    """show all information about user, including cart and orders"""
    info = data.show_user(user_id)
    orders = data.show_orders(user_id)
    result = f"NAME: {info['name']} ADDRESS{info['address']} CART: {show_cart()}"
    if orders:
        orders = "\n".join([show_order(id) for id in orders])
        result +=  f"\n ORDERS: {orders}"
    else:
        result += f"You have no orders"
    return result

@decorator_validate_id
def show_order(order_id):
    """show current user's order"""
    cart = data.show_order(order_id)["cart"]
    if cart:
        items_list = f'ORDER ID {order_id}'
        for k, v in cart.items():
            items_list += f"{show_item(k)} QUANTITY {v}\n"
        return items_list
    else:
        return "The order is empty"

@decorator_validate_id
def to_cart(item_id):
    """put the item to the cart"""
    if data.get_item(item_id)["quantity"] > 0:
        data.to_cart(item_id, user_id)
        return f"{show_item(item_id)} \n has been added to yor cart"
    else:
        raise RuntimeError("This item is out of stock")

@decorator_validate_id
def from_cart(item_id):
    """remove the item from the cart"""
    data.from_cart(item_id, user_id)
    return f"{show_item(item_id)} \n has been removed from cart"

@decorator
def clear_cart():
    """clear user's cart"""
    data.clear_cart(user_id)
    return f"your cart has been cleared"

@decorator
def make_order():
    """make order using current cart"""
    global order_id
    cart = data.show_user(user_id)['cart']

    if cart:
        for k, v in cart.items():
            item_in_stock = data.get_item(k)["quantity"]
            if v > item_in_stock:
                raise RuntimeError(
                    f"There is a problem with this one :/n{show_item(k)}/n There are only {item_in_stock} items in stock")
    else:
        raise RuntimeError("Your cart is empty")

    order_id = data.make_order(user_id)
    data.decrease(data.show_order(order_id)["cart"])
    data.clear_cart(user_id)
    return f"Your order {order_id} is being processed"

@decorator_validate_id
def select_order(id):
    """change current order"""
    global order_id
    if data.search_order(id):
        order_id = id
        return f"The order {order_id} has been selected/n" + show_order(order_id)
    else:
        raise NameError("order ID doesn't exist")

@decorator
def cancel_order():
    """cancel current order"""
    data.cancel_order(order_id)
    data.increase(data.show_order(order_id)["cart"])
    return f"The order {order_id} has been cancelled"