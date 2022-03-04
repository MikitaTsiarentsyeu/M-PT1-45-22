import data

def factory(func, is_phone_required = True):
    def maker(name, phone):
        try:
            validate_phone(phone)
        except ValueError:
            return "The phone must consist of digits"
        except RuntimeError as err:
            return err

        try:
            func(name, phone) if is_phone_required else func(name)
        except NameError as err:
            return str(err)
        except:
            return "Something went wrong"

        return "The operation was successful"
    return maker

add_phone = factory(data.add_phone)
remove_contact = factory(data.remove_contact, False)
remove_phone = factory(data.remove_phone)


def get_all():
    return '\n'.join([f"{x[0]}: {','.join(x[1])}" for x in data.get_all()])

def add_contact(name, *phones):
    try:
        data.add_contact(name, *phones)
    except:
        return "Something went wrong"

    return "The contact was added"
    
def validate_phone(phone):
    phone = int(phone)
    if not (999999 < phone < 100000000):
        raise RuntimeError("the phone must consist of 7 digits")

# def add_phone(name, phone):
#     try:
#         data.add_phone(name, phone)
#     except NameError as err:
#         return str(err)
#     except:
#         return "Something went wrong"

#     return "The phone was added"

# def remove_contact(name):
#     try:
#         data.remove_contact(name)
#     except NameError as err:
#         return str(err)
#     except:
#         return "Something went wrong"

#     return "The contact was removed"

# def remove_phone(name, phone):
#     try:
#         data.remove_phone(name, phone)
#     except NameError as err:
#         return str(err)
#     except:
#         return "Something went wrong"

#     return "The phone was removed"

def search(name): pass