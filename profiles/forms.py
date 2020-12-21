# Django
from django.forms import ModelForm

# local Django
from . import models


class ProfileCreationForm(ModelForm):

    """Profile Creation Form Definition """

    class Meta:
        model = models.Profile
        fields = [
            "nickname",
            "status_message",
            "image",
        ]