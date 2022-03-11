import data
import json


def outline(data_products):
    return "\n".join(f"товар категории: {v[0]}  название: {k}  код: {v[1]}  стоимость: {v[2]}р  в наличии {v[3]}шт"
                     for k, v in data_products if v[3] != 0)


def get_all():
    """выводит пользователю все товары, которые есть в наличии"""
    return outline(data.get_all().items())


def get_category(category):
    """выводит пользователю товары по выбранной категории"""
    return outline(data.get_category(category).items())


def del_data(name_product):
    """удаляет данные из базы данных если пользователь их помещает в корзину, если он не купет товары, то они
    вернуться в корзину если купит, то нет. Считает стоимость повторного товара в корзине"""
    if data.data_base[name_product][3] > 0:
        data.data_base[name_product][3] -= 1
        if name_product not in data.basket:
            data.basket[name_product] = data.data_base[name_product][2]
        else:
            data.basket[name_product] = int(data.data_base[name_product][2]) + int(data.basket[name_product])


def get_basket():
    """возвращает товары, которые были добавлены в корзину"""
    if data.basket:
        return "\n".join(f"{int(v) // int(data.data_base[k][2])} {k} стоимостью: {v}р был добавлен в корзину"
                         for k, v in data.get_basket().items())
    else:
        return f"your basket is empty!"


def get_order():
    """возвращает строку если корзина пустаяб если в ней есть товар, то если надо считает колличество
     товара в корзине показывает пользователю и оповещает его о том, что товар куплен
    затем перезаписывает базу данных с учетом купленных товаров и выходит из программы"""
    if not data.basket:
        return f"your basket is empty! please! put the product in the basket!"
    else:
        print("\n".join(f"{int(v) // int(data.data_base[k][2])} {k} стоимостью: {v}р были куплены! спасибо за заказ!"
                        for k, v in data.get_basket().items()))
        filename = "data_base.json"
        with open(filename, "w") as f:
            json.dump(data.data_base, f)
        return quit()
