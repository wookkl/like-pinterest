# Django
from django.forms import ModelForm

# local Django
from . import models


class ProfileCreateForm(ModelForm):

    """Profile Create Form Definition """

    class Meta:
        model = models.Profile
        fields = [
            "nickname",
            "status_message",
            "image",
        ]


class ProfileUpdateForm(ModelForm):

    """Profile Update Form Definition """

    class Meta:
        model = models.Profile
        fields = [
            "nickname",
            "status_message",
            "image",
        ]
