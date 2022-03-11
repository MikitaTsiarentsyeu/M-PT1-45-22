import bl


def show_all():
    return bl.get_all()


def show_category(category):
    return bl.get_category(category)


def show_basket():
    return bl.get_basket()


def get_value():
    return input(
        "---------------------------------------------------------------------------------------------\n"
        "Choose your action: \nдля добавления товара в корзину введите его имя!"
        "\n0. Exit\n1. Show all product\n2. Show category 'computers'  "
        "3. Show category 'tables'  4. Show category 'phones'\n5. Show basket \npay. Make an order \n| ")


def make_order():
    return bl.get_order()


def main_flow():
    while True:
        chosen_value = get_value()
        if chosen_value == '0':
            break
        elif chosen_value == '1':
            print(show_all())
        elif chosen_value == '2':
            category = "computers"
            print(show_category(category))
        elif chosen_value == '3':
            category = "tables"
            print(show_category(category))
        elif chosen_value == '4':
            category = "phones"
            print(show_category(category))
        elif chosen_value == '5':
            print(show_basket())
        elif chosen_value in bl.data.data_base:
            bl.del_data(chosen_value)
        elif chosen_value == 'pay':
            print(make_order())
