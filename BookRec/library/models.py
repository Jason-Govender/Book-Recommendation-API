from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    rating = models.FloatField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    read = models.BooleanField(default=False)



