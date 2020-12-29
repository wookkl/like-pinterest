# Django
from django.urls import path
from django.views.generic import TemplateView

# local Django
from articles.views import ArticleListView
from .views import switch_language

app_name = "core"

urlpatterns = [
    path("", ArticleListView.as_view(), name="home"),
    path("lang/", switch_language, name="switch-language"),
]
