products = {
# id - product code
# 0 - name
# 1 - categories
# 2 - price
# 3 - count
# 4 - rating
# 5 - product_key (int)
# 6 - count_of_rate
# [product_name(string), ['some_category_1'(string), 'some_category_2'(string)](choose_from_category_list) , price_in_dollars(int), count(int), rating(float), product_code(int), count_of_rate(int)],
    1 : ['Sneakers', ['Shoes', 'Sport'], 35, 8, 9.0, 1, 1],
    2 : ['Keyboard', ['Electronics', 'Computers & Accessories'], 10, 4, 7.6, 2, 1],
    3 : ['Mouse', ['Electronics', 'Computers & Accessories'], 5, 15, 8.4, 3, 1],
    4 : ['Headsets', ['Electronics', 'Computers & Accessories', 'Music'], 15, 1, 7.0, 4, 1],
    5 : ['Sandals', ['Shoes'], 15, 6, 10.0, 5, 1],
    6 : ['Garry Potter', ['Books'], 10, 2, 9.2, 6, 1],
    7 : ['Hungry games', ['Books'], 10, 0, 8.7, 7, 1],
    8 : ['Gaming laptop', ['Electronics', 'Computers & Accessories', 'Laptop'], 1999, 3, 8.7, 8, 1], 
    9 : ['Robot Vacuum', ['Vacuums'], 130, 5, 6.6, 9, 1],
    10 : ['Vacuum Cleaner', ['Vacuums'], 99, 1, 8.1, 10, 1],
}

category = {
    1 : 'Shoes',
    2 : 'Sport',
    3 : 'Electronics', 
    4 : 'Computers & Accessories',
    5 : 'Music', 
    6 : 'Books',
    7 : 'Vacuums'
}

basket = {}

def get_all(): 
    return products.values()

def get_all_category(): 
    return category

def get_one_category(key):
    choosen_category = category[int(key)]
    choosen_products = filter(lambda x: choosen_category in x[1], products.values())
    return choosen_products

def add_to_basket(key_product, count): 
        try:
            if basket.get(key_product):
                basket[key_product][3] += count
            else:
                basket[key_product] = products[key_product].copy()
                basket[key_product][3] = count
            return True
        except:
            return False

def get_name(key_product):
    return products[key_product][0]

def get_basket():
    return basket.values()

def update_count(key_product, count):
    if products[key_product][3] - count < 0:
        return False
    products[key_product][3] -= count
    return True

def delete_from_basket(key_product,count):
    if basket[key_product][3] - count <= 0:
        basket.pop(key_product,count)
        return False
    basket[key_product][3] -= count
    update_count(key_product, -count)
    return True

def get_total_price():
    total_price = 0
    for x in basket.values():
        total_price += x[2]*x[3]
    return total_price

def buy():
    global basket 
    basket = {}

def update_rate(key_product, rate):
    products[key_product][6] += 1
    new_rate =products[key_product][4] = (products[key_product][4] * products[key_product][6] + rate) / (products[key_product][6])
    return new_rate
