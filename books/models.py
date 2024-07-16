from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=50)
    authors = models.ManyToManyField(Author)
    edition = models.IntegerField()
    description = models.TextField(blank=True)
    language = models.CharField(max_length=20, default='en')
    publisher = models.CharField(max_length=50)
    publication_date = models.DateField()
    genre = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.title


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    content = models.TextField()
    rating = models.IntegerField(choices=((1, '1 Star'), (2, '2 Starts'), (3, '3 Stars'), (4, '4 Stars'), (5, '5 Stars')))
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.user.username}'s review for {self.book.title}"
    


