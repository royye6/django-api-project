from django.db import models


class Posts(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    post = models.TextField()
    category = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self) -> str:
        return f"{self.title}, {self.author}, {self.post}, {self.category}, {self.created_at}"


class Comments(models.Model):
    username = models.CharField(max_length=50)
    post_title = models.ForeignKey(to_field=Posts.title)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.username}, {self.comment}, {self.created_at}"
    

class Categories(models.Model):
    category = models.ForeignKey(to_field=Posts.category)
    total_posts_per_category = models.AutoField()

    def __str__(self) -> str:
        return f"{self.category}, {self.total_posts_per_category}"


