from django.urls import path
from .views import BookList, RatingList, RecommendView, MetaList

urlpatterns = [
    path(
        'books/',
        BookList.as_view({'get': 'list', 'post': 'create',}),
        name='book-list-create'
    ),
    path(
        'books/<int:pk>/',
        BookList.as_view({'delete': 'destroy'}),
        name='book-list-destroy'
    ),
    path(
        'ratings/',
        RatingList.as_view({'get': 'list', 'post': 'create',}),
        name='rating-list-create-update-destroy'
    ),
    path(
        'ratings/<int:pk>/',
        RatingList.as_view({'put': 'update', 'delete': 'destroy'}),
        name='rating-list-create-update-destroy'
    ),
    path(
        'search/',
        MetaList.as_view({'get': 'list'}),
        name='retrieve-list'
    ),
    path(
        'recommend/',
        RecommendView.as_view(),
        name='recommend-list'
    ),
]