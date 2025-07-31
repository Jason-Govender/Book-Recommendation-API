from rest_framework import viewsets, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from Recommender import recommend
from .models import Book, Book_Meta, Rating_Data
from .serializer import BookSerializer, BookMetaSerializer, RatingDataSerializer

class BookList(viewsets.modelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class MetaList(viewsets.modelViewSet):
    queryset = Book_Meta.objects.all()
    serializer_class = BookMetaSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'author']

class RatingList(viewsets.modelViewSet):
    queryset = Rating_Data.objects.all()
    serializer_class = RatingDataSerializer

class RecommendView(APIView):
    def get(self, request):
        recommendation = recommend()
        serializer = BookMetaSerializer(recommendation, many=True)
        return Response(serializer.data)





