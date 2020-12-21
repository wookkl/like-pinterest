# Django
from django.urls import path

# local Django
from . import views

app_name = "profiles"

urlpatterns = [
    path("create/", views.ProfileCreateView.as_view(), name="create"),
    path("update/<int:pk>", views.ProfileUpdateView.as_view(), name="update"),
]