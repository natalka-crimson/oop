from abc import ABC, abstractmethod


# Уявіть, що у вас є базовий клас Algorithm, який визначає шаблонний метод для виконання певного алгоритму. Давайте розглянемо задачу сортування списку цілих чисел. Ваше завдання – створити підкласи цього базового класу, щоб реалізувати конкретні алгоритми сортування бульбашкою та сортування вибором. (Дз виконувати за допомогою реалізації патерну «Шаблонний метод»).

class Algorithm(ABC):
    
    def sort_algorithm_template(self):
        self.l = self.get_len()
        for i in range(self.l):
            j = self.compare_and_swap(i)
            self.hook(i, j)

    def get_len(self):
        return len(self.lst)
    
    @abstractmethod
    def compare_and_swap(self, i):
        pass
    
    @abstractmethod
    def swap(self, i, j):
        pass
    
    def hook(self, i, j):
        pass
    
    def __str__(self):
        str_lst = ', '.join(map(str, self.lst))
        return f'The list: {str_lst}'

class BubbleSort(Algorithm):
    def __init__(self, lst: list):
        self.lst = lst
        
    def swap(self, i, j):
        self.lst[j], self.lst[j + 1] = self.lst[j + 1], self.lst[j]
        
    def compare_and_swap(self, i):
        for j in range(0, self.l-i-1):
            if self.lst[j] > self.lst[j + 1]:
                self.swap(i, j)
    
class SelectionSort(Algorithm):
    def __init__(self, lst: list):
        self.lst = lst
    
    def compare_and_swap(self, i):
        min_num = i
        for i in range(i+1, self.l):
            if self.lst[i] < self.lst[min_num]:
                min_num = i
        return min_num
    
    def swap(self, i, j):
        self.lst[i], self.lst[j] = self.lst[j], self.lst[i]
    
    def hook(self, i, min_num):
        return self.swap(i, min_num)

bubble_sort = BubbleSort([2, -34, 45, 1, 75, -7, 54, 9])

selection_sort = SelectionSort([58, 15, 79, -2, 17, 12, 3, -23])

bubble_sort.sort_algorithm_template()
selection_sort.sort_algorithm_template()

print(bubble_sort)
print(selection_sort)