import episode_bl

def show_goods(product):
    print(product)

def get_value(product, end="\n"):
    return input(product + end)

def buy():
    show_goods(episode_bl.buy())

def show_all_1():
    show_goods(episode_bl.get_all_1())

def show_all_2():
    show_goods(episode_bl.get_all_2())

def show_all_3():
    show_goods(episode_bl.get_all_3())

def show_all_4():
    show_goods(episode_bl.get_all_4())

def add_basket_1():
    product_code = input("Please enter a product code:")
    print(episode_bl.add_basket_1(product_code))
def add_basket_2():
    product_code = input("Please enter a product code:")
    print(episode_bl.add_basket_2(product_code))
def add_basket_3():
    product_code = input("Please enter a product code:")
    print(episode_bl.add_basket_3(product_code))
def add_basket_4():
    product_code = input("Please enter a product code:")
    print(episode_bl.add_basket_4(product_code))

def show_basket():
    show_goods(episode_bl.show_basket())


def main_flow():
    while True:
        choosen_value = get_value("    Sporting goods\n Catalog: "
        "\n1. Football goods.\n2. Hockey goods.\n3. Tennis goods.\n4. Other sporting goods.\n5. Buy product. "
                                  "\n6. Exit.\n", end='')
        if choosen_value == "1":
            show_all_1()
            while True:
                choosen_category = get_value(
                    ' Choose your action:\n 1.Сhoose a product;\n 2.Show basket;\n 3.Back to menu.\n', end='')
                if choosen_category == "1":
                    add_basket_1()
                elif choosen_category == "2":
                    show_basket()
                elif choosen_category == "3":
                    break
        elif choosen_value == "2":
            show_all_2()
            while True:
                choosen_category = get_value(
                    ' Choose your action:\n 1.Сhoose a product;\n 2.Show basket;\n 3.Back to menu.\n', end='')
                if choosen_category == "1":
                    add_basket_2()
                elif choosen_category == "2":
                    show_basket()
                elif choosen_category == "3":
                    break
        elif choosen_value == "3":
            show_all_3()
            while True:
                choosen_category = get_value(
                    ' Choose your action:\n 1.Сhoose a product;\n 2.Show basket;\n 3.Back to menu.\n', end='')
                if choosen_category == "1":
                    add_basket_3()
                elif choosen_category == "2":
                    show_basket()
                elif choosen_category == "3":
                    break
        elif choosen_value == "4":
            show_all_4()
            while True:
                choosen_category = get_value(
                    ' Choose your action:\n 1.Сhoose a product;\n 2.Show basket;\n 3.Back to menu.\n', end='')
                if choosen_category == "1":
                    add_basket_4()
                elif choosen_category == "2":
                    show_basket()
                elif choosen_category == "3":
                    break
        elif choosen_value == "5":
            buy()
        elif choosen_value == "6":
            break
