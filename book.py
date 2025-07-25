class Book:
    def __init__(self, title: str, author: str, genre: str, rating: float):
        self._title = title
        self._author = author
        self._genre = genre
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
    def to_dict(self):
        return {'title': self.title,
                'author': self.author,
                'genre': self.genre,
                'rating': self.rating,
                'is_read': self.is_read
        }

    def from_dict(self, data):
        self.title = data['title']
        self.author = data['author']
        self.genre = data['genre']
        self.rating = data['rating']
        self.is_read = data['is_read']



