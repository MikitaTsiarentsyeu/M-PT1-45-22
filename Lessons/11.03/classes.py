class Simpleton: pass

s = Simpleton()
print(s, type(s))
print(Simpleton, type(Simpleton))

s2 = Simpleton()

Simpleton.test = "default test value"

s.test = 12
print(s.test, s2.test)

def new_func(self):
    print("this is a new func")

s.n_f = new_func

s.n_f(s)

allowed_colors = ["green", "black", "red"]

class Car:

    # make = ""
    # model = ""
    # color = ""

    def init(self, make, model, color):
        self.__make = make
        self.__model = model.upper()
        self.set_color(color)

    def get_color(self):
        return self.__color

    def set_color(self, color):
        color = color.lower()
        if color in allowed_colors:
            self.__color = color
        # else:
        #     raise AttributeError(f"cannot set value {color} for attr color")

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_info(self):
        print(f"this is {self.__make} {self.__model} of color {self.__color}")

    # def change_color(self, new_color):
    #     self.color = new_color

c1 = Car()
c1.init("Toyota", "Camry", "Black")
# c1.make = "Toyota"
# c1.model = "Camry"
# c1.color = "Black"

c2 = Car()
c2.init("Tesla", "Model s", "Red")
# c2.make = "Tesla"
# c2.model = "Model s"
# c2.color = "Red"

c1.get_info()
c2.get_info()

print(c1.get_make(), c1.get_model())
c1.set_color("red")
print(c1.get_color())

print(c1._Car__make)