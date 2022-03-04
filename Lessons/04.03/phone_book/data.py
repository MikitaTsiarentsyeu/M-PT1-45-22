"""TO DO: IMPLEMENT FACTORY"""
repo = { 1 : ["some name", ["2345678", "3456789"]], 2 : ["another name", ["2345678"]]}

def get_all():
    return repo.values()

def add_contact(name, *phones):
    for i in range(1, len(repo)+2):
        if i not in repo:
            repo[i] = [name, phones]
            return True

def add_phone(name, phone):
    for contact in repo.values():
        if contact[0] == name:
            contact[1].append(phone)
            return True
    raise NameError("the contact with such name was not found")

def remove_contact(name):
    for id, contact in repo.items():
        if contact[0] == name:
            del repo[id]
            return True
    raise NameError("the contact with such name was not found")

def remove_phone(name, phone):
    for contact in repo.values():
        if contact[0] == name:
            contact[1].remove(phone)
            return True
    raise NameError("the contact with such name was not found")

def search(name): pass