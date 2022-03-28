import episode_data

def get_all_1():
    try:
        product = episode_data.get_all_1()
        list_product = " < Available products in the store > \n"
        for x in product:
            list_product += f"Product: {x[0]}; price - {x[1]}$; In stock:{x[2]}; Product code:({x[3]}). \n"
        return list_product
    except:
        return "<\nError!> Try again.\n"

'''get_all_2 = factory(episode_data.get_all_2) and it was possible to write with the help of a factory?'''

def get_all_2():
    try:
        product = episode_data.get_all_2()
        list_product = " < Available products in the store > \n"
        for x in product:
            list_product += f"Product: {x[0]}; price - {x[1]}$; In stock:{x[2]}; Product code:({x[3]})."'\n'
        return list_product
    except:
        return "<\nError!> Try again.\n"


def get_all_3():
    try:
        product = episode_data.get_all_3()
        list_product = "< Available products in the store >\n"
        for x in product:
            list_product += f"Product: {x[0]}; price - {x[1]}$; In stock:{x[2]}; Product code:({x[3]})."'\n'
        return list_product
    except:
        return "<\nError!> Try again.\n"


def get_all_4():
    try:
        product = episode_data.get_all_4()
        list_product = "< Available products in the store >\n"
        for x in product:
            list_product += f"Product: {x[0]}; price - {x[1]}$; In stock:{x[2]}; Product code:({x[3]})."'\n'
        return list_product
    except:
        return "<\nError!> Try again.\n"


def add_basket_1(product_code):
    try:
        if episode_data.add_basket_1(product_code):
            return "Your product has been added to your basket!\n"
        else:
            return "<\nError!> Try again.\n"
    except ValueError:
        return "Sorry, this code is invalid.\n"


def add_basket_2(product_code):
    try:
        if episode_data.add_basket_2(product_code):
            return "Your product has been added to your basket!\n"
        else:
            return "<\nError!> Try again.\n"
    except ValueError:
        return "Sorry, this code is invalid.\n"

def add_basket_3(product_code):
    try:
        if episode_data.add_basket_3(product_code):
            return "Your product has been added to your basket!\n"
        else:
            return "<\nError!> Try again.\n"
    except ValueError:
        return "Sorry, this code is invalid.\n"

def add_basket_4(product_code):
    try:
        if episode_data.add_basket_4(product_code):
            return "Your product has been added to your basket!\n"
        else:
            return "<\nError!> Try again.\n"
    except ValueError:
        return "Sorry, this code is invalid.\n"


def show_basket():
    product = episode_data.show_basket()
    total_sum = 0
    if not product:
        return "\nYour basket is empty.\n"
    else:
        list_product = "Your basket:\n"
        for x in product:
            list_product += f"Product: {x[0]}; price - {x[1]}$ \n"
            total_sum += int(x[1])
        list_product += f"Total price: {total_sum}$\n"
        return list_product

def buy():
    try:
        basket = episode_data.buy()
        total = 0
        for x in basket:
            total += int(x[1])
        episode_data.basket = []
        return f" You paid:{total}$. \n Thank you for your purchase!.\n"
    except RuntimeError:
        return "\n<Error!>\nSorry, your basket empty.\n"
