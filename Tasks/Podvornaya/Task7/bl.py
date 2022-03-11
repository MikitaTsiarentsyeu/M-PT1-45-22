import data


def category_show(category):
    """ Function to show items by category. Will raise an error if category is absent among all the goods.
        Makes a list of fitting items to manipulate. Uses formatting to provide readable data to the user."""
    try:
        product_list = f'List of items in category "{category}": \n\n'
        items = data.show_category(category)
        for item in items:
            product_list += f'Name: {item[0]} \n Price: {item[2]}$ \n In stock: {item[3]} \n Item code: {item[4]} \n\n'
        return product_list
    except NameError:
        return "Sorry, category do not exist.\n"
    except:
        return "Oops! Something went wrong. Try again.\n"


def show_all():
    """ Shows all the items. Uses text formatting to make data more appealing to the user."""
    try:
        products = data.show_all()
        product_list = "All products in shop:\n\n"
        for item in products:
            product_list += f"Name: {item[0]}\n Category: {item[1]} \n Price: {item[2]}$ \n In stock: {item[3]} \n Item code: {item[4]} \n\n"
        return product_list
    except:
        return "Oops! Something went wrong. Try again.\n"


def add_product(code):
    """ Function to add product to a shopping cart. Will raise an Error if product is out of stock. Decreases an amount
         of pieces in stock after adding one to a shopping cart. All errors return string explanations of what went
          wrong to demonstrate it to the user.
          Exploits code validation to avoid codes that don't exist."""
    try:
        code_validation(code)
        if data.add_product(code):
            return "You successfully added an item to your shopping cart!\n"
    except RuntimeError:
        return "Sorry, product is out of stock.\n"
    except ValueError:
        return "Sorry, this code is invalid.\n"
    except:
        return "Oops! Something went wrong. Try again.\n"


def place_order():
    """Implements ordering items in shopping cart. Counts the total price. Raises an error if shopping cart is empty.
    After ordering removes all items for shopping cart so user can place another order."""
    try:
        shopping_cart = data.place_order()
        total = 0
        for item in shopping_cart:
            total += int(item[2])
        data.shopping_cart = []
        return f"Order placed! Your total will be {total}$.\n"
    except RuntimeError:
        return "Sorry, your shopping cart empty. Can't place an order.\n"
    except:
        return "Oops! Something went wrong. Try again.\n"


def shopping_card():
    """ Demonstrates to the user theirs shopping cart. Counts total price. Errors are not expected to appear as shopping
    cart is either empty or filled. Shopping cart is unlimited. I want users to spend a lot of money."""
    products = data.shopping_card()
    total = 0
    if not products:
        return "Your shopping card is empty.\n"
    else:
        product_list = "Your shopping card:\n\n"
        for item in products:
            product_list += f"Name: {item[0]}\n Category: {item[1]} \n Price: {item[2]}$ \n In stock: {item[3]} \n Item code: {item[4]} \n\n"
            total += int(item[2])
        product_list += f"Total price: {total}$\n"
        return product_list


def code_validation(code):
    """ Validates code value. Will raise an error if value is not on the list of goods."""
    code = int(code)
    if data.goods[0][-1] > code or code > data.goods[-1][-1]:
        raise ValueError

