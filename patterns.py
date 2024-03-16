from abc import ABC, abstractmethod

# Розгляньте систему управління транспортними засобами. Необхідно реалізувати фабрику транспортних засобів, яка забезпечить створення різних видів транспорту (автомобілі, мотоцикли, велосипеди тощо).
# Створіть абстрактний клас Транспорт, який має метод пересуватися().
# Створіть конкретні класи, що реалізують Транспорт (наприклад, Автомобіль, Мотоцикл, Велосипед), кожен з яких має свою власну реалізацію методу пересуватися().
# Створіть абстрактний клас ФабрикаТранспорту з методом створити_транспорт(), який повинен бути реалізований в підкласах.
# Створіть конкретні фабрики для кожного виду транспорту (наприклад, ФабрикаАвтомобілів, ФабрикаМотоциклів, ФабрикаВелосипедів), які реалізують метод створити_транспорт() та повертають відповідний об'єкт.
# Створіть клас Клієнт, який використовує фабрику для створення транспортних засобів та виклику їх методу пересуватися().

class Transport(ABC):
    @abstractmethod
    def move(self):
        pass

class Auto(Transport):
    def move(self, speed):
        print(f'Auto is moving with speed {speed} km/hr.')

class Motorcycle(Transport):
    def move(self, speed):
        print(f'Motorcycle is moving with speed {speed} km/hr.')

class Bicycle(Transport):
    def move(self, speed):
        print(f'Bicycle is moving with speed {speed} km/hr.')

class TransportFactory(ABC):
    @abstractmethod
    def create_transport(self):
        return Transport()

class AutoFactory(TransportFactory):
    def create_transport(self):
        return Auto()

class MotorcycleFactory(TransportFactory):
    def create_transport(self):
        return Motorcycle()

class BicycleFactory(TransportFactory):
    def create_transport(self):
        return Bicycle()

auto_factory = AutoFactory()
opel = auto_factory.create_transport()
opel.move(70)

moto_factory = MotorcycleFactory()
honda = moto_factory.create_transport()
honda.move(60)

bike_factory = BicycleFactory()
merida = bike_factory.create_transport()
merida.move(15)