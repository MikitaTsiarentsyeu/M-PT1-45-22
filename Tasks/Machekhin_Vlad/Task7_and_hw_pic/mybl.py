import mydata

def get_all_category():
    res = mydata.get_category()
    cor_categ = "\n".join([f'{x}' for x in res])
    return f"The product categories are displayed below:\n{cor_categ}"

def get_product(selected_category):
    try:
        res = mydata.get_product(selected_category)
        prod_from_categ = "\n".join([f"{x}: barcode = {res[x][0]}, price = {res[x][1]}, quantity = {res[x][2]}" for x in res])
        return f"This are products from category {selected_category}:\n{prod_from_categ}"
    except NameError as err:
        return str(err)


def add_to_basket(selected_category, selected_product, selected_quantity):
    try:
        validation(selected_quantity)
    except ValueError:
        return "The quantity must consist of digits"
    except RuntimeError as err:
        return str(err)
    try:
        mydata.add_to_basket(selected_category, selected_product, selected_quantity)
        return "The product was added to your basket"
    except NameError as err:
        return str(err)
    except RuntimeError as err:
        return str(err)


def final_buy():
    try:
        mydata.final_buy()
        return "Your purchase is complete"
    except RuntimeError as err:
        return str(err)

        
def validation(n):
    n = int(n)
    if n <= 0:
        raise RuntimeError("The quantity must be positive value")
