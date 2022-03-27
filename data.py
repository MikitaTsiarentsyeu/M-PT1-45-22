# category: product: product code, price, quantity

catalogue = \
{
    'electronics':
    {
        'laptops': [111, 499.9, 100], 'tablets': [112, 399.9, 250],
        'smartphones': [113, 699.9, 600], 'gaming pc': [114, 899.9, 120]
     },
    'furniture':
    {
        'beds': [211, 199.9, 310], 'chairs': [212, 49.9, 550], 'tables': [213, 99.9, 480],
    },
    'clothing & shoes':
    {
        't-shirts': [311, 39.9, 1100], 'shirts': [312, 69.9, 1000],
        'sneakers': [313, 149.9, 450], 'hoodies': [314, 99.9, 750],
        'jackets': [315, 129.9, 600],
    },
    'music':
    {
        'guitars': [411, 499.9, 320], 'drums': [412, 899.9, 150],
        'keyboards': [413, 599.9, 200], 'dj equipment': [414, 349.9, 100]
    }
}

basket = {}


def get_categories():
    return catalogue.keys()


def get_products(chosen_category):
    for category in catalogue.keys():
        if category == chosen_category:
            return catalogue.get(chosen_category)
    raise NameError("There is no such category in our catalogue")


def get_basket():
    return basket


def add_to_basket(chosen_category, chosen_product, chosen_quantity):
    if chosen_category in catalogue.keys():
        if chosen_product in catalogue.get(chosen_category):
            if catalogue.get(chosen_category).get(chosen_product)[2] >= int(chosen_quantity):
                price = catalogue.get(chosen_category).get(chosen_product)[1]
                if chosen_product not in basket:
                    basket[chosen_product] = [price*int(chosen_quantity), int(chosen_quantity)]
                else:
                    basket[chosen_product][0] += price
                    basket[chosen_product][1] += int(chosen_quantity)
                return True
            else:
                raise RuntimeError(f"Only {catalogue.get(chosen_category).get(chosen_product)[2]} products left")
        else:
            raise NameError("There is no such product in our catalogue")
    else:
        raise NameError("There is no such category in our catalogue")


def remove_from_basket(chosen_product, chosen_quantity):
    if not basket:
        raise RuntimeError("Your basket is empty")
    else:
        if chosen_product in basket:
            if int(chosen_quantity) <= basket[chosen_product][1]:
                if int(chosen_quantity) == basket[chosen_product][1]:
                    del basket[chosen_product]
                else:
                    price = basket[chosen_product][0]-basket[chosen_product][0]/basket[chosen_product][1]*int(chosen_quantity)
                    basket[chosen_product] = [price, int(chosen_quantity)]
                return True
            else:
                raise RuntimeError("You cannot remove more products than you have in your basket")
        else:
            raise NameError("There is no such product in your basket")


def final_buy():
    global basket
    if not basket:
        raise RuntimeError("Your basket is empty")
    else:
        for product in basket.keys():
            for value in catalogue.values():
                if product in value:
                    value[product][2] -= basket[product][1]
        basket.clear()
        return True
