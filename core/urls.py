# Django
from django.urls import path
from django.views.generic import TemplateView

# local Django
from articles import views

app_name = "core"

urlpatterns = [path("", TemplateView.as_view(template_name="home.html"), name="home")]
