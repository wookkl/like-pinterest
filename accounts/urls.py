# Django
from django.urls import path

# local Django
from . import views

app_name = "accounts"

urlpatterns = [
    path("create/", views.AccountCreateView.as_view(), name="create"),
    path("login/", views.AccountLoginView.as_view(), name="login"),
    path("logout/", views.AccountLogoutView.as_view(), name="logout"),
]
