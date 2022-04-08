import data
import ui


def get_all_category():
    all_category = data.all_category()
    print ('\n|| Категория  || Наименование || Номенклатурный код  || Цена  || Количество на складе ||\n')
    for k, v in all_category:
        print ((f"|| {v[0]}   || {k}  || {v[1]}  || {v[2]} || {v[3]}||\n"))
    ui.continue_selection()



def get_category(category):
    cat = data.category(category)
    #print (cat)
    for k, v in cat:
        print (f"|| Наименование: {k}\n|| Номенклатурный код: {v[1]}\n|| Цена: {v[2]} USD\n|| В наличии: {v[3]} шт.\n")
    ui.product_selection()
    ui.continue_execution()
    

def get_product(selection_product, quantity_product):
    product = data.all_category()
    #print (product)
    for k, v in product:
        if k == selection_product:
            name_category = v[0]
            name_product = k
            price_product = float(v[2])
            cost_product = round((int(quantity_product)*float(v[2])), 2)
            remaining_stock = int(v[3])-int(quantity_product)
            print ((f"""\nВы выбрали {name_product}, {name_category}, по цене {price_product} USD, в количестве {quantity_product} бутылок.\n
Общая стоимость товара: {cost_product} долларов США.\nОстаток на складе: {remaining_stock}\n"""))
    basket = [name_category, name_product, quantity_product, price_product, cost_product, remaining_stock]
    print (basket)
    ui.put_basket(basket)
    return basket
    
basket_finish = []
def get_basket(basket):
    [basket_finish.append(elem) for elem in basket]
    print (basket_finish)
    bf = basket_finish
    len_bf = len(bf)
    i = 0
    a = 1
    the_sum = []
    print ('\nВы выбрали товары:\n' )
    while a <= len_bf/6:
        print (f'{a}. {bf[i]} {bf[i+1]}, в количестве: {bf[i+2]} бут., по цене: {bf[i+3]} $, стоимостью: {bf[i+4]} $')
        the_sum.append(bf[i+4])
        i = i+6
        a +=1
    total_amount = sum(the_sum)
    print (f'\nИтого общая сумма товаров в корзине: {total_amount} $\n')
   