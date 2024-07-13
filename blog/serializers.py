from rest_framework import serializers
from .models import Posts, Comments, Categories


class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ['id', 'title', 'author', 'post', 'category', 'created_at']


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['id', 'username', 'post_title', 'comment', 'created_at']


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['id', 'category', 'total_posts_per_category']


