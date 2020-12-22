# Django
from django.contrib.auth.models import User
from django.db import models

# local Django
from projects.models import Project


class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="article")
    project = models.ForeignKey(
        Project, on_delete=models.SET_NULL, related_name="article", null=True
    )
    title = models.CharField(max_length=150)
    content = models.TextField()
    image = models.ImageField(upload_to="article/")

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
