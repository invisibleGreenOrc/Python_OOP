from book import Book

def validate_book_data(book: Book) -> bool:
    if book.title and book.title.strip() and book.author and book.author.strip() and book.genre and book.genre.strip():
        return True
    return False