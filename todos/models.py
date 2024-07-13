from django.db import models


class Todos(models.Model):
    title = models.CharField(max_length=50)
    task = models.TextField(max_length=100)
    is_complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title