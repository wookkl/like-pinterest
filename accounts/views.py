# Django
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.list import MultipleObjectMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

# local Django
from .forms import AccountUpdateForm
from .decorators import account_ownership_required
from articles.models import Article

ownership_decorators = [login_required, account_ownership_required]


class AccountCreateView(CreateView):

    """ Account Create View Definition """

    model = User
    form_class = UserCreationForm
    template_name = "accounts/create.html"

    def form_valid(self, form):
        valid = super().form_valid(form)
        login(self.request, self.object)
        return valid

    def get_success_url(self):
        pk = self.object.pk
        return reverse_lazy("accounts:detail", kwargs={"pk": pk})


class AccountLoginView(LoginView):

    """ Account Log in View Definition """

    template_name = "accounts/login.html"


@method_decorator(login_required, "get")
@method_decorator(login_required, "post")
class AccountLogoutView(LogoutView):

    """ Account Log out View Definition """

    pass


class AccountDetailView(DetailView, MultipleObjectMixin):

    """ Account Detail View Definition """

    model = User
    template_name = "accounts/detail.html"
    context_object_name = "target_user"
    paginate_by = 25
    paginate_orphans = 5

    def get_context_data(self, **kwargs):
        object_list = Article.objects.filter(writer=self.get_object())
        return super(AccountDetailView, self).get_context_data(
            object_list=object_list, **kwargs
        )


@method_decorator(ownership_decorators, "get")
@method_decorator(ownership_decorators, "post")
class AccountUpdateView(UpdateView):

    """ Account Update View Definition """

    model = User
    form_class = AccountUpdateForm
    context_object_name = "target_user"
    template_name = "accounts/update.html"

    def get_success_url(self):
        pk = self.object.user.pk
        return reverse_lazy("accounts:detail", kwargs={"pk": pk})


@method_decorator(ownership_decorators, "get")
@method_decorator(ownership_decorators, "post")
class AccountDeleteView(DeleteView):

    """ Account Delete View Definition """

    model = User
    context_object_name = "target_user"
    success_url = reverse_lazy("accounts:login")
    template_name = "accounts/delete.html"
