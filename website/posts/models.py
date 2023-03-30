from django.db import models

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=50, unique=True)
    content = models.TextField()
    author = models.CharField(max_length=50)
    publication_date = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.title