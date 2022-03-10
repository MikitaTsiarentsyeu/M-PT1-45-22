import bl


def factory(func):
    """Factory to print functions responses."""
    print(func)


def show_products():
    category = input("Please submit a category:")
    print(bl.category_show(category))


def add_product():
    code = input("Please input the item code:")
    print(bl.add_product(code))


def main_flow():
    while True:
        customer_response = input("Choose an action: \n 1 - Show all \n 2 - Show by category \n 3 - Add product to "
                                  "shopping cart \n 4 - Checkout \n 5 - Show shopping cart\n 0 - Exit \n")
        if customer_response == "0":
            break
        if customer_response == "1":
            factory(bl.show_all())
        if customer_response == "2":
            show_products()
        if customer_response == "3":
            add_product()
        if customer_response == "4":
            factory(bl.place_order())
        if customer_response == "5":
            factory(bl.shopping_card())


if __name__ == '__main__':
    main_flow()
