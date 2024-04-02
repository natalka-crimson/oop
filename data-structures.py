
# Завдання 
# Користувач вводить з клавіатури набір чисел. Отримані 
# числа необхідно зберегти до списку (тип списку оберіть в залежності від поставленого нижче завдання). Після чого покажіть меню, в якому запропонуєте користувачеві набір пунктів: 
# 1. Додати нове число до списку (якщо таке число існує у
# списку, потрібно вивести повідомлення про це користувачеві без додавання числа).
# 2. Видалити усі входження числа зі списку (користувач вводить з клавіатури число для видалення)
# 3. Показати вміст списку (залежно від вибору користувача,
# покажіть список з початку або з кінця)
# 4. Перевірити, чи є значення у списку
# 5. Замінити значення у списку (користувач визначає, чи
# замінити тільки перше входження, чи всі)
# Дія виконується залежно від вибору користувача, після
# чого меню з’являється знову.


class SinglyNode:
    def __init__(self, data):
        self.data = data 
        self.next = None
    
    def __str__(self):
        return f'{self.data} -> {self.next}'
    
    def set_next(self, next):
        self.next = next

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
    
    def __str__(self):
        return f'{self.head}'
    
    def __len__(self):
        return self.length
    
    def append(self, data):
        self.length += 1
        new_node = SinglyNode(data)
        
        if self.head is None:
            self.head = new_node
            return
        
        last_node = self.head
        
        while last_node.next:
            last_node = last_node.next
        
        last_node.set_next(new_node)
    
    def insert_at_begining(self, data):
        self.length += 1
        new_node = SinglyNode(data)
        
        new_node.set_next(self.head)
        self.head = new_node
    
    def insert_after_key(self, key, data):
        if not self.search(key):
            raise ValueError('Key not found')
    
        self.length += 1
        new_node = SinglyNode(data)
        temp = self.head
        while temp is not None:
            if temp.data == key:
                new_node.set_next(temp.next)
                temp.set_next(new_node)
                return
            temp = temp.next
    
    def search(self, key):
        search_val = self.head
        while search_val is not None:
            if search_val.data == key:
                return True
            search_val = search_val.next
        return False
    
    def count(self, key):
        if not self.search(key):
            return 0
        
        count = 0
        count_val = self.head
        
        while count_val is not None:
            if count_val.data == key:
                count += 1
            count_val = count_val.next
        return count
        
    def remove(self, key):
        if not self.search(key):
            raise ValueError('Key not found')
        
        self.length -= 1
        
        while self.count(key) != 0:
        
            temp = self.head
            
            if temp is not None:
                if temp.data == key:
                    self.head = temp.next
                    temp = None
                    return
            while temp is not None:
                if temp.data == key:
                    break
                prev = temp
                temp = temp.next
            
            if temp == None:
                return
            
            prev.set_next(temp.next)
            temp = None
    
    def replace_first(self, key, data):
        if not self.search(key):
            raise ValueError('Key not found')
        
        rep_val = self.head
        
        while rep_val is not None:
            if rep_val.data == key:
                rep_val.data = data
                break
            rep_val = rep_val.next
    
    def replace_all(self, key, data):
        if not self.search(key):
            raise ValueError('Key not found')
        
        rep_val = self.head
        
        while rep_val is not None:
            if rep_val.data == key:
                rep_val.data = data
            rep_val = rep_val.next


my_list = SinglyLinkedList()
my_list.append('March')
my_list.append('April')
my_list.append('May')
my_list.append(1)
my_list.append(2)
my_list.append('May')
my_list.append(2)
my_list.append('May')
my_list.insert_at_begining(10)
my_list.insert_at_begining('start')
my_list.insert_after_key(2, 9)
my_list.insert_after_key('April', 4)
print(my_list.search('April'))
print(my_list)
print(len(my_list))
my_list.remove(9)
print(my_list.count('May'))
my_list.replace_all(2, 7)
print(my_list)
my_list.replace_first('May', 5)
print(my_list)
print(len(my_list))
