from rest_framework import generics
from .models import Book
from .serializer import BookSerializer

class BookListCreateView(generics.ListCreateAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = Book.objects.all()
        author = self.request.query_params.get('author')
        title = self.request.query_params.get('title')
        if author:
            queryset = queryset.filter(author__icontains=author)
        if title:
            queryset = queryset.filter(title__icontains=title)
        return queryset

class BookRetrieveDestroyView(generics.RetrieveDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
