
# Припустимо, ви розробляєте програму для замовлення напоїв у кав'ярні. У вас є базовий клас Напій, який визначає основні характеристики кожного напою, такі як назва і вартість. Ви хочете надати можливість додавати до кожного напою додаткові складові, наприклад, молоко, цукор або шоколад.
# Задача полягає в тому, щоб застосувати паттерн "Декоратор", щоб можна було динамічно додавати додаткові функціональності до об'єктів Напій, зберігаючи при цьому їхні основні характеристики.

class DrinkDecorator:
    def __init__(self, additive, ad_price):
        self.additive = additive
        self.ad_price = ad_price

    def __call__(self, cls):
        def wrapper(drink_name, drink_price):
            drink_obj = cls(drink_name, drink_price)
            drink_obj.name = f'{drink_name} with {self.additive}'
            drink_obj.price = drink_price + self.ad_price
            return drink_obj
        return wrapper

@DrinkDecorator('milk', 5)
class Drink:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __str__(self):
        return f'You drink is {self.name} for {self.price} UAH.'
    

coffee = Drink('Cappuccino', 40)
black_tea = Drink('Black tea', 15)
print(coffee)
print(black_tea)

