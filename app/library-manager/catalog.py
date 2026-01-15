from utils import Book
from utils import validate_book_data

class Library:
    def __init__(self):
        self.books: list[Book] = []

    def add_book(self, book: Book) -> bool:
        if validate_book_data(book):
            self.books.append(book)
            return True
        return False

    def delete_books(self, book_title: str) -> None:
        self.books = [book for book in self.books if book.title != book_title]

    def find_books(self, title: str | None = None, author: str | None = None, genre: str | None = None) -> list[Book]:
        books = [book for book in self.books if (book.title == title or title is None) and (book.author == author or author is None) and (book.genre == genre or genre is None)]
        return books

    def get_books(self) -> list[Book]:
        return self.books