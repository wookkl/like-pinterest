# Django
from django.urls import path

# local Django
from .views import CommentCreateView, CommentDeleteView

app_name = "comments"

urlpatterns = [
    path("create/", CommentCreateView.as_view(), name="create"),
    path("delete/<int:pk>/", CommentDeleteView.as_view(), name="delete"),
]
