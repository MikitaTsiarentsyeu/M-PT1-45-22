# catalog_dict = {id : [name, [category], product_code, price, stock, rating, sale]}
catalog_dict = {1 : ["T-short", ["Wear", "Sports"], 991, 99.95, 5, 5.8, False],
                2 : ["Nike shoes", ["Shoes", "Sports"], 992, 89.70, 2, 8.8, False],
                3 : ["Keyboard Asus Strix", ["Computer", "Electronics"], 91, 60.00, 5, 9.8, False],
                4 : ["Videocard Asus 3090 TI", ["Computer", "Electronics"], 15, 25.50, 4, 7.5, True],
                5 : ["Smart watch Apple Series 5", ["Accessoires", "Electronics"], 425, 152.15, 9, 9.8, False],
                6 : ["Iphone 13 Pro", ["Smartphones", "Electronics"], 48, 252.15, 15, 6.0, True],
                7 : ["Sauron ring", ["Jewelry"], 1, 99999.99, 1, 10.0, True],
                8 : ["Dark Souls 3", ["Games", "Electronics"], 51, 99.99, 10, 2.5, False]}

category_dict = {1 :"Wear",
                 2: "Sports",
                 3: "Shoes",
                 4: "Computer", 
                 5: "Electronics",
                 6: "Accessoires",
                 7: "Smartphones",
                 8: "Jewelry",
                 9: "Games"}

basket_dict = {}

def view(basket=None):
    """Return values from catalog or basket"""
    if not basket:
        return catalog_dict.values()
    if basket:
        return basket_dict.values()
    
def categories_view():
    """Return categories from catalog"""
    return category_dict.items()

def category_items(choosen_category):
    """Return items that belongs to choosen category"""
    if choosen_category in category_dict:
        return category_dict[choosen_category]
    else:
        return False

def buy_items():
    """Return empty basket and decreased quantity of items in catalog"""
    global catalog_dict, basket_dict
    if basket_dict == {}:
        return False
    for y,z in catalog_dict.copy().items():
        for x in basket_dict.values():
            if z[0] == x[0]:
                z[4] -= x[4]
                if z[4] == 0:
                    del catalog_dict[y]
    basket_dict = {}
    return catalog_dict

def basket_add_delete(pr_code, pcs, add=True): #todo better solution
    """Delete or add elemets to the basket"""
    global basket_dict
    flag1, flag2 = False, False
    for x,y in catalog_dict.items():
        if pr_code == y[2]:
            flag1 = True
            if add: #adding element
                if y[4] >= pcs and pcs != 0:
                    basket_dict[x] = catalog_dict[x].copy()
                    basket_dict[x][4] = pcs  
                    flag2 = True
                else:
                    if y[4] < pcs or pcs == 0:
                        return False
            elif not add: #delete element
                if y[4] > pcs:
                    basket_dict[x][4] -= pcs
                    flag2 = True  
                elif y[4] == pcs:
                    del basket_dict[x]
                    flag2 = True  
                elif y[4] < pcs:
                    return False
    if not flag1 or not flag2:
        return False
    return True