# Django
from django.forms import ModelForm, Textarea

# local Django
from .models import Comment


class CommentCreateForm(ModelForm):

    """ Comment Create Form Definition """

    class Meta:
        model = Comment
        fields = [
            "content",
        ]
        widgets = {
            "content": Textarea(attrs={"placeholder": "comment"}),
        }
        labels = {"content": "comment"}
