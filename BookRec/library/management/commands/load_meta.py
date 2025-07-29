from django.core.management.base import BaseCommand, CommandError
from library.models import Book_Meta
import json

class Command(BaseCommand):
    help = "Storage for book meta data."

    def add_arguments(self, parser):
        parser.add_argument('books', type=str, help="C:/Users/jason/OneDrive/Documents/Python QT/BookRec/BookRec/jupyter_export")

    def handle(self, *args, **kwargs):

        books = kwargs['books']

        with open(books, 'r', encoding='utf-8') as f:
            data = json.load(f)

        for entry in data:
            Book_Meta.objects.create(
                book_id=entry['book_id'],
                title=entry['title'],
                author=entry['author'],
                average_rating=entry['average_rating'],
                ratings_count=entry['ratings_count'],
                url=entry['url'],
                small_url=entry['small_url']

            )

        self.stdout.write(self.style.SUCCESS(f"Loaded {len(data)} books into the database."))