1. Создал виртуальное окружение:
   PS D:\MyPython\MyProjects\LibraryOOP> python -m venv venv

2. Активировал виртуальное окружение:
   PS D:\MyPython\MyProjects\LibraryOOP> venv\Scripts\activate
   (venv) PS D:\MyPython\MyProjects\LibraryOOP>

3. Создал пакет library.

4. В library создал 4 модуля:
   __init__ - чтобы директория library определялась как пакет.
   book - модуль для книг.
   library - модуль для библиотеки книг.
   user - для читателей.

5. Создал директорию tests для проверки проекта. Внутри создал модуль __init__ для того,
   чтобы директория стала пакетом.

6. Создал файл .gitignore для того, чтобы поместить туда файлы, которые не нужно
   выгружать в GitHub.

7. Создал файл Requirements.txt для импорта библиотек, нужных для проекта.
   В консоли прописал: pip freeze > requirements.txt

8. Создал файл ReadMe.md для технического описания проекта.

9. В модуле library создал класс Library с методами поведения:
   class Library:
    def __init__(self):
        self.books = [] в этот список будут добавляться книги с помощью метода add_book
        self.users = [] в этот список будут добавляться читатели с помощью метода register_user

    def add_book(self, book):
        self.books.append(book)
        return f"книга {book} добавлена"

    def register_user(self, user):
        self.users.append(user)
        return f"читатель {user} зарегистрирован"

    def list_available_books(self):
        available_books = [book for book in self.books if book.is_available]
        if len(available_books) <= 0:
            return f"Книг нет"
        return f"Список доступных книг: \n" + '\n'.join(str(book) for book in available_books)


10. В модуле book создал класс Book и метод __str__ для описания объекта класса.

   class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.is_available = True # Это не обязательный параметр в __init__, сделан для дальнейшего написания
                                   метода borrow_book

    def __str__(self):
        return f"Книга: {self.title}, автор: {self.author}, год выпуска книги: {self.year}"

11. В модуле user создал класс User и методы поведения:
class User:
    def __init__(self, name, lastname, phone):
        self.name = name
        self.lastname = lastname
        self.phone = phone
        self.borrowed_books = []

    def __str__(self):
        return (f"Читатель: {self.name} {self.lastname},"
                f" взял книги {', '.join([b.title for b in self.borrowed_books])}")

    def borrow_book(self, book):
        if book.is_available:
            book.is_available = False
            self.borrowed_books.append(book)
            return f"{self.name} взял книгу {book.title}"
        return f"Книга {book.title} в наличии"

    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_available = True
            self.borrowed_books.remove(book)
            return f"{self.name} вернул книгу {book.title}"
        return f"Книги {book.title} нет в наличии"
    
12. В модуле main импортировал классы Library, Book, User:
    from library.book import Book
    from library.library import Library
    from library.user import User

13. Создал функцию main() для создания объектов классов.
    def main(): 
    library = Library()
    library.add_book(Book("Колобок", "А. Толстой", "1965"))
    library.add_book(Book("Три мушкетера", "А. Дюма", "1844"))
    library.add_book(Book("Война и мир", "Л. Толстой", "1867"))

    user1 = User("Вася", "Пупкин", 375295656855)
    user2 = User("Петя", "Смирнов", 375296586987)
    user = User("Миша", "Сидоров", 375294587956)
    library.register_user(user)

14. Запуск проекта:
    if __name__ == "__main__":
    main()

Коммит для гита 17:11
Коммит для гита 17:14
Коммит для гита 17:28
Коммит для гита 18:18