from library.book import Book # импорт класса из модуля book
from library.library import Library # импорт класса из модуля library
from library.user import User # импорт класса из модуля user

def main():
    library = Library()
    library.add_book(Book("Колобок", "А. Толстой", "1965"))
    library.add_book(Book("Три мушкетера", "А. Дюма", "1844"))
    library.add_book(Book("Война и мир", "Л. Толстой", "1867"))


    user1 = User("Вася", "Пупкин", 375295656855)
    user2 = User("Петя", "Смирнов", 375296586987)
    user = User("Миша", "Сидоров", 375294587956)
    library.register_user(user)

    # print(library.list_available_books())
    # print(user.borrow_book(library.books[0]))
    # print(user1.borrow_book(library.books[1]))
    # print(user2.borrow_book(library.books[2]))
    # print(library.list_available_books())
    print(user.return_book(library.books[0]))
    print(library.list_available_books())
    print(user1.return_book(library.books[1]))
    print(library.list_available_books())
    print(user2.return_book(library.books[2]))
    print(library.list_available_books())


if __name__ == "__main__":
    main()
