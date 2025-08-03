from rest_framework import viewsets, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from .Recommender import recommend
from .models import Book, Book_Meta, Rating_Data
from .serializer import BookSerializer, BookMetaSerializer, RatingDataSerializer
#Defines and implements all API endpoints for functionality-
#through all three databases.

#Create, read, delete user's books.
class BookList(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

#Search by author or title
class MetaList(viewsets.ModelViewSet):
    queryset = Book_Meta.objects.all()
    serializer_class = BookMetaSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'author']

#Create, read and delete user ratings.
class RatingList(viewsets.ModelViewSet):
    queryset = Rating_Data.objects.all()
    serializer_class = RatingDataSerializer

#Returns the list of five recommendations
class RecommendView(APIView):
    def get(self, request):
        recommendation = recommend()
        serializer = BookMetaSerializer(recommendation, many=True)
        return Response(serializer.data)





