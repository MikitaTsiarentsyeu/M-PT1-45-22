class Animal: 

    def SaySomething(self):
        print("Hello, I'm an animal")

class Dog(Animal):

    def SaySomething(self):
        print("Woof!")

class Cat(Animal):

    def SaySomething(self):
        print("Nyaaa!")

class Human:

    def SaySomething(self, something):
        print(f"Hello, I'm Ivan, saying {something}")

a = Animal()
d = Dog()
c = Cat()
h = Human()

for animal in [a, d, c, h]:
    animal.SaySomething()