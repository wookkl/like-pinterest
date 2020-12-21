# Django
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# local Django
from . import forms
from . import decorators

ownershtp_decorators = [login_required, decorators.account_ownership_required]


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


@method_decorator(ownershtp_decorators, "get")
@method_decorator(ownershtp_decorators, "post")
class AccountUpdateView(UpdateView):

    """ Account Update View Definition """

    model = User
    form_class = forms.AccountUpdateForm
    context_object_name = "target_user"
    success_url = reverse_lazy("account:detail")
    template_name = "accounts/update.html"


@method_decorator(ownershtp_decorators, "get")
@method_decorator(ownershtp_decorators, "post")
class AccountDeleteView(DeleteView):

    """ Account Delete View Definition """

    model = User
    context_object_name = "target_user"
    success_url = reverse_lazy("accounts:login")
    template_name = "accounts/delete.html"
