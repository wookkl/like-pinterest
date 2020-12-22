# Django
from django.urls import path

# local Django
from .views import CommentCreateView

app_name = "comments"

urlpatterns = [
    path("create", CommentCreateView.as_view(), name="create"),
]
