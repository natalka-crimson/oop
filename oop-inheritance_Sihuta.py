
#1. Створіть клас Book з атрибутами, такими як назва книги та автор. Створіть підкласи для різних жанрів книг, наприклад, FictionBook, NonFictionBook, MysteryBook. Додайте атрибути та методи, що характеризують кожен жанр та можливо методи для роботи з книгами (наприклад, видача, повернення).

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True
    
    def take_book(self):
        self.is_available = False
    
    def return_book(self):
        self.is_available = True
    
    def __str__(self):
        if self.is_available:
            return f'The book "{self.title}" of {self.author} is available.'
        else:
            return f'The book "{self.title}" of {self.author} is not available.'


class FictionBook(Book):
    def __init__(self, title, author, plot_type, heroes: list, has_pictures: bool):
        super().__init__(title, author)
        self.plot_type = plot_type
        self.heroes = heroes
        self.has_pictures = has_pictures
    
    def characters(self):
        print(f'The main characters of the book are: {self.heroes}.')
        

class NonFictionBook(Book):
    def __init__(self, title, author, topic, facts):
        super().__init__(title, author)
        self.topic = topic
        self.facts = facts
    
    def present_facts(self):
        print(f'The book approves the following facts: {self.facts}.')

class MysteryBook(Book):
    def __init__(self, title, author, crime_type, criminal_name):
        super().__init__(title, author)
        self.crime_type = crime_type
        self.criminal_name = criminal_name
    
    def show_criminal(self):
        print(f'The crime was done by {self.criminal_name}.')


hunger_games = FictionBook('The Hunger Games', 'Suzanne Collins', 'dystopian adventure', ['Katniss Everdeen', 'Peeta Mellark', 'Gale Hawthorne'], False)
sapiens = NonFictionBook('Sapiens: A Brief History of Humankind', 'Yuval Noah Harari', 'human evolution', 'Homo sapiens are the dominant species on Earth due to their unique ability to communicate and cooperate in large groups')
girl_with_tattoo = MysteryBook('The Girl with the Dragon Tattoo', 'Stieg Larsson', 'disappearance of a woman', 'Martin Vanger')

girl_with_tattoo.take_book()
girl_with_tattoo.show_criminal()
hunger_games.characters()
sapiens.present_facts()
girl_with_tattoo.return_book()
print(girl_with_tattoo)


#2. Створіть клас Library з методами для видачі та повернення книг. Використовуйте поліморфізм при створенні функції, яка може видачу та повернення книги, безперечно працюючи з об'єктами різних типів. Також створіть клас Book та підкласи для різних жанрів. 

class Library:
    def __init__(self, name):
        self.name = name
        self.books_of_library = {}
    
    def __str__(self):
        if not self.books_of_library:
            return f'"{self.name}" library is empty at the moment.'
        books_list = '\n'.join([f'{author}: {', '.join(title)}' for author, title in self.books_of_library.items()])
        return f'"{self.name}" has the following books:\n{books_list}'
     
    def add_book(self, book):
        if book.author in self.books_of_library:
            self.books_of_library[book.author].append(book.title)
        else:
            self.books_of_library[book.author] = [book.title]
    
    def find_books_by_author(self, author):
        if author not in self.books_of_library:
            print('The author not found.')
            return
        
        print(f'The books of "{author}": ')
        
        for index, book in enumerate(self.books_of_library[author], start=1):
            print(f'\t{index}: {book};')
    
    def find_book_by_title(self, title):
        for author, author_books in self.books_of_library.items():
            if title in author_books:
                print(f'The book "{title}" of "{author}" was found.')
                break
        else:
            print('The book was not found.')
        
    def remove_book(self, title):
        for author, author_books in self.books_of_library.items():
            if title in author_books:
                author_books.remove(title)
                print(f'The book {title} of {author} has been removed from the library.')
                break
        else:
            print(f'The book {title} wsn not found.')
    
    def take_book(self, book):
        if book.author not in self.books_of_library:
            print('The book was not added to the library, you cannot take it.')
            return
        if book.title not in self.books_of_library[book.author]:
            print('The book was not added to the library, you cannot take it.')
            return
        if book.is_available:
            book.is_available = False
        else:
            print('The book is not available at the moment.')
    
    def return_book(self, book):
        if book.is_available:
            print('Wrong action.')
        else:
            book.is_available = True


class Book():
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True
    
    def __str__(self):
        if self.is_available:
            return f'The book "{self.title}" of {self.author} is available.'
        else:
            return f'The book "{self.title}" of {self.author} is not available.'

class FictionBook(Book):
    def __init__(self, title, author, plot_type, heroes: list, has_pictures: bool):
        super().__init__(title, author)
        self.plot_type = plot_type
        self.heroes = heroes
        self.has_pictures = has_pictures
    
    def characters(self):
        print(f'The main characters of the book are: {self.heroes}.')
        

class NonFictionBook(Book):
    def __init__(self, title, author, topic, facts):
        super().__init__(title, author)
        self.topic = topic
        self.facts = facts
    
    def present_facts(self):
        print(f'The book approves the following facts: {self.facts}.')

class MysteryBook(Book):
    def __init__(self, title, author, crime_type, criminal_name):
        super().__init__(title, author)
        self.crime_type = crime_type
        self.criminal_name = criminal_name
    
    def show_criminal(self):
        print(f'The crime was done by {self.criminal_name}.')


hunger_games = FictionBook('The Hunger Games', 'Suzanne Collins', 'dystopian adventure', ['Katniss Everdeen', 'Peeta Mellark', 'Gale Hawthorne'], False)
hunger_games_prequel = FictionBook('The Ballad of Songbirds and Snakes', 'Suzanne Collins', 'dystopian coming-of-age story', ['Coriolanus Snow', 'Lucy Gray Baird'], False)
sapiens = NonFictionBook('Sapiens: A Brief History of Humankind', 'Yuval Noah Harari', 'human evolution', 'Homo sapiens are the dominant species on Earth due to their unique ability to communicate and cooperate in large groups')
girl_with_tattoo = MysteryBook('The Girl with the Dragon Tattoo', 'Stieg Larsson', 'disappearance of a woman', 'Martin Vanger')


lib = Library('Glorya')
lib.add_book(hunger_games)
lib.add_book(hunger_games_prequel)
lib.add_book(girl_with_tattoo)
print(lib)
lib.take_book(sapiens)
lib.return_book(sapiens)
lib.take_book(hunger_games_prequel)
lib.take_book(hunger_games_prequel)