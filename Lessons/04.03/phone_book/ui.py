"""UPDATE MAIN FLOW"""
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

def factory(func, is_phone_required = True):
    def maker():
        name = get_value("Enter a name")
        if is_phone_required:
            phone = get_value("Enter a phone")
        res = func(name, phone) if is_phone_required else func(name)
        show_message(res)
    return maker

add_phone = factory(bl.add_phone)
remove_contact = factory(bl.remove_contact, False)
remove_phone = factory(bl.remove_phone)

def main_flow():
    while True:
        choosen_value = get_value("Choose your action:\n0. Exit\n1. Show all contacts\n2. Create a new contact\n", end='')
        if choosen_value == '0':
            break
        elif choosen_value == '1':
            show_all()
        elif choosen_value == '2':
            add_contact()
