# Django
from django.urls import path
from django.views.generic import TemplateView

# local Django
from articles import views

app_name = "core"

urlpatterns = [path("", views.ArticleListView.as_view(), name="home")]
