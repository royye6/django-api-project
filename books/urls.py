from django.urls import path
from . import views


urlpatterns = [
    path('books/', views.BookListCreate.as_view(), name='get_all_books'),
    path('books/<int:pk>/', views.BookRetrieveUpdateDestroy.as_view(), name='book_update_retrieve_destroy'),
    path('books/reviews/', views.ReviewListCreate.as_view(), name='get_all_reviews'),
    path('books/reviews/<int:pk>/', views.ReviewRetrieveUpdateDestroy.as_view(), name='review_update_retrieve_destroy'),
    path('books/authors/', views.AuthorListCreate.as_view(), name='get_all_authors'),
    path('books/authors/<int:pk>/', views.AuthorRetrieveUpdateDestroy.as_view(), name='author_update_retrieve_destroy'),
]