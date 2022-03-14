katalog = {1: ('1. Bed', ['Sofa', '15523', '320$']), 2: ('2. Letto Djulia', ['Armchair', '12001', '185$']),
           3: ("3. RANDERS", ["Cupboard", "15001", "290$"]), 4: ("4. BETRI", ["Curtain", "16001", "20$"]),
           5: ("5. SORTLAND", ["Mirror", "17001", "35$"])}
basket = []
order = []


def get_all_items():
    return katalog.values()


def add_to_basket():
    return basket


def make_order():
    return order
