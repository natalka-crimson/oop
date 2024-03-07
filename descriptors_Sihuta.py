
# Створіть систему для управління витратами. Клас Витрати повинен мати атрибути для зберігання суми витрат та категорії витрат. Використайте дескриптори для забезпечення обмежень на введені дані:
# Дескриптор для суми витрат (СумаВитрат):
# Сума витрат не може бути від'ємною.
# Сума витрат не може перевищувати заданий ліміт за місяць.
# Дескриптор для категорії витрат (КатегоріяВитрат):
# Категорія витрат повинна бути однією з попередньо визначених категорій (наприклад, "Їжа", "Транспорт", "Розваги" і т. д.).

class AmountExpense:
    def __get__(self, obj, objType=None):
        return obj.__amount_expense
    
    def __set__(self, obj, value):
        month_limit = 1000
        if value < 0:
            raise ValueError('Ammount of expense can`t be negative.')
        elif value > month_limit:
            raise ValueError('The amount of expenses can`t exceed the specified limit for the month.')
        obj.__amount_expense = value

class CategoryExpense:
    def __get__(self, obj, objType=None):
        return obj.__categories_expense
    
    def __set__(self, obj, value):
        categories = ['food', 'transport', 'entertainment', 'sport', 'study', 'traveling']
        if value not in categories:
            raise ValueError('Category is not defined.')
        obj.__categories_expense = value

class Expenses:
    amount_expense = AmountExpense()
    categories_expense = CategoryExpense()
    
    def __init__(self, amount_expense, categories_expense):
        self.amount_expense = amount_expense
        self.categories_expense = categories_expense


march_expense = Expenses(800, 'food')
print(march_expense.amount_expense)
print(march_expense.categories_expense)

# april_expense = Expenses(-1700, 'clothes')
# print(april_expense.amount_expense)
# print(april_expense.categories_expense)