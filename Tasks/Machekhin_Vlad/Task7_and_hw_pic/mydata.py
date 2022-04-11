# Реализовать каталог товаров, основанный на шаблоне 3-х слойной архитектуры.
# Пользователь должен иметь возможность просматривать товары из определённой категории, добавлять определённое количество товаров в корзину и делать окончательный заказ.
# Минимальный набор характеристик товара: название, категория, товарный код, цена, (количество на складе).

catalogue = {'electronics' : {'television' : [8529909201, '2000 BYN', 200], 'fridge' : [8418102001, '2500 BYN', 100]}, 
        'pet products' :{'animal litter' : [3824999609, '10 BYN', 50], 'rat food' : [5410340613702, '8 BYN', 30]}}

basket = {}
def get_category():
    return catalogue.keys()

def get_product(selected_category):
    for category in catalogue.keys():
        if category == selected_category:
            return catalogue.get(selected_category)


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
            raise NameError("There is no such product")
    else:
        raise NameError("There is no such category")

def final_buy():
    global basket
    if not basket:
        raise RuntimeError("There is no item in your basket")
    else:
        for product in basket.keys():
            for value in catalogue.values():
                if product in value:
                    value[product][2] -= basket[product][1]
        basket.clear()
        return True













