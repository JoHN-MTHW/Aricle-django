from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateField()
    is_locked = models.BooleanField(default=True)  
    is_deleted = models.BooleanField(default=False)  

    def __str__(self):
        return self.title


