from book import Book

def format_book_data(book: Book) -> str:
    return f"Название: {book.title}, Автор: {book.author}, Жанр: {book.genre}"