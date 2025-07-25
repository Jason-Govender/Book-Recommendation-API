from book import Book
import json

class Library:
    def __int__(self):
        self._book_list = []

    def add_book(self, book: Book):
        self._book_list.append(book)
        self.save_books()

    def remove_book(self, book: Book):
        self._book_list.remove(book)
        self.save_books()

    def get_book_list(self):
        return self._book_list

    def search_by_title(self, title: str):
        title = title.lower()
        for book in self._book_list:
            if title == book.get_title().lower():
                return True
        return False

    def search_by_author(self, author: str):
        author = author.lower()
        for book in self._book_list:
            if author == book.get_author().lower():
                return True
        return False

    def save_books(self, filename="books.json"):
        data = [book.to_dict() for book in self._book_list]
        with open(filename, "w", encoding="utf-8") as f:json.dump(data, f, ensure_ascii=False, indent=4)

    def load_books(self, filename="books.json"):
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
        self._book_list = [Book.from_dict(book) for book in data]

