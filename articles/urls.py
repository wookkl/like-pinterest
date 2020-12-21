# Django
from django.urls import path

# local Django
from . import views

app_name = "articles"

urlpatterns = [
    path("create/", views.ArticleCreateView.as_view(), name="create"),
    path("<int:pk>/", views.ArticleDetailView.as_view(), name="detail"),
    path("update/<int:pk>/", views.ArticleUpdateView.as_view(), name="update"),
    path("delete/<int:pk>/", views.ArticleDeleteView.as_view(), name="delete"),
]
