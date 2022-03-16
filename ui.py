import bl


def show_message(message):
    print(message + ".")


def get_value(message, end=":\n"):
    return input(message + end)


def show_categories():
    print(bl.get_categories())


def show_products():
    chosen_category = get_value("Enter the category you are interested in")
    print(bl.get_products(chosen_category))


def show_basket():
    print(bl.get_basket())


def add_to_basket():
    chosen_category = get_value("Enter the category you are interested in")
    chosen_product = get_value("Enter the product you want to add to basket")
    chosen_quantity = get_value("Enter the quantity of products you want to add to basket")
    res = bl.add_to_basket(chosen_category, chosen_product, chosen_quantity)
    show_message(res)


def remove_from_basket():
    chosen_product = get_value("Enter the product you want to remove from basket")
    chosen_quantity = get_value("Enter the quantity of products you want to remove from basket")
    res = bl.remove_from_basket(chosen_product, chosen_quantity)
    show_message(res)


def final_buy():
    res = bl.final_buy()
    show_message(res)


def main_flow():
    while True:
        chosen_value = get_value("Choose your action:\n0. Exit\n1. Show categories\n"
                                 "2. Show products from category\n3. Make an order\n", end="")
        if chosen_value == "0":
            break
        elif chosen_value == "1":
            show_categories()
        elif chosen_value == "2":
            show_categories()
            show_products()
        elif chosen_value == "3":
            while True:
                chosen_value = get_value("Choose your action:\n0. Exit\n1. Add to basket\n"
                                         "2. Remove from basket\n3. Show basket\n4. Buy\n", end="")
                if chosen_value == "0":
                    break
                elif chosen_value == "1":
                    add_to_basket()
                elif chosen_value == "2":
                    remove_from_basket()
                elif chosen_value == "3":
                    show_basket()
                elif chosen_value == "4":
                    final_buy()
