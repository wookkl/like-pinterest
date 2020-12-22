# Django
from django.urls import path

# local Django
from . import views

app_name = "projects"

urlpatterns = [
    path("create/", views.ProjectCreateView.as_view(), name="create"),
    path("detail/<int:pk>/", views.ProjectDetailView.as_view(), name="detail"),
    path("", views.ProjectListView.as_view(), name="list"),
]
