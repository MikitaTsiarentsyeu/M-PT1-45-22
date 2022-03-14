import brain


def show_query(message):
    print(message)
    val = input()
    try:
        val = int(val)
    except ValueError:
        print("You must enter digit number of operation")
        return False
    return val


def show_data(data):
    print(data)


def show_items():
    data = brain.get_all()
    show_data(data)


def main():
    while True:
        operation = show_query(
            'Enter what you want to do:\n0. Exit;\n1. Show all of items in our shop;\n2. Add something to basket;\n3. Show my basket;\n4. Make order\n')
        if operation == False:
            continue
        if operation == 0:
            break
        elif operation == 1:
            show_items()
        elif operation == 2:
            while True:
                show_items()
                action = show_query(
                    'What you want to add to basket? (You should enter number of item, which you want to add)\n0. Return to the action list\n')
                if action == 0:
                    break
                elif action == 1:
                    brain.add_to_basket(1)
                elif action == 2:
                    brain.add_to_basket(2)
                elif action == 3:
                    brain.add_to_basket(3)
                elif action == 4:
                    brain.add_to_basket(4)
                elif action == 5:
                    brain.add_to_basket(5)
        elif operation == 3:
            if brain.if_basket_is_empty():
                show_data(brain.show_basket())
            else:
                show_data("Your basket is empty")
        elif operation == 4:
            if not brain.if_basket_is_empty():
                show_data('You didnt add something to basket, do it and then make order')
            else:
                while True:
                    if not brain.make_order():
                        break
                    show_data('Sure about making order?')
                    show_data(f'Your basket - {brain.show_basket()}')
                    action_2 = show_query('0. Cancel order;\n1. Order;\n')
                    if action_2 == 0:
                        break
                    if action_2 == 1:
                        while True:
                            show_data('Did you input your address and items you gonna buy correctly?')
                            show_data(f'Your data - {brain.show_data()}')
                            action_3 = show_query('1. Yes;\n2. No, return to the previous page;\n')
                            if action_3 == 1:
                                show_data('Accepted! You can receive your order in a few days')
                                exit()
                            if action_3 == 2:
                                break
