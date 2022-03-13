import  bl

def main_flow():
    "Show main menu of catalog"
    while True:
        show_dummy()
        choosen_value = get_value('Choose your action:\n0. Exit.\n1. Show all products.\n2. Show sales items.\n3. Show items by rating.\n4. Show items in specified category.\n5. Show items in basket.\n', end='')
        if choosen_value == '0':
            break
        elif choosen_value == '1':
            show(choosen_value)
            basket_operations()
        elif choosen_value == '2': 
            show(choosen_value)
            basket_operations()
        elif choosen_value == '3':
            show(choosen_value)
            basket_operations()   
        elif choosen_value == '4':
            choose_category()           
        elif choosen_value == '5':
            show_basket(choosen_value)
            show_dummy()
            basket_operations()
        else:
            show_message('Input correct value!')       
          
def show_message(message):
    """Print message with dummy"""
    show_dummy()
    print(message)
    
def show_dummy():
    """Print dummy message"""
    print('--------------------------------')    
    
def get_value(message, end=":\n"):
    """Return symbol from input string
    
    Returns:
        string"""
    return input(message + end)
def show(val):
    """Shows items all/ on sale/ by rating"""
    if val  == '1' or val == '2' or val == '3':
        show_message(bl.get(val))
            
def choose_category():
    """Show menu to choose category of catalog items and shows these category items"""
    while True:
        show_message(f'Choose your action:\n0. Back to menu.\n{bl.get_category_list()}')
        choosen_value_category = get_value('',end='')
        try:
            if  choosen_value_category == '0':
                break
            elif  choosen_value_category != '0':
                category = bl.get_category(int(choosen_value_category))
                if category:
                    category_items = bl.get('4', category)
                    show_message(category_items)
                    basket_operations()
                elif not category:
                    show_message('Input correct value!')
        except: 
            show_message('OOOPS! Something went wrong')

def basket_operations():
    """Show menu for basket operations"""
    while True:
        show_dummy()
        choose_place_order = get_value('Choose your action:\n0. Back to menu.\n1. Show items in basket.\n2. Add products to basket.\n3. Delete items from basket.\n4. Place order.\n',end='')
        try:
            if  choose_place_order == '0':
                break
            elif  choose_place_order == '1':
                show_basket('basket_view')
            elif  choose_place_order == '2' or choose_place_order == '3':
                add_delete_goods(choose_place_order)
            elif  choose_place_order == '4':
                place_order()
                break
            else:
                show_message('Input correct value!')                 
        except: 
            show_message('OOOPS! Something went wrong')
                
def add_delete_goods(val):
    """Shows menu for addition/deletetion item to basket and add/remove this item to/from basket"""
    show_dummy()
    try:
        pr_code = int(get_value('Choose product code'))
        pcs = int(get_value("How much you want?", end='\n'))
        moving = bl.add_remove_to_basket(pr_code, pcs, val)
        if moving:
            show_message("Succesfully added item" if val == '2' else "Succesfully removed item")
        elif not moving:
            show_message('Input correct values!')
    except:
       show_message('OOOPS! Something went wrong') 
           
def show_basket(val):
    """Show current user basket and total amount of goods"""
    show_message(bl.get(val))
    show_message(f'Total amount for items in basket: {bl.get_basket_price()} $')

def place_order():
    """Decrease quantity of items from catalog and remove all items in basket"""
    try:
        if bl.buy():
            show_message('Order sucesefully placed!')
        else:
            show_message('OOOPS! Basket is empty!')
    except:
        show_message('OOOPS! Something went wrong') 