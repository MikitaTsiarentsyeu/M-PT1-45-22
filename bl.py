import data


def get_categories():
    res = data.get_categories()
    categ_from_catal = "\n".join([f"{x}" for x in res])
    return f"This are categories from our catalogue:\n{categ_from_catal}"


def get_products(chosen_category):
    try:
        res = data.get_products(chosen_category)
        prod_from_categ = "\n".join([f"{x}: product key = {res[x][0]}, price = {res[x][1]}, quantity = {res[x][2]}" for x in res])
        return f"This are products from category {chosen_category}:\n{prod_from_categ}"
    except NameError as err:
        return str(err)


def get_basket():
    if not data.get_basket():
        return "Your basket is empty"
    else:
        res = data.get_basket()
        prod_in_basket = "\n".join([f"{x}: total price = {res[x][0]}, quantity = {res[x][1]}" for x in res])
        return f"Your basket:\n{prod_in_basket}"


def add_to_basket(chosen_category, chosen_product, chosen_quantity):
    try:
        chos_qant_valid(chosen_quantity)
    except ValueError:
        return "The quantity must consist of digits"
    except RuntimeError as err:
        return str(err)
    try:
        data.add_to_basket(chosen_category, chosen_product, chosen_quantity)
        return "The product was added to your basket"
    except NameError as err:
        return str(err)
    except RuntimeError as err:
        return str(err)


def remove_from_basket(chosen_product, chosen_quantity):
    try:
        chos_qant_valid(chosen_quantity)
    except ValueError:
        return "The quantity must consist of digits"
    except RuntimeError as err:
        return str(err)
    try:
        data.remove_from_basket(chosen_product, chosen_quantity)
        return "The product was removed from your basket"
    except NameError as err:
        return str(err)
    except RuntimeError as err:
        return str(err)


def final_buy():
    try:
        data.final_buy()
        return "Your purchase is complete"
    except RuntimeError as err:
        return str(err)


def chos_qant_valid(n):
    n = int(n)
    if n <= 0:
        raise RuntimeError("The quantity must be positive value")
