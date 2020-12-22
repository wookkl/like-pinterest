# Django
from django.forms import ModelForm

# local Django
from .models import Comment


class CommentCreateForm(ModelForm):

    """ Comment Create Form Definition """

    class Meta:
        model = Comment
        fields = [
            "content",
        ]
