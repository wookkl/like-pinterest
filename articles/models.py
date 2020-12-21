from django.contrib.auth.models import User
from django.db import models


class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="article")
    title = models.CharField(max_length=150)
    content = models.TextField()
    image = models.ImageField(upload_to="article/")

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
