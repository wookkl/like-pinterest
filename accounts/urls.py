# Django
from django.urls import path
from django.contrib.auth.models import User

# local Django
from . import views

app_name = "accounts"

urlpatterns = [
    path("create/", views.AccountCreateView.as_view(), name="create"),
    path("login/", views.AccountLoginView.as_view(), name="login"),
    path("logout/", views.AccountLogoutView.as_view(), name="logout"),
    path("<int:pk>/", views.AccountDetailView.as_view(), name="detail"),
    path("update/<int:pk>/", views.AccountUpdateView.as_view(), name="update"),
    path("delete/<int:pk>/", views.AccountDeleteView.as_view(), name="delete"),
]
