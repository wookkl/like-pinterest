# Django
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

    """ Profile Model Definition """

    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    nickname = models.CharField(max_length=20, unique=True)
    status_message = models.CharField(max_length=255, blank=True, default="")
    image = models.ImageField(blank=True, null=True, upload_to="profile/")
