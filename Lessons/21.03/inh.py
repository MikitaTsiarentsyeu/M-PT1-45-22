from matplotlib.pyplot import cla


class Vehicle:

    def __init__(self, make, model, power) -> None:
        self.make = make
        self.model = model
        self.set_power(power)

    def get_power(self):
        return self.__power

    def set_power(self, power):
        self.__power = power

    power = property(get_power, set_power)
    
    def move(self):
        print("I'm moving!")

class SimpleCar(Vehicle) : pass

sc = SimpleCar("Ford", "Focus", 144)

# print(sc.power)

# sc.move()

class Car(Vehicle):

    def __init__(self, make, model, power, color) -> None:
        super().__init__(make, model, power)
        # Vehicle.__init__(self, make, model, power)
        self.set_color(color)

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    color = property(get_color, set_color)

    def move(self):
        print(f"I'm a car of {self.color} color!")
        super().move()


c = Car("Kia", "Optima", 123, "White")
# print(c.power, c.color)
# c.move()

class Food:

    def __init__(self, name,  type) -> None:
        self.name = name
        self.type = type

    def __str__(self):
        return self.name

class Animal:

    def eat(self, something):
        print(f"Eating {something}")

    def phe(self):
        print("Phe..")

class Carnivore(Animal):

    def eat(self, something):
        if something.type == "meat":
            # super().eat()
            Animal.eat(self, something)
        else:
            super().phe()

class Herbivore(Animal):

    def eat(self, something : Food):
        if something.type == "herbal":
            Animal.eat(self, something)
        else:
            super().phe()

class Omnivore(Carnivore, Herbivore):

    def eat(self, something):
        if something.type == "meat":
            Carnivore.eat(self, something)
        elif something.type == "herbal":
            Herbivore.eat(self, something)

chicken = Food("chicken", "meat")
grass = Food("grass", "herbal")

human = Omnivore()
human.eat(chicken)
human.eat(grass)

print(Omnivore.mro())