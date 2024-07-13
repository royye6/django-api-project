from django.shortcuts import render
from rest_framework import generics
from .models import Todos
from .serializers import TodosSerializer


class TodosListCreate(generics.ListCreateAPIView):
    queryset = Todos.objects.all()
    serializer_class = TodosSerializer


class TodosRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todos.objects.all()
    serializer_class = TodosSerializer
    lookup_field = 'pk'
