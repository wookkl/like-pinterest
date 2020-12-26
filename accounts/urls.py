# Django
from django.urls import path

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
    path("login/github/", views.login_github, name="github-login"),
    path("login/github/callback", views.github_callback, name="github-callback"),
]
