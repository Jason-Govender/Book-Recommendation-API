from django.urls import path
from .views import BookList, RatingList, RecommendView, MetaList

urlpatterns = [
    path('books/', BookList, name='book-list-create-destroy'),
    path('ratings/', RatingList, name='rating-list-create-update-destroy'),
    path('search/', MetaList, name='retrieve-list'),
    path('recommend/', RecommendView.as_view(), name='recommend-list'),
]