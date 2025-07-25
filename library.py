from book import Book

class Library:
    def __int__(self, book_list: list):
        self._book_list = book_list

    def add_book(self, book: Book):
        self._book_list.append(book)

    def remove_book(self, book: Book):
        self._book_list.remove(book)

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