from datetime import timedelta
from datetime import date


# Створіть систему для електронного магазину. Маєте класи для продуктів, замовлень та користувачів. Реалізуйте можливість додавання товарів у кошик, оформлення замовлення та відстеження статусу доставки.

class Shop:
    def __init__(self):
        self.cart = {}
        self.total = 0

    def add_to_cart(self, product, quantity=1):
        self.cart.update({product.name: product.price * quantity})

    def calculate_total(self):
        self.total = sum(self.cart.values())
        return self.total

    def clear_cart(self):
        self.cart = {}


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class User:
    def __init__(self, name, city):
        self.name = name
        self.city = city


class Order:
    def __init__(self, number):
        self.number = number
    
    def make_order(self, user: User, shop: Shop):
        delivery_days = timedelta(days=2)
        self.date_of_delivery = date.today() + delivery_days
        print(f'Your order #{self.number} will be in {user.city} on {self.date_of_delivery}. Total price: {shop.total} UAH. Your products: {shop.cart}')
    
    def chech_order_status(self):
        if date.today() < self.date_of_delivery:
            print(f'Wait your order on {self.date_of_delivery}')
        else:
            print('Your order has arrived.')
        
milk_choco = Product('Milk chocolate', 25)
black_choco = Product('Black chocolate', 28)
candy = Product('Orange candy', 2.5)
almond = Product('Almond 100g', 35)
biscuit = Product('Vanila Buiscuits', 20)

market = Shop()

market.add_to_cart(biscuit, 2)
market.add_to_cart(almond)
market.add_to_cart(black_choco, 2)
market.calculate_total()

lida = User('Lida', 'Chernihiv')
or1 = Order(1)
or1.make_order(lida, market)
or1.chech_order_status()

market.clear_cart()

market.add_to_cart(milk_choco, 3)
market.add_to_cart(candy, 10)
market.add_to_cart(biscuit)
market.calculate_total()

denis = User('Denis', 'Dnipro')
or1 = Order(2)
or1.make_order(denis, market)
or1.chech_order_status()

market.clear_cart()