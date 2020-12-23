# Django
from django.forms import ModelForm
from django import forms

# local Django
from .models import Article
from projects.models import Project


class ArticleCreateForm(ModelForm):

    """ Article Create Form Definition """

    content = forms.CharField(
        widget=forms.Textarea(attrs={"class": "editable text-start"})
    )
    project = forms.ModelChoiceField(queryset=Project.objects.all(), required=False)

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

    content = forms.CharField(
        widget=forms.Textarea(attrs={"class": "editable text-start"})
    )
    project = forms.ModelChoiceField(queryset=Project.objects.all(), required=False)

    class Meta:
        model = Article
        fields = [
            "title",
            "image",
            "content",
            "project",
        ]
