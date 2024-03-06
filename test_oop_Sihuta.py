
#1. Напишіть клас Animal, який при створенні екземпляру надає йому атрибут виду тварини species. Клас має містити метод, який виводить інформацію про вид тварини, і метод, який виводить характерний звук для даного виду тварини. Створіть два класи Dog і Cat, які успадковуються від класу Animal (є підкласами для Animal). У кожному з підкласів реалізуйте виклик конструктора надкласу з передачею йому назви виду тварини. Також, у підкласах реалізуйте методи, які перевизначають метод надкласу для відтворення характерного звуку для конкретного виду тварини. Визначте окрему функцію show_animal_info, яка приймає об’єкт (екземпляр класу) як аргумент і викликає його методи show_species і make_sound, якщо це тварина, а інакше - виводиться відповідне повідомлення як у вихідних даних.

class Animal:
    def __init__(self, species):
        self.species = species
    
    def show_species(self):
        return self.species
    
    def make_sound(self):
        return 'Animal`s sound'

class Dog(Animal):
    def __init__(self, species):
        super().__init__(species)
           
    def make_sound(self):
        return 'Woof'

class Cat(Animal):
    def __init__(self, species):
        super().__init__(species)
    
    def make_sound(self):
        return 'Meow'

buddy = Dog('dog')
josephine = Dog('dog')
musia = Cat('cat')
kitty = Cat('cat')

animals = [buddy, josephine, musia, kitty]

def show_animal_info(*animals):
    for animal in animals:
        if isinstance(animal, Animal):
            print(f'It`s a {animal.show_species()}. It says {animal.make_sound()}!')
        else:
            print('It`s not an animal.')

# show_animal_info(*animals)


# 2.Реалізуйте клас-зоопарк (Zoo), що можє вміщувати в себе об’єкти класу Animal, та його дочірніх класів. Zoo повинен мати метод, що заставляє всіх його тварин відтворити їх характерний звук (Поліморфізм), та методи, що дозволяють додавати та видаляти тварин.

class Zoo:
    def __init__(self):
        self.animals = []
    
    def add_animal(self, animal: Animal):
        if animal not in self.animals:
            self.animals.append(animal)
    
    def remove_animal(self, animal: Animal):
        animal_spice = animal.species
        if animal_spice in self.animals:
            self.animals.pop(animal_spice)
        else:
            print('Animan not found')
    
    def play_sound(self):
        for animal in self.animals:
            print(f'{animal.species} says {animal.make_sound()}')
    

class Animal:
    def __init__(self, species):
        self.species = species
    
    def get_species(self):
        return self.species
    
    def make_sound(self):
        return 'Animal`s sound'

class Monkey(Animal):
    def __init__(self, species):
        super().__init__(species)
    
    def make_sound(self):
        return 'Hoo-hoo'

class Giraffe(Animal):
    def __init__(self, species):
        super().__init__(species)
    
    def make_sound(self):
        return 'Grumble'

class Parrot(Animal):
    def __init__(self, species):
        super().__init__(species)
    
    def make_sound(self):
        return 'Squawk'

zoopark = Zoo()

amanda = Monkey('monkey')
ken = Giraffe('giraffe')
jaco = Parrot('parrot')

zoopark.add_animal(amanda)
zoopark.add_animal(ken)
zoopark.add_animal(jaco)

# zoopark.play_sound()


# 3. * Реалізуйте систему для реєстрації та автентифікації користувачів. Програма може мати декілька класів, що відповідають різним рівням користувачів (User, Admin, тощо), та інтерфейс для взаємодії.

class BaseUser:
    def __init__(self, username, password):
        self.username = username
        self.__password = password
        self.islogged_in = False
        self.user_role = 'user'
    
    def get_password(self):
        return self.__password

class Member(BaseUser):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.user_role = 'member'

class Admin(BaseUser):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.user_role = 'admin'

class Moderator(BaseUser):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.user_role = 'moderator'

class System:
    def __init__(self):
        self.users = {}
    
    def sign_up(self, user: BaseUser):
        user_password = user.get_password()
        self.users.update({user.username: user_password})
        print(f'{user.username} is registered in the System.')
    
    def sign_in(self, user: BaseUser):
        user_password = user.get_password()
        for person in self.users.items():
            if user.username == person[0] and user_password == person[1]:
                user.islogged_in = True
                print('You are logged in')
                break
        else:
            print('Wrong username or password. If you don`t have an account, please sign up.')
    
    def get_system_content(self, user: BaseUser):
        if not user.islogged_in:
            print('You are not logged in')
            return
        if user.user_role == 'member':
            with open('system_content.txt', 'r', encoding='UTF-8') as file:
                content = file.read()
                print(content)
        if user.user_role == 'moderator' or user.user_role == 'admin':
            with open('system_content.txt', 'a', encoding='UTF-8') as file:
                new_article = input('Write new article: ')
                file.write(new_article + '\n')
            with open('system_content.txt', 'r', encoding='UTF-8') as file:
                content = file.read()
                print(content)

# journal = System()

# jack = Admin('jack_rassel', 'bdsj<7932$df')
# anna = Member('ann_nilson', 'b98s^&dhbs')
# journal.get_system_content(jack)
# journal.sign_in(jack)
# journal.sign_up(jack)
# journal.sign_in(jack)
# journal.get_system_content(jack)
# journal.sign_up(anna)
# journal.sign_in(anna)
# journal.get_system_content(anna)


#4. *Розробіть класи для представлення виробів, робочих процесів та виробничого обладнання. Реалізуйте систему, яка дозволяє планувати та відстежувати виробничі операції.

class Cake:
    def __init__(self, name):
        self.name = name
        self.biscuit_base = ['flour', 'butter', 'milk', 'salt']
        self.cake_cream = ['milk', 'butter', 'vanilla', 'sugar']
        self.dough = False
        self.crust = False
        self.cream = False

class DoughMixer:
    def knead_dough(self, cake: Cake):
        cake.dough = True
        print(f'The ingredients of biscuit base: {cake.biscuit_base} are mixed and dough is ready.')

class Oven:
    def bake_crust(self, cake: Cake):
        if cake.dough:
            self.crust = True
            print('Biscuit base is baked.')
        else:
            print('You must knead the dough first.')

class CreamMixer:
    def make_cream(self, cake: Cake):
        self.cream = True
        print(f'The cream ingredients: {cake.cake_cream} are mixed. Cream is ready.')

class Cook:
    def __init__(self, name):
        self.name = name
        
    def introduce(self, cake: Cake):
        print(f'Hello! My name is {self.name}. I`ll make a {cake.name} for you.')
    
    def make_cake(self, cake: Cake, dough_mixer: DoughMixer, cooker: Oven, mixer: CreamMixer):
        dough_mixer.knead_dough(cake)
        cooker.bake_crust(cake)
        mixer.make_cream(cake)
        print(f'I put cream on biscuit and {cake.name} is ready!')

banana_cake = Cake('Banana Cake')
banana_cake.cake_cream = ['banana', 'milk', 'butter', 'sugar']

coconut_cake = Cake('Coconut Cake')
coconut_cake.cake_cream = ['flesh of mature coconuts', 'milk', 'butter', 'sugar']

chocolate_cake = Cake('Chocolate Cake')
chocolate_cake.cake_cream = ['chocolate', 'milk', 'butter', 'sugar']

dough_mixer = DoughMixer()
cooker = Oven()
mixer = CreamMixer()

anna = Cook('Anna')
# anna.introduce(coconut_cake)
# anna.make_cake(coconut_cake, dough_mixer, cooker, mixer)


# 5. Створіть класи для замовлень, страв, кур'єрів та клієнтів. Реалізуйте функціонал для прийому та обробки замовлень, визначення маршрутів для доставки та відстеження статусу замовлень.

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def say_hello(self):
        print(f'Hello! My name is {self.name}. I am {self.age} y.o.')


class Courier(Human):
    def __init__(self, name, age):
        super().__init__(name, age)
        
    def say_hello(self):
        print(f'I`m courier {self.name} and I deliver an order.')
        
class Food:
    def __init__(self, food_name, price):
        self.food_name = food_name
        self.__price = price
        
    def get_price(self):
        return self.__price

class Order:
    def __init__(self, order_list, order_address):
        self.order_list = order_list
        self.order_address = order_address

    def delivery(self, courier: Courier):
        order_sum = self.__calculate_sum()
        courier.say_hello()
        print(f'Order sum: {order_sum}')
        print(f'Delivery to the address: {self.order_address}.')
    
    def __calculate_sum(self):
        return(sum(food.get_price() for food in self.order_list))

class Client(Human):
    def __init__(self, name, age, address):
        super().__init__(name, age)
        self.address = address
        
    def create_order(self, *order_values: Food):
        self.say_hello()
        print('Order is made.')
        return Order(list(order_values), self.address)
    

olena = Client('Olena', 25, 'Kyiv, Central Str, 24/12')

stepan = Courier('Stepan', 20)

# olena_order = olena.create_order(Food('Pizza', 150), Food('Humburger', 80))

# olena_order.delivery(stepan)