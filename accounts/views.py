# Django
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User

# local Django
from . import forms


class AccountCreateView(CreateView):

    """ Account Create View Definition """

    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy("core:home")
    template_name = "accounts/create.html"


class AccountLoginView(LoginView):

    """ Account Log in View Definition """

    template_name = "accounts/login.html"


class AccountLogoutView(LogoutView):

    """ Account Log out View Definition """

    pass


class AccountDetailView(DetailView):

    """ Account Detail View Definition """

    model = User
    template_name = "accounts/detail.html"
    context_object_name = "target_user"


class AccountUpdateView(UpdateView):

    """ Account Update View Definition """

    model = User
    form_class = forms.AccountUpdateForm
    success_url = reverse_lazy("account:detail")
    template_name = "accounts/update.html"


class AccountDeleteView(DeleteView):

    """ Account Delete View Definition """

    model = User
    success_url = reverse_lazy("accounts:login")
    template_name = "accounts/delete.html"
