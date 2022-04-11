import mybl

def main_flow():
    while True:
        choosen_value = get_value("Choose your action:\n0. Exit\n1. Show all category\n2. Show a product of a specific category\n3. Ordering\n", end='')
        if choosen_value == '0':
            break
        elif choosen_value == '1':
            show_all_category()
        elif choosen_value == '2':
            x = get_value('Show product of a specific category')
            get_product(x)
        elif choosen_value == '3':
             while True:
                chosen_value = get_value("Choose your action:\n0. Exit\n1. Add to basket\n2. Buy\n", end="")
                if chosen_value == "0":
                    break
                elif chosen_value == "1":
                    add_to_basket()
                elif chosen_value == "2":
                    final_buy()




def show_message(message):
    print(message)

def get_value(message, end=":\n"):
    return input(message + end)

def show_all_category():
    show_message(mybl.get_all_category())

def get_product(x):
    show_message(mybl.get_product(x))


def add_to_basket():
    chosen_category = get_value("Select the category that interests you")
    chosen_product = get_value("Select the item you want to add to the basket")
    chosen_quantity = get_value("Select the quantity of the item")

    res = mybl.add_to_basket(chosen_category, chosen_product, chosen_quantity)
    show_message(res)

def final_buy():
    itog = mybl.final_buy()
    show_message(itog)



      
# print(main_flow())

