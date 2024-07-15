from django.urls import path
from . import views


urlpatterns = [
    path('posts/', views.PostsListCreate.as_view(), name='all_posts_view'),
    path('posts/<int:pk>/', views.PostsRetrieveUpdateDestroy.as_view(), name='posts_update_retrieve_destroy'),
    path('posts/comments/', views.CommentsListCreate.as_view(), name='all_comments_view'),
    path('posts/comments/<int:pk>/', views.CommentsRetrieveUpdateDestroy.as_view(), name='comments_update_retrieve_destroy'),
    path('posts/categories/', views.CategoriesListCreate.as_view(), name='all_categories_view'),
    path('posts/categories/<int:pk>/', views.CategoriesRetrieveUpdateDestroy.as_view(), name='categories_update_retrieve_destroy'),
]