from pyexpat import model


allowed_colors = ["black", "red"]

class Car:

    # make = ""
    # model = ""
    # color = ""

    def __init__(self, make, model, color):
        self.__make = make
        self.__model = model.upper()
        self.set_color(color)
        self.__test = "test"

    def get_color(self):
        return self.__color

    def set_color(self, color):
        color = color.lower()
        if color in allowed_colors:
            self.__color = color
        # else:
        #     raise AttributeError(f"cannot set value {color} for attr color")

    color = property(get_color, set_color)

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_info(self):
        print(f"this is {self.__make} {self.__model} of color {self.__color}")


c = Car("Toyota", "Camry", "black")
c.get_info()

c.color = "red"
print(c.color)

# print(c.__test)
# print(c.__make)
# print(c._Car__make)

