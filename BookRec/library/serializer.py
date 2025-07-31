from rest_framework import serializers
from .models import Book
from .models import Book_Meta
from .models import Rating_Data
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class BookMetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book_Meta
        fields = '__all__'

class RatingDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating_Data
        fields = '__all__'