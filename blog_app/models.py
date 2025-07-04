from django.db import models

# Create your models here.

class Blog_Post(models.Model):

    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100, default="Unknown")

    def __str__(self):
        return self.title
