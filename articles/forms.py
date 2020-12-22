# Django
from django.forms import ModelForm

# local Django
from .models import Article


class ArticleCreateForm(ModelForm):

    """ Article Create Form Definition """

    class Meta:
        model = Article
        fields = [
            "title",
            "image",
            "content",
            "project",
        ]


class ArticleUpdateForm(ModelForm):

    """ Article Update Form Definition """

    class Meta:
        model = Article
        fields = [
            "title",
            "image",
            "content",
            "project",
        ]
