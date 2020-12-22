# Django
from django.forms import ModelForm

# local Django
from .models import Project


class ProjectCreateForm(ModelForm):

    """ Project Create Form Definition """

    class Meta:
        model = Project
        fields = [
            "title",
            "description",
            "image",
        ]


class ProjectUpdateForm(ModelForm):

    """ Project Update Form Definition """

    class Meta:
        model = Project
        fields = [
            "title",
            "description",
            "image",
        ]
