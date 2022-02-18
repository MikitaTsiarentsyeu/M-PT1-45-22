def start_process():
    print("STARTING A NEW PIZZA MAKING PROCESS")
    print("prepare a base")
    print("select a sause")

def add_topping(topping):
    print(f"adding some {topping}")

def add_cheese():
    print("grinding some cheese")

def bake():
    print("baking")

def finish_process():
    print("boxing")
    print("DONE!")

# def make_pepperonni():
#     start_process()
#     add_topping("pepperonni")
#     add_cheese()
#     bake()
#     finish_process()

# def make_double_pepperonni():
#     start_process()
#     add_topping("pepperonni")
#     add_topping("pepperonni")
#     add_cheese()
#     bake()
#     finish_process()

# def make_margarita():
#     start_process()
#     add_topping("tomatoes")
#     add_topping("ТРАВЫ")
#     add_cheese()
#     bake()
#     finish_process()

def pizza_factory(toppings):
    def maker():
        start_process()
        for t in toppings:
            add_topping(t)
        add_cheese()
        bake()
        finish_process()
    return maker

make_pepperonni = pizza_factory(["pepperonni"])
make_double_pepperonni = pizza_factory(["pepperonni", "pepperonni"])
make_margarita = pizza_factory(["tomatoes", "ТРАВЫ"])

make_pepperonni()
make_double_pepperonni()
make_margarita()