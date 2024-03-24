from abc import ABC, abstractmethod

#1. Ваша команда розробляє програму для керування списком завдань (to-do list). Ваше завдання – реалізувати функціональність повідомлень користувача про майбутні завдання. Для цього ви вирішуєте використовувати патерн Observer. Після реалізації цієї структури ви зможете підписатися на повідомлення про завдання та отримувати оповіщення про майбутні події у вашому списку завдань. 

class Observer(ABC):
    def __init__(self, name) -> None:
        self.name = name
    @abstractmethod
    def update(self, to_do_list):
        pass

class TeamMember(Observer):
    def update(self, to_do_list):
        print(f'{self.name}, check the updated to-do list: {to_do_list}')

class Program(ABC):
    def __init__(self) -> None:
        self.observers = []
    
    def add_observer(self, observer: Observer):
        self.observers.append(observer)
    
    def remove_observer(self, observer: Observer):
        self.observers.remove(observer)
    
    def notify_observers(self, to_do_list):
        for observer in self.observers:
            observer.update(to_do_list)
    
class ToDoList(Program):
    def __init__(self) -> None:
        super().__init__()
        self.to_do_list = []
        
    def add_to_do_item(self, item):
        self.to_do_list.append(item)
        self.notify_observers(self.to_do_list)
    
    def remove_to_do_item(self, item):
        self.to_do_list.remove(item)
        self.notify_observers(self.to_do_list)


anna = TeamMember('Anna')
nick = TeamMember('Nick')
olena = TeamMember('Olena')

conference_preparation = ToDoList()

conference_preparation.add_observer(anna)
conference_preparation.add_observer(nick)
conference_preparation.add_observer(olena)

conference_preparation.add_to_do_item('send invitations to conference')
conference_preparation.add_to_do_item('invite speakers')
conference_preparation.add_to_do_item('make topics')
conference_preparation.add_to_do_item('sell tickets')

conference_preparation.remove_observer(nick)
conference_preparation.remove_to_do_item('make topics')


#2. Уявіть, що у вас є система керування розумним будинком, яка взаємодіє з різними пристроями через інтерфейси різних виробників. Однак у вас є новий пристрій, який використовує власний інтерфейс взаємодії, відмінний від стандартних інтерфейсів, що підтримуються системою. Ваше завдання – використовувати патерн "Адаптер", щоб інтегрувати цей новий пристрій у вашу систему управління розумним будинком.


class SmartHomeDevice(ABC) :

    @abstractmethod
    def turn_on(self):
        pass
    
    @abstractmethod
    def turn_off(self):
        pass

class SmartHomeDevice2023(SmartHomeDevice): # девайси 2023 року з однаковим інтерфейсом
    def __init__(self, name):
        self.name = name
    
    def turn_on(self):
        return f'{self.name} is turned on.'
    
    def turn_off(self):
        return f'{self.name} is turned off.'

class SmartSecurityCamera(SmartHomeDevice2023):
    pass

class SmartLighting(SmartHomeDevice2023):
    pass

class SmartSmokeDetector(SmartHomeDevice2023):
    pass

class SmartHomeDevice2024(): #девайси 2024 року з іншим інтерфейсом
    def __init__(self, name):
        self.name = name
    
    def switch_on(self):
        return f'{self.name} is switched on.'
    
    def switch_off(self):
        return f'{self.name} is switched off.'

class SmartRefrigerator(SmartHomeDevice2024):
    pass

class Adapter: #адаптує девайс 2023 року під систему 2023 року
    def __init__(self, adaptee: SmartHomeDevice2024):
        self.adaptee = adaptee
    
    def turn_on(self):
        return self.adaptee.switch_on()
    
    def turn_off(self):
        return self.adaptee.switch_off()
        
camera = SmartSecurityCamera('Camera')
light = SmartLighting('Light')
smoker_detactor = SmartSmokeDetector('Smoke detactor') 
refrigirator = SmartRefrigerator('Fridge')
adapter = Adapter(refrigirator)

devices = [camera, light, smoker_detactor, adapter]
for device in devices:
    print(device.turn_on())
    print(device.turn_off())

#3. Припустимо, у вас є клас Playlist, який представляє плейлист з піснями. Вам необхідно створити ітератор для обходу цього плейлиста.

class SongsSwitcher:
    def __init__(self, songs):
        self.__songs = songs
        self.__index = 0
    
    def __next__(self):
        if self.__index < len(self.__songs):
            item = self.__songs[self.__index]
            self.__index += 1
            return item
        else:
            raise StopIteration

class Playlist:
    def __init__(self):
        self.__songs = []
        
    def add(self, song):
        self.__songs.append(song)
    
    def __iter__(self):
        return SongsSwitcher(self.__songs)
    
my_playlist = Playlist()

my_playlist.add('"Someone Like You" by Adele')
my_playlist.add('"Thinking Out Loud" by Ed Sheeran')
my_playlist.add('"I Will Always Love You" by Whitney Houston')
my_playlist.add('"Smells Like Teen Spirit" by Nirvana')
my_playlist.add('"Stairway to Heaven" by Led Zeppelin')

for el in my_playlist:
    print(el)