# Django
from django.urls import path

# local Django
from . import views

app_name = "accounts"

urlpatterns = [
    path("helloworld/", views.hello_world, name="helloworld"),
]
