import data_base

def get_all():
    return '\n'.join(f"Categoty - {x[0]}: {x[1]},  id: {x[2]},  price: {x[3]} $,  in stock: {x[4]}" for x in data_base.get_all())

def get_category():
    return '\n'.join(set([x[0] for x in data_base.get_all()]))     

def get_item_category(choosen_value):
    return '\n'.join(f"{x[1]} - id: {x[2]},  price: {x[3]} $,  in stock: {x[4]}" for x in data_base.get_all() if choosen_value in x[0]) 

def add_cart(id, count):
    try:
        validate(id, count)
    except ValueError:
        return "The values must be digits"
    try:
        data_base.add_cart(id, count)
        return "Product successfully added to cart"
    except RuntimeError as err:
        return str(err)
    except NameError as err:
        return str(err)
    except:
        return "Something went wrong"
        
def show_cart():
    try:
        data_base.show_cart()
        return '\n'.join([f"{x[0]} (id: {x[1]}), quantity: {x[2]}, price: {x[3]} $, in stock: {x[4]}" for x in data_base.show_cart()])
    except RuntimeError as err:
        return str(err)

def make_order():
    try:
        data_base.make_order()
        return (f"Your order has been approved.\nTo pay: {data_base.make_order()} $")
    except RuntimeError as err:
        return str(err)

def validate(id, count):
    id = int(id)
    count = int(count)
