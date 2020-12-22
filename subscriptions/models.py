# Django
from django.db import models
from django.contrib.auth.models import User

# local Django
from projects.models import Project


class Subscription(models.Model):

    """ Subscription Model Definition """

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="subscriptions"
    )
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="subscriptions"
    )

    class Meta:
        unique_together = ("user", "project")
