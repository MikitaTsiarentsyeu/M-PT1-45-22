from django.template import engines


class Engine:

    def __init__(self, power) -> None:
        self.__power = power

    def get_power(self):
        return self.__power

    power = property(get_power)

class SerialCar:

    def __init__(self, engine) -> None:
        self.engine = engine

    def set_engine(self, engine):
        self.__engine = engine

    def get_engine(self):
        return self.__engine

    engine = property(get_engine, set_engine)

v6 = Engine(100)
Polo = SerialCar(v6)

v8 = Engine(250)
Polo.engine = v8

class SuperCar:

    def __init__(self, power) -> None:
        self.__engine = Engine(power)

    def get_engine(self):
        return self.__engine

    engine = property(get_engine)

ferrari100 = SuperCar(100)
ferrari250 = SuperCar(250)