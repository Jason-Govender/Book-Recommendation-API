from django.contrib import admin
from .models import Book
from .models import Book_Meta

admin.site.register(Book_Meta)
admin.site.register(Book)

