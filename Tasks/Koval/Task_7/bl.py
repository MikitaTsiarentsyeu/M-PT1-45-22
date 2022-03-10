import data

def beatifull_showing(products):
     return '\n'.join([f"{x[5]}. {x[0]} - {x[2]}$, {x[3]} in stock, rating - {x[4]} categories - {', '.join(x[1])} " for x in products])

def get_all():
    return beatifull_showing(data.get_all())

def get_all_category():
    return '\n'.join([f'{key} - {value}' for key, value in data.get_all_category().items()])

def get_one_category(key):
    answer = data.get_one_category(key)
    if answer:
        return beatifull_showing(answer)
    return 'You selected unexists category. Please try again!'

def add_to_basket(key_product, count):
    if not data.update_count(key_product, count):
        return 'Wrong item count!'
    if data.add_to_basket(key_product, count):
        return f'{data.get_name(key_product)} add to you basket.'
    return 'Wrong product code!'

def delete_from_basket(key_product, count): 
    if data.delete_from_basket(key_product, count):
        return 'Success!'
    return f'{data.get_name(key_product)} full delete from your basket!'

def get_basket(): 
    basket = data.get_basket()
    if basket:
        return  beatifull_showing(basket)
    return 'Your basket is empty!'    

def get_total_price():
    return f'Total price is {data.get_total_price()}$'

def buy(): 
    total = data.get_total_price()
    data.buy()
    return f'Thank you for your purchase. You paid - {total}$'

def update_rate(key_product, rate):
    new_rate = data.update_rate(key_product, rate)
    return f'Thanks for you rate. New rate of {data.get_name(key_product)} is {new_rate}'