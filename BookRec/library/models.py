from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
import json
import os
BASE_DIR = settings.BASE_DIR
MODEL_DIR = os.path.join(BASE_DIR, "jupyter_export")
with open(os.path.join(MODEL_DIR, "books.json")) as f:
    book_meta = json.load(f)

class Book(models.Model):
    book_id = models.IntegerField(max_length=200)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    read = models.BooleanField(default=False)

class BOOK_META(models.Model):
    book_id = models.IntegerField(max_length=10)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    average_rating = models.FloatField(max_length=3)
    url = models.URLField(max_length=500)
    small_url = models.URLField(max_length=500)





