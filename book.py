class Book:
    def __init__(self, title: str, author: str, genre: str, isbn: int, rating: float):
        self._title = title
        self._author = author
        self._genre = genre
        self._isbn = isbn
        self._rating = rating
        self._read = False

    @property
    def title(self ):
        return self._title
    @title.setter
    def title(self, value):
        self._title = value
    @property
    def author(self ):
        return self._author
    @author.setter
    def author(self, value):
        self._author = value
    @property
    def genre(self ):
        return self._genre
    @genre.setter
    def genre(self, value):
        self._genre = value
    @property
    def get_isbn(self ):
        return self._isbn
    @get_isbn.setter
    def get_isbn(self, value):
        self._isbn = value
    @property
    def is_read(self):
        return self._read
    @is_read.setter
    def is_read(self, value):
        self._read = value
    @property
    def rating(self):
        return self._rating
    @rating.setter
    def rating(self, value):
        self._rating = value

