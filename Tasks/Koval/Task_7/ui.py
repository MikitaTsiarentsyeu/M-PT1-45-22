import bl

def user_input_check(message):
    if not message.isdigit():
        print('Please text a number!')
        return False
    return True

def show_message(message):
    print ('***************************************************************')
    print(message)
    print ('***************************************************************')

def get_value(message, end=":\n"):
    flag = False
    while flag == False:
        out_message = input(message + end)
        flag = user_input_check(out_message)
    return int(out_message)

def show_all():
    show_message(bl.get_all())

def choose_category():
    show_message(bl.get_all_category())
    key_category = get_value('Choose category')
    show_message(bl.get_one_category(key_category))

def add_to_basket():
    key_product = get_value('Choose product key')
    count = get_value("How much you want?", end='\n')
    show_message(bl.add_to_basket(key_product, count))

def show_basket():
    basket = bl.get_basket()
    show_message(basket)
    if basket != 'Your basket is empty!':
        return True
    return False
    
def buy():
    show_message(bl.buy())

def delete_from_basket():
    key_product = get_value('Choose product key')
    count = get_value("How much you want to delete?", end='\n')
    show_message(bl.delete_from_basket(key_product, count))

def view_total_price():
    show_message(bl.get_total_price())

def rate():
    key_product = get_value('Choose product key')
    user_rate = get_value('Your rate')
    show_message(bl.update_rate(key_product, user_rate))

def main_flow():
    while True:
        choosen_value = get_value("Choose your action:\n0. Exit\n1. Show all products;\n2. Choose category;\n3. Add some product to basket;\n4. Show basket;\n...\n...\n...\n9. Rate any product.\n", end='')
        if choosen_value == 0:
            break
        elif choosen_value == 1:
            show_all()
        elif choosen_value == 2:
            choose_category()
            while True:
                choosen_value_on_category = get_value('Choose your action:\n0. Back to menu;\n1. See another category.\n',end='')
                if  choosen_value_on_category == 0:
                    break
                elif  choosen_value_on_category == 1:
                    choose_category()
                else:
                    show_message('Input true value!')
        elif choosen_value == 3:
            add_to_basket()
        elif choosen_value == 4:
            while True:
                if not show_basket():
                    break
                choosen_value_on_basket = get_value("Choose your action:\n0. Back to menu;\n1. Buy;\n2. View total price;\n3. Delete some product.\n", end='')
                if  choosen_value_on_basket == 0:
                    break
                elif  choosen_value_on_basket == 1:
                    buy()
                elif  choosen_value_on_basket == 2:
                    view_total_price()
                elif  choosen_value_on_basket == 3:
                    delete_from_basket()
                else:
                    show_message('Input true value!')
        elif choosen_value == 9:
            rate()
        else:
            show_message('Input true value!')
