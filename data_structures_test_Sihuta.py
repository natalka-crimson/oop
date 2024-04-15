import random
from datetime import datetime


# 1. Напишіть функцію для побудови структури дерева з використанням класів. Дерево повинно мати такі властивості:
# Кожен вузол дерева повинен мати значення (наприклад, ціле число) та список дочірніх вузлів. 
# Функція повинна приймати значення кореня дерева та список його дочірніх вузлів. 
# Має бути можливість додавати нові вузли до будь-якого вузла в дереві. 
# Функція повинна надавати метод для виведення дерева у вигляді деревоподібної структури або іншим зручним способом. 

class Node:
    def __init__(self, value):
        self.value = value
            
        self.left = None
        self.right = None

    def __str__(self):
        return self.value

class BinaryTree:
    def __init__(self):
        self.root = None
        
    def __insert_recursive(self, new_value, current_node: Node):
        if new_value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(new_value)

            else:
                self.__insert_recursive(new_value, current_node.left)
        else:
            if current_node.right is None:
                current_node.right = Node(new_value)
                
            else:
                self.__insert_recursive(new_value, current_node.right)
        
    def insert(self, new_value):
        if self.root is None:
            self.root = Node(new_value)
            return
            
        self.__insert_recursive(new_value, self.root)
        
    def __inorder_traversal_recursive(self, current_node: Node):
        if current_node is not None:
            self.__inorder_traversal_recursive(current_node.left)
            
            print(current_node.value)
            self.__inorder_traversal_recursive(current_node.right)
        
    def inorder_traversal(self):
        self.__inorder_traversal_recursive(self.root)
    
    def print_ascii_tree(self): # є глюк, але це найкраще, що вдалось зробити (робила з інтернетом)
        self._print_ascii_tree_recursive(self.root)

    def _print_ascii_tree_recursive(self, node, prefix='', is_left=True):
        if node is not None:
            self._print_ascii_tree_recursive(node.right, prefix + ('│   ' if is_left else '    '), False)
            print(prefix + ('└── ' if is_left else '┌── ') + str(node.value))
            self._print_ascii_tree_recursive(node.left, prefix + ('    ' if is_left else '│   '), True)


root = 10
children = [3, 65, 2, 6, 71, 14, 4, 1, 8, 16, 30, 12]

def build_tree(root, children):

    tree = BinaryTree()
    
    tree.insert(root)
    
    for ch in children:
        tree.insert(ch)
    
    tree.print_ascii_tree()
    return tree


def add_node(tree, new_node):
    tree.insert(new_node)
    tree.inorder_traversal()
    return tree

# build_tree(root, children)
# add_node(build_tree(root, children), 26)


# 2. Напишіть функцію, яка приймає на вхід корінь дерева і повертає максимальну глибину цього дерева.

def find_depth(root):
    if root is None:
        return 0
    
    left_depth = find_depth(root.left)
    right_depth = find_depth(root.right)
    return max(left_depth, right_depth) + 1

print(find_depth(build_tree(root, children).root))


# 3. Напишіть функцію на, яка приймає на вхід список і повертає його середній елемент. Якщо кількість елементів у списку парна, поверніть середнє значення двох центральних елементів.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.size = 0
        self.head = Node('Head')
    
    def __str__(self):
        current = self.head.next
        result = ''
        
        while current:
            result += str(current.value) + ' -> '
            current = current.next
        return result[:-4] 

    def __len__(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0
    
    def push(self, new_value):
        node = Node(new_value)
        
        node.next = self.head.next
        self.head.next = node
        
        self.size += 1
    
    def pop(self):
        if self.is_empty():
            raise IndexError('Operation with an empty stack')
        
        remove_node = self.head.next
        self.head.next = self.head.next.next
        
        self.size -= 1
        
        return remove_node.value
    
    def peek(self):
        if self.is_empty():
            raise IndexError('Operation with an empty stack')
        
        return self.head.next.value

numbers = [random.randint(1, 100) for _ in range(random.randint(10, 15))]
stack = Stack()
for number in numbers:
    stack.push(number)

def show_medium(stack: Stack):
    current = stack.head.next
    if len(stack) % 2 != 0:
        for _ in range(len(stack) // 2):
            current = current.next
        return current.value
    else:
        for _ in range(len(stack) // 2 - 1):
            current = current.next
        return round((current.value + current.next.value) / 2, 2)

# print(f'The medium in the stack "{stack}" is {show_medium(stack)}.')


# 4. Розробіть додаток, що імітує чергу запитів до сервера. Мають бути клієнти, які надсилають запити на сервер, кожен з яких має свій пріоритет. Кожен новий клієнт потрапляє у чергу залежно від свого пріоритету. Зберігайте статистику запитів (користувач, час) в окремій черзі. Передбачте виведення статистики на екран. Вибір необхідних структур даних визначте самостійно.

class RequestQueue:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def enqueue(self, new_value):
        self.items.append(new_value)
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError('Queue is empty')
        return self.items.pop(0)

high_priority_queue = RequestQueue()
low_priority_queue = RequestQueue()

class RequestStatistic:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def enqueue(self, new_value):
        self.items.append(new_value)
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError('Queue is empty')
        return self.items.pop(0)

statistic = RequestStatistic()

class Client:
    def __init__(self, id):
        self.id = id
    
    def send_request(self, priority, request):
        timestamp = datetime.now()
        string_timestamp = timestamp.strftime('%Y-%m-%d %H:%M:%S')
        
        statistic.enqueue((f'Request from client ID: {self.id} sent at {string_timestamp}'))
        
        match priority:
            case 'high':
                high_priority_queue.enqueue(request)
            case 'low':
                low_priority_queue.enqueue(request)
            case _:
                raise ValueError('Wrong input')

class Server:
    def handle_requests(self):
        if not high_priority_queue.is_empty():
            print(high_priority_queue.dequeue())
        else:
            print(low_priority_queue.dequeue())

client_1 = Client(101)
client_2 = Client(102)
client_3 = Client(103)
client_1.send_request('high', 'Get info')
client_2.send_request('low', 'Show info')
client_3.send_request('high', 'Update info')
client_3.send_request('low', 'Delete info')
client_3.send_request('high', 'Add data to the table')

server = Server()
while not high_priority_queue.is_empty() or not low_priority_queue.is_empty():
    server.handle_requests()

def show_statistic():
    while not statistic.is_empty():
        print(statistic.dequeue())
print('Request log:')
show_statistic()
