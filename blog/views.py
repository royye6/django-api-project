from django.shortcuts import render
from rest_framework import generics
from .models import Posts
from .serializers import PostsSerializer, CommentsSerializer, CategoriesSerializer


