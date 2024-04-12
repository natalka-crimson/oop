
# Реалізуйте базу даних зі штрафами податкової
# інспекції. Ідентифікувати кожну конкретну людину буде
# персональний ідентифікаційний код. В однієї людини може
# бути багато штрафів.
# Реалізуйте:
# 1. Повний друк бази даних;
# 2. Друк даних за конкретним кодом;
# 3. Друк даних за конкретним типом штрафу;
# 4. Друк даних за конкретним містом;
# 5. Додавання нової людини з інформацією про неї;
# 6. Додавання нових штрафів для вже існуючого запису;
# 7. Видалення штрафу;
# 8. Заміна інформації про людину та її штрафи.
# Використайте дерево для реалізації цього завдання.

class Person:
    def __init__(self, id_code):
        self.id_code = id_code
        
        self.left = None
        self.right = None
        
        self.tax_fines = []
    
    def __str__(self):
        return f'ID: {self.id_code} Fines: {self.tax_fines}'

class TaxInspectionBase:
    def __init__(self):
        self.root = None
    
    def __insert_recursive(self, new_id, current_person: Person):
        if new_id < current_person.id_code:
            if current_person.left is None:
                current_person.left = Person(new_id)
            else:
                self.__insert_recursive(new_id, current_person.left)
        else:
            if current_person.right is None:
                current_person.right = Person(new_id)
            else:
                self.__insert_recursive(new_id, current_person.right)
    
    def insert_person(self, new_id):
        if self.root is None:
            self.root = Person(new_id)
            return
        
        self.__insert_recursive(new_id, self.root)
    
    def __inorder_traversal_recursive(self, current_person: Person):
        if current_person is not None:
            self.__inorder_traversal_recursive(current_person.left)
            print(f'Person ID: {current_person.id_code}\nTax inspection fines: {current_person.tax_fines}\n')
            self.__inorder_traversal_recursive(current_person.right)
    
    def inorder_traversal(self):
        if self.root is None:
            raise ValueError('Empty tree!')
        self.__inorder_traversal_recursive(self.root)
    
    def __search_recursive(self, person_id, current_person: Person):
        if current_person is None:
            return False
        elif current_person.id_code == person_id:
            return current_person
        elif person_id < current_person.id_code:
            return self.__search_recursive(person_id, current_person.left)
        else:
            return self.__search_recursive(person_id, current_person.right)
    
    def search(self, person_id):
        return self.__search_recursive(person_id, self.root)
    
    def add_fine(self, id_code, fine):
        if not self.search(id_code):
            raise ValueError('Person ID not found')
        else:
            update_person = self.search(id_code)
            update_person.tax_fines.append(fine)
    
    def remove_fine(self, id_code, fine_index):
        if not self.search(id_code):
            raise ValueError('Person ID not found')
        else:
            update_person = self.search(id_code)
            if len(update_person.tax_fines) < fine_index - 1:
                raise IndexError('Incorrect index')
            del update_person.tax_fines[fine_index]

tax_base = TaxInspectionBase()

def main():
    while True:
        print('0: Вихід')
        print('1: Повний друк бази даних')
        print('2: Друк даних за конкретним кодом')
        print('3: Додавання нової людини з інформацією про неї')
        print('4: Додавання нових штрафів для вже існуючого запису')
        print('5: Видалення штрафу')
        
        choice = input('> ')
        
        match choice:
            case '0':
                break
            case '1':
                try:
                    tax_base.inorder_traversal()
                except ValueError as e:
                    print('Trying to see the full base:', e)
            case '2':
                try:
                    result = tax_base.search(int(input('Enter ID to see info: ')))
                    if result:
                        print(result)
                    else:
                        print('ID not found')
                except ValueError:
                    print('Input must be an integer')
            case '3':
                try:
                    tax_base.insert_person(int(input('Enter person`s ID: ')))
                except ValueError:
                    print('Input must be an integer')
            case '4':
                try:
                    id = int(input('Enter person`s ID: '))
                    fine = int(input('Enter fine: '))
                    tax_base.add_fine(id, fine)
                except ValueError as e:
                    print('Trying to add fine:', e)
            case '5':
                try:
                    id = int(input('Enter person`s ID: '))
                    fine_in = int(input('Enter fine index to remove: '))
                    tax_base.remove_fine(id, fine_in)
                except ValueError as e:
                    print('Trying to remove fine:', e)
                except IndexError as e:
                    print('Trying to remove fine:', e)
            case _:
                print('Incorrect choice')

if __name__ == '__main__':
    main()
