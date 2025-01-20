class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.is_available = True

    def __str__(self):
        return f"Книга: {self.title}, автор: {self.author}, год выпуска книги: {self.year}"
