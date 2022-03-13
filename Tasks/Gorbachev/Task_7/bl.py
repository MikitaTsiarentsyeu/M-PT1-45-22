import data
from decimal import Decimal

def format(catalog_dict, sale=False, category=None): #todo better solution
    """Return formatted data from catalog"""
    catalog = ''
    #catalog_dict = {id : [name, [category], product_code, price, stock, rating, sale]}
    if not sale:
        catalog += ''.join([(f"{x[2]} product code. {x[0]} - price {x[3]}$ is on SALE, {x[4]} pcs in stock, rating - {x[5]}. Categories - {', '.join(x[1])}\n" if x[6] else f"{x[2]} product code. {x[0]} - price {x[3]}$, {x[4]} pcs in stock, rating - {x[5]}. Categories - {', '.join(x[1])}\n") for x in catalog_dict])
    elif sale and category == None:
        catalog += ''.join([f"{x[2]} product code. {x[0]} - price {x[3]}$ is on SALE, {x[4]} pcs in stock, rating - {x[5]}. Categories - {', '.join(x[1])}\n" if x[6] else '' for x in catalog_dict])
    elif category != None:
        for x in catalog_dict:
            if category in x[1]:
                catalog += (f"{x[2]} product code. {x[0]} - price {x[3]}$ is on SALE, {x[4]} pcs in stock, rating - {x[5]}. Categories - {', '.join(x[1])}"+ '\n') if x[6] else (f"{x[2]} product code. {x[0]} - price {x[3]}$, {x[4]} pcs in stock, rating - {x[5]}. Categories - {', '.join(x[1])}"+ '\n')
    return catalog.removesuffix('\n')
 
def get(val, category=None):
    """Return formatted data from catalog in case if choosen sort"""
    if val == '1':
        return f'Catalog items \n{format(data.view(), False)}'
    elif val == '2':
        return f'On sale items\n{format(data.view(), True)}'
    elif val == '3':
        return f'Sorted by rating items\n{format(sorted(data.view(), key=lambda rating: rating[5]), False)}'
    elif val == '4':
        if not category:
            return False
        else:  
            return f'Items from category {category}\n{format(data.view(), True, category)}'
    elif val == '5' or val == 'basket_view':
        return f'Basket items\n{format(data.view(True), False)}'
    
def get_category(choosen_category):
    """Return mane of choosen category"""
    return data.category_items(choosen_category)

def show_category_list(category_list):
    """Return formatted list of categories to ui"""
    return '\n'.join(f"{x[0]}. {x[1]}" for x in category_list)

def get_category_list():
    """Return list of categories from data"""
    return show_category_list(data.categories_view())

def get_basket_price():
    """Return amount of items, placed in basket"""
    basket_amount = Decimal(0.0)
    basket_tmp = data.view(True)
    for x in basket_tmp:
        basket_amount += Decimal(x[3]*x[4])
    return basket_amount.quantize(Decimal('1.00'))

def buy():
    """Buy items from basket and decrease quantity in catalog"""
    return data.buy_items()

def add_remove_to_basket(pr_code, pcs, val):
    """Add or remove items from basket"""
    if val == '2':
        return data. basket_add_delete(pr_code, pcs, True)
    elif val == '3':
        return data. basket_add_delete(pr_code, pcs, False)
        
