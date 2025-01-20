class Library:
    def __init__(self):
        self.books = []
        self.users = []

    # def __str__(self):
    #     return f"Книга: {self.book}, читатель: {self.user}"

    # def user_book(self, book, user):
    #     if book in user:
    #         return f"Книга: {self.book} на руках у {self.user}"
    #     else:
    #         return f"Книга в наличии"

    def add_book(self, book):
        self.books.append(book)
        return f"книга {book} добавлена"

    def register_user(self, user):
        self.users.append(user)
        return f"читатель {user} зарегистрирован"

    def list_available_books(self):
        available_books = [book for book in self.books if book.is_available]
        if len(available_books) <= 0:
            return f"Книги закончились"
        return f"Список доступных книг: \n" + '\n'.join(str(book) for book in available_books)


