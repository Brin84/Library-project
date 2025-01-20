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
