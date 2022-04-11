#items dict {item_ID: information}
repo_items = { '1' : {"category": "category 1",
                    "name" : "item name 1",
                    "price" : 100500,
                    "quantity" : 3},
            '2' : {"category" : " category 1",
                    "name" : "item name 2",
                    "price" : 100,
                    "quantity" : 33},
            '3' : {"category" : " category 2",
                    "name" : "item name 3",
                    "price" : 500,
                    "quantity" : 1},
            }
# users dict {user_ID: information}
repo_users = { '1' : {"name" : "Ivan",
                    "address" : "address x",
                    "cart" : {} },
            '2' : {"name" : "Petr",
                    "address" : "address y",
                    "cart" : {1:2} }, #cart {item_id:qauntity}
            '3' : {"name" : "Olga",
                    "address" : "address o",
                    "cart" : {2:1, 3:1} }
               }
#  orders dict {order_ID: information}
repo_orders = {'1' : {"user_id" : 3, #user ID
                    "cart" : {1:1, 2:1} , #cart {item_id:quantity}
                    "payed" : False, #payed
                    "status" : 0} #status: -1 canceled, +1 delivered, 0 processing
                }

def search_user(user_id):
    """confirm user exists"""
    return (user_id in repo_users)

def search_order(order_id):
    """confirm order exists"""
    return (order_id in repo_orders)

def register_user():
    """generate user ID"""
    user_id = str(len(repo_users)+2)
    repo_users[user_id] = {'name':'unknown', 'address':'unknown', 'cart':{}}
    return user_id

def categories():
    """return dict {category:[items]}"""
    cat_items = {}
    for k,v in repo_items.items():
        if v["category"] in cat_items:
            cat_items[v["category"]].append(k)
        else:
            cat_items[v["category"]] = [k]
    return cat_items

def get_item(id):
    return repo_items[id]
    raise NameError("the item with such ID was not found")

def show_user(user_id):
    return repo_users[user_id]
    raise NameError("the user with such ID was not found")

def to_cart(item_id, user_id):
    """add the item to the cart"""
    if item_id in  repo_users[user_id]['cart']:
        repo_users[user_id]['cart'][item_id] += 1
    else:
        repo_users[user_id]['cart'][item_id] = 1
    return True
    raise NameError("such ID was not found")

def from_cart(item_id, user_id):
    """remove the item from the cart"""
    if repo_users[user_id]['cart'][item_id] == 1:
        del repo_users[user_id]['cart'][item_id]
    else:
        repo_users[user_id]['cart'][item_id] -= 1
    return True
    raise NameError("such ID was not found")

def clear_cart(user_id):
    repo_users[user_id]['cart'] = {}
    return True
    raise NameError("the user with such ID was not found")

def show_order(order_id):
    return repo_orders[order_id]
    raise NameError("the order with such ID was not found")

def show_orders(user_id):
    """return ser's orders"""
    return [k for k,v in repo_orders.items() if v["user_id"]==user_id]

def make_order(user_id):
    order_id = str(len(repo_orders) + 2)
    repo_orders[order_id] = {"user_id":user_id, "cart":repo_users[user_id]["cart"], "payed":False, "status":0}
    return order_id
    raise NameError("the user with such ID was not found")

def cancel_order(order_id):
    repo_orders[order_id]["status"] = -1
    return True
    raise NameError("the order with such ID was not found")

def decrease(cart):
    """move goods from stock"""
    for k, v in cart.items():
        repo_items[k]["quantity"] -= v

def increase(cart):
    """move goods back to stock - if order has been cancelled"""
    for k, v in cart.items():
        repo_items[k]["quantity"] += v