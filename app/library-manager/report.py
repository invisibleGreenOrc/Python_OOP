from catalog import Library
from utils import format_book_data

def generate_report(library: Library) -> str:
    books = library.get_books()

    if not books:
        return "Библиотека пуста."
    
    report_lines = ["Отчет по библиотеке:"]

    for book in books:
        report_lines.append(format_book_data(book))
    return "\n".join(report_lines)