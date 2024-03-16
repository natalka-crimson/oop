
#1. Створіть метаклас, що обмежує деякі назви атрибутів та методів(), забороняючи їх використання. Перелік обмежених назв можна написати прямо у метакласі.

class MetaClass(type):
    def __new__(cls, name, bases, attrs):
        
        forbidden_names = ['object', 'meta', 'inheritance', 'encapsulation', 'decorator', 'closure']
        for name in attrs:
            if name in forbidden_names:
                raise ValueError(f'{name} is forbidden. You are not allowed to use it.')
            
        return super().__new__(cls, name, bases, attrs)

class Creator(metaclass=MetaClass):
    name = 'Creator'
    def get_name(self):
        return Creator.name
    meta = 123
    def decorator(self):
        return('It is forbidden name.')
    
obj = Creator()
print(obj.name)
print(obj.get_name())


#2. *Реалізуйте патерн проектування Сінглтон. Створіть метаклас, що обмежує кількість екземплярів класу до 1. При наступному створенні об’єкту, все одно повинен повертатись перший екземпляр (див. патерн Singleton).

class SingletonMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):

        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):
    name = 'class 1'

obj1 = Singleton()
obj2 = Singleton()

print(obj1 == obj2)
