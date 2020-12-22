# Django
from django.db import models
from django.contrib.auth.models import User

# local Django
from articles.models import Article


class Comment(models.Model):
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name="comment", null=True
    )
    writer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comment", null=True
    )
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
