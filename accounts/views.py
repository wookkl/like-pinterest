# Django
from django.views.generic import CreateView, DetailView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User

# local Django
from . import forms


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy("core:home")
    template_name = "accounts/create.html"


class AccountLoginView(LoginView):
    template_name = "accounts/login.html"


class AccountLogoutView(LogoutView):
    pass


class AccountDetailView(DetailView):
    model = User
    template_name = "accounts/detail.html"
    context_object_name = "target_user"


class AccountUpdateView(UpdateView):
    model = User
    form_class = forms.AccountUpdateForm
    success_url = reverse_lazy("account:detail")
    template_name = "accounts/update.html"