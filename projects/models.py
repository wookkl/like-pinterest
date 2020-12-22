# Django
from django.db import models

# local Django


class Project(models.Model):

    """ Project Model Definition """

    title = models.CharField(max_length=20)
    description = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True, upload_to="project/")
    created_at = models.DateField(auto_now_add=True)
