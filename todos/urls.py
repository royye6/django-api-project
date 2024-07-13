from django.urls import path
from . import views

urlpatterns = [
    path('todos/', views.TodosListCreate.as_view(), name='todos_view'),
    path('todos/<int:pk>/', views.TodosRetrieveUpdateDestroy.as_view(), name='todos_update_retrieve_destroy_view'),
]