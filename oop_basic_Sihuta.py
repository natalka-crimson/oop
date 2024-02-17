from datetime import date


#1. Реалізуйте клас Student (Студент) із атрибутами name (ім'я) та grades (оцінки). Додати метод average_grade, який обчислює середню оцінку студента.

class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades
    
    def average_grade(self):
        self.aver = sum(self.grades) / len(self.grades)
        print(f'An average grade is {self.aver}')

bob = Student('Bob', [8, 10, 7, 11])
# bob.average_grade()

kate = Student('Kate', [12, 7, 7, 5, 9])
# kate.average_grade()


#2. Створіть клас Book (Книга) з атрибутами title (назва), author (автор) та publication_year (рік видання). Реалізуйте метод get_age, який повертає вік книги (поточний мінус рік видання). 

class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year
    
    def get_age(self):
        self.book_age = date.today().year - self.publication_year
        print(f'The book is {self.book_age} years old.')

forest_song = Book('Лісова пісня', 'Леся Українка', 1913)
# forest_song.get_age()

kobzar = Book('Кобзар', 'Тарас Шевченко', 1840)
# kobzar.get_age()


#3. Створіть клас BankAccount (Банківський рахунок) з атрибутами account_number (номер рахунку) та balance (баланс). Додайте методи deposit (внесення коштів) та withdraw (зняття коштів), які змінюють баланс відповідним чином. Реалізуйте метод get_balance, який повертає поточний баланс.

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, ammount):
        self.balance += ammount
    
    def withdraw(self, ammount):
        self.balance -= ammount
    
    def get_balance(self):
        print(f'Balance is {self.balance}')

acc1 = BankAccount('379237832', 650)
acc1.deposit(150)
acc1.withdraw(80)
# acc1.get_balance()