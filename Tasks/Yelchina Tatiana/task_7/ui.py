import bl

def show_message(message):
    print('*-------*-------*-------*-------*------*------*------*------*------*')
    print(message)
    print('*-------*-------*-------*-------*------*------*------*------*------*')

def get_value(message, end=":\n"):
    return input(message + end)

def show_all():
    show_message(bl.get_all())

def show_category():
    show_message(bl.get_category())
    choosen_value = input("Enter category: ") 
    show_message(bl.get_item_category(choosen_value))

def add_cart(): 
    id = get_value("Enter an item id")
    count  = get_value("Enter a count of item")
    show_message(bl.add_cart(id, count))

def show_cart():
    print('Items in the cart:') 
    show_message(bl.show_cart())

def make_order(): 
    show_message(bl.make_order())

def main_flow():
    while True:
        choosen_value = get_value("Select your action:\n0. Exit\n1. Show all items\n2. Select category show items\n3. Add item to cart\n4. Show a cart\n5. Make an order\n", end='')
        if choosen_value == '0':
            break
        elif choosen_value == '1':
            show_all()
        elif choosen_value == '2':
            show_category()
        elif choosen_value == '3':
            add_cart()
        elif choosen_value == '4':
            show_cart()
        elif choosen_value == '5':
            make_order()