import data

def get_all():
    return '\n'.join([f"{x[0]}: {','.join(x[1])}" for x in data.get_all()])

def add_contact(name, *phones):
    res = data.add_contact(name, *phones)
    if res:
        return "The contact was added"
    else:
        return "Something went wrong"

def add_phone(name, phone): pass

def remove_contact(name): pass

def remove_phone(name, phone): pass

def search(name): pass