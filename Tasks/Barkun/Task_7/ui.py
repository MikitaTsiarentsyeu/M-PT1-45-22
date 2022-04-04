import bl
import sys

def show_query (message):
    return input(message)

def show_all_category():
    data = bl.get_all_category()

def show_category(category):
    print (f'\n*************  CATEGORY: {category}  ******************\n')
    data = bl.get_category(category)

def show_product (selection_product, quantity_product):
    data = bl.get_product(selection_product, quantity_product)

def continue_execution ():
     while True:
        cont_execution = show_query("""
    Eсли хотите продолжить выбор введите "yes"
    Если хотите закончить выбор и оплатить введите  "buy"
    Если вы передумали, что-нибудь покупать и хотите выйти введите  "ex"
    Сделайте свой выбор:   """)
        if cont_execution == 'yes':
            main_flow()
        elif cont_execution == 'buy':
            buy_product()
        elif cont_execution == 'no':
            sys.exit()
        print (f'\nВы ввели {cont_execution}\nЭто неправильно!!!\nПовторите пожалуйста ввод.\n')

def continue_selection():
     while True:
        cont_execution = show_query("""
    Eсли хотите продолжить выбор введите "yes"
    Если вы передумали, что-нибудь покупать и хотите выйти введите  "ex"
    Сделайте свой выбор:   """)
        if cont_execution == 'yes':
            main_flow()
        elif cont_execution == 'no':
            sys.exit()
        print (f'\nВы ввели {cont_execution}\nЭто неправильно!!!\nПовторите пожалуйста ввод.\n')   


def main_flow():
    while True:
        choose_category = show_query("""
        Введите номер категории, которую вы хотите просмотреть:\n 
        Если хотите посмотреть все категории введите "0"\n
        Если хотите посмотреть категорию "Whisky" введите "1"\n
        Если хотите посмотреть категорию "Cognac" введите "2"\n
        Если хотите посмотреть категорию "'Wine" введите "3"\n
        Если хотите выйти из программы введите "ex" \n
        Сделайте свой выбор:  """)
        if choose_category == '0':
            show_all_category()
        if choose_category == '1':
            category = 'Whisky'
        elif choose_category == '2':
            category = 'Cognac'
        elif choose_category == '3':
            category = 'Wine'
        elif choose_category == 'ex':
            sys.exit()
        try:
            show_category(category)
        except UnboundLocalError:
             print (f'Вы ввели {choose_category}\nЭто неправильно!!!\nПовторите пожалуйста ввод.\n')


def product_selection():
    selection_product = show_query("""Если вы хотите выбрать товар из этой категории, введите пожалуйста после ":" наименование товара\n : """)
    quantity_product = show_query("""Введите пожалуйста после ":" количество товара\n : """)
    show_product(selection_product, quantity_product)
    
def put_basket(basket):
    a = True
    while a:
        to_put_basket = show_query ("""
        Положить выбранный товар в корзину?
        Если да, то введите "yes":
        Если не хотите ложить в корзину, но хотите продолжить выбор введите "ok":
        Если хотите закончить программу, введите "ex"
        Сделайте свой выбор:  """)
        if to_put_basket == 'yes':
            bl.get_basket(basket)
            a = False
        elif to_put_basket == 'ok':
            main_flow()
            a = False
        elif to_put_basket == 'ex':
            sys.exit()
        else:
            print (f'\nВы ввели { to_put_basket}\nЭто неправильно!!!\nПовторите пожалуйста ввод.\n')


def buy_product():
    print (f"\nСпасибо за покупку!!!\n")
    sys.exit()
