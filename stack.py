
# Завдання 1
# Реалізуйте клас стеку для роботи з рядками (стек рядків).
# Стек має бути фіксованого розміру. Реалізуйте набір операцій
# для роботи зі стеком:
# o розміщення рядка у стек;
# o виштовхування рядка зі стеку;
# o підрахунок кількості рядків у стеку;
# o перевірку, чи порожній стек;
# o перевірку, чи повний стек;
# o очищення стеку;
# o отримання значення без виштовхування
# верхнього рядка зі стеку.
# На старті додатка відобразіть меню, в якому користувач
# може вибрати необхідну операцію.

class StrNode:
    def __init__(self, value: str):
        self.__value = value
        self.next = None
    
    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, data):
        if not isinstance(data, str):
            raise ValueError('Only string is allowed')
        else:
            self.__value = data

class Stack:
    def __init__(self) -> None:
        self.size = 0
        self.head = StrNode('Head')
        self.max_len = 10
    
    def __str__(self) -> str:
        if self.is_empty():
            raise IndexError('Operation with an empty stack.')
        current = self.head.next
        result = ''
        
        while current:
            result += current.value + ', '
            current = current.next
        return result[:-2]

    def __len__(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0
    
    def is_full(self):
        return self.size == self.max_len
    
    def push(self, new_value): 
        
        if len(self) == self.max_len:
            raise IndexError('Max length reached.')
        
        if not isinstance(new_value, str):
            raise ValueError('Incorrect data type. Only string is allowed.')
        
        node = StrNode(new_value)
        
        node.next = self.head.next
        self.head.next = node
        
        self.size += 1
    
    def pop(self):
        if self.is_empty():
            raise IndexError('Operation with an empty stack.')
        
        remove_node = self.head.next
        self.head.next = self.head.next.next
        
        self.size -= 1
        
        return remove_node.value
    
    def peek(self):
        if self.is_empty():
            raise IndexError('Operation with an empty stack.')
        
        return self.head.next.value
    
    def clean_stack(self):
        self.head = StrNode('Head')
        self.size = 0
    
cities = Stack()

def main():
    while True:
        print('0: Exit')
        print('1: Add to stack')
        print('2: Pop from stack')
        print('3: Show number of elements of stack')
        print('4: Check if stack is empty')
        print('5: Check if stack is full')
        print('6: Clean stack')
        print('7: Show first item')
        print('8: Show stack')
        
        choice = input('> ')
        
        match choice:
            case '0':
                break
            case '1':
                try:
                    cities.push(input('Enter new city: '))
                except IndexError as e:
                    print('Trying to add a new item:', e)
            case '2':
                try:
                    print(cities.pop())
                except IndexError as e:
                    print('Trying to remove at item:', e)
            case '3':
                print(f'Length of stack: {len(cities)}')
            case '4':
                print(f'Stack is empty: {cities.is_empty()}')
            case '5':
                print(f'Stack is full: {cities.is_full()}')
                
            case '6':
                cities.clean_stack()
            case '7':
                try:
                    print(cities.peek())
                except IndexError as e:
                    print('Trying to show the first item:', e)
            case '8':
                try:
                    print(cities)
                except IndexError as e:
                    print('Trying to show the stack:', e)
            case _:
                print('Incorrect choice')

if __name__ == '__main__':
    main()


# Завдання 3
# Дано три вежі та n дисків різного розміру, відсортованих
# за зростанням, розміщених на першій вежі у вигляді піраміди.
# Потрібно перемістити всі диски на третю вежу,
# використовуючи проміжну вежу, за умови, що можна
# переміщати тільки один диск за раз та диск завжди можна
# покласти лише на диск більшого розміру або на порожню
# вежу.
# Ця задача може бути вирішена за допомогою
# рекурсивного алгоритму, використовуючи стек для
# зберігання проміжних ходів при переміщенні дисків між
# вежами.

class Disk:
    def __init__(self, diameter):
        self.diameter = diameter
        self.next = None

class Pyramid:
    def __init__(self):
        self.disks = []
    
    def __str__(self):
        if self.is_empty():
            return "Empty pyramid"
        
        max_disk_size = max(self.disks, key=lambda disk: disk.diameter).diameter
        result = ''

        for disk in self.disks[::-1]:
            num_spaces = (max_disk_size - disk.diameter) // 2
            level = ' ' * num_spaces + '_' * disk.diameter
            result += level + '\n'
        return result
    
    def is_empty(self):
        return len(self.disks) == 0
    
    def push(self, diameter):
        disk = Disk(diameter)
        self.disks.append(disk)
    
    def pop(self):
        if self.is_empty():
            raise IndexError('Operation with an empty pyramid')
        
        return self.disks.pop()

def move_disks(n, first, final, medium):
    if n == 0:
        return
    move_disks(n - 1, first, medium, final)
    disk = first.pop()
    final.push(disk.diameter)
    move_disks(n - 1, medium, final, first)

#створення та заповнення першої піраміди
pyramid_1 = Pyramid()
for n in range(13, 0, -2):
    pyramid_1.push(n)
print("Pyramid 1 before moving disks:")
print(pyramid_1)

pyramid_2 = Pyramid()

pyramid_3 = Pyramid()

#переміщення дисків з pyramid_1 на pyramid_3, використовуючи pyramid_2 як проміжну
move_disks(len(pyramid_1.disks), pyramid_1, pyramid_3, pyramid_2)

print("\nPyramid 1 after moving:")
print(pyramid_1)
print("\nPyramid 2 after moving:")
print(pyramid_2)
print("\nPyramid 3 after moving:")
print(pyramid_3)