# oop/library_system.py

class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def describe(self):
        return f"Book: {self.title} by {self.author}"

class EBook(Book):
    def __init__(self, title: str, author: str, file_size: int):
        super().__init__(title, author)
        self.file_size = int(file_size)

    def describe(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int):
        super().__init__(title, author)
        self.page_count = int(page_count)

    def describe(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

class Library:
    def __init__(self):
        self.books = []  # composition: contains Book objects

    def add_book(self, book):
        # optional type check:
        if not isinstance(book, Book):
            raise TypeError("Only Book (or subclasses) can be added")
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(book.describe())

