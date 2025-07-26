from django.urls import path
from .views import BookListCreateView, BookRetrieveDestroyView

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookRetrieveDestroyView.as_view(), name='book-retrieve-destroy'),
]