import bl

def show_message(message):
    print(message + ".")

def get_value(message, end=":\n"):
    return input(message + end)

def show_all():
    show_message(bl.get_all())

def add_contact():
    name = get_value("Enter a new name")
    phones = get_value("Enter phones separated by a comma").split(',')
    res = bl.add_contact(name, *phones)
    show_message(res)

def main_flow():
    while True:
        choosen_value = get_value("Choose your action:\n0. Exit\n1. Show all contacts\n2. Create a new contact\n", end='')
        if choosen_value == '0':
            break
        elif choosen_value == '1':
            show_all()
        elif choosen_value == '2':
            add_contact()
