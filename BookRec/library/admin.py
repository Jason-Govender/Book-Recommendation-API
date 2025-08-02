from django.contrib import admin
from .models import Book
from .models import Book_Meta
from .models import Rating_Data

admin.site.register(Book_Meta)
admin.site.register(Book)
admin.site.register(Rating_Data)

