repo = { 1 : ["some name", ["2345678", "3456789"]], 2 : ["another name", ["2345678"]]}

def get_all():
    return repo.values()

def add_contact(name, *phones):
    try:
        for i in range(1, len(repo)+2):
            if i not in repo:
                repo[i] = [name, phones]
                return True
    except:
        return False

def add_phone(name, phone): pass

def remove_contact(name): pass

def remove_phone(name, phone): pass

def search(name): pass