# Python
import os
import requests
import random

# Django
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.list import MultipleObjectMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

# local Django
from .forms import AccountUpdateForm
from .decorators import account_ownership_required, unusable_password_required
from articles.models import Article
from profiles.models import Profile

ownership_decorators = [login_required, account_ownership_required]
update_password_decorator = [
    login_required,
    account_ownership_required,
    unusable_password_required,
]


def get_random_nickname():
    random_number = random.randint(100000, 1000000)
    return "#USER" + str(random_number)


class AccountCreateView(SuccessMessageMixin, CreateView):

    """ Account Create View Definition """

    model = User
    form_class = UserCreationForm
    template_name = "accounts/create.html"
    success_message = "Created successfully"

    def form_valid(self, form):
        valid = super().form_valid(form)
        nickname = get_random_nickname()
        user_profile = Profile.objects.create(user=self.object, nickname=nickname)
        user_profile.save()
        login(self.request, self.object)
        return valid

    def get_success_url(self):
        pk = self.object.pk
        return reverse_lazy("accounts:detail", kwargs={"pk": pk})


class KakaoException(Exception):
    pass


def login_kakao(request):

    redirect_uri = "http://127.0.0.1:8000/accounts/login/kakao/callback"
    rest_api_key = os.environ.get("KAKAO_REST_API_KEY")
    return redirect(
        f"https://kauth.kakao.com/oauth/authorize?client_id={rest_api_key}&redirect_uri={redirect_uri}&response_type=code"
    )


def kakao_callback(request):
    try:
        code = request.GET.get("code", None)
        if code is not None:
            client_id = os.environ.get("KAKAO_REST_API_KEY")
            redirect_uri = "http://127.0.0.1:8000/accounts/login/kakao/callback"

            access_token = (
                requests.post(
                    f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={client_id}&redirect_uri={redirect_uri}&code={code}",
                    headers={"Content-Type": "application/json;charset=UTF-8"},
                )
                .json()
                .get("access_token", None)
            )
            if access_token is not None:
                user_profile = requests.post(
                    "https://kapi.kakao.com/v2/user/me",
                    headers={
                        "Authorization": f"Bearer {access_token}",
                        "Content-type": "application/x-www-form-urlencoded;charset=utf-8",
                    },
                ).json()
                email = user_profile.get("kakao_account").get("email", None)
                if email is not None:
                    try:
                        user = User.objects.get(username=email, email=email)
                    except User.DoesNotExist:
                        user = User.objects.create(username=email, email=email)
                        user.set_unusable_password()
                        user.save()
                        nickname = get_random_nickname()
                        user_profile = Profile.objects.create(
                            user=user, nickname=nickname
                        )
                        user_profile.save()
                    login(request, user)
                    messages.info(request, "Welcome")
                    return redirect(reverse("core:home"))
                else:
                    raise KakaoException("user's info")
            else:
                raise KakaoException("token")
        else:
            raise KakaoException("code")
    except KakaoException as e:
        err = "Can't get " + str(e)
        messages.error(request, err)
        return redirect(reverse("accounts:login"))


class GithubException(Exception):
    pass


def login_github(request):
    client_id = os.environ.get("GH_CLIENT_ID")
    scope = "user:email"
    redirect_uri = "http://127.0.0.1:8000/accounts/login/github/callback"
    return redirect(
        f"https://github.com/login/oauth/authorize?client_id={client_id}&scope={scope}&redirect_uri={redirect_uri}"
    )


def github_callback(request):
    try:
        code = request.GET.get("code", None)
        if code is not None:
            client_id = os.environ.get("GH_CLIENT_ID")
            client_secret = os.environ.get("GH_CLIENT_SECRET")
            access_token = (
                requests.post(
                    f"https://github.com/login/oauth/access_token?client_id={client_id}&client_secret={client_secret}&code={code}",
                    headers={"Accept": "application/json"},
                )
                .json()
                .get("access_token", None)
            )
            if access_token is not None:
                user_json = requests.get(
                    "https://api.github.com/user",
                    headers={"Authorization": f"token {access_token}"},
                ).json()
                email = user_json.get("email", None)
                if email is not None:
                    try:
                        user = User.objects.get(username=email, email=email)
                    except User.DoesNotExist:
                        user = User.objects.create(username=email, email=email)
                        user.set_unusable_password()
                        nickname = get_random_nickname()
                        user_profile = Profile.objects.create(
                            user=user, nickname=nickname
                        )
                        user_profile.save()
                        user.save()
                    login(request, user)
                    messages.info(request, "Welcome")
                    return redirect(reverse("core:home"))
                else:
                    raise GithubException("user's info")
            else:
                raise GithubException("token")
        else:
            raise GithubException("code")
    except GithubException as e:
        err = "Can't get " + str(e)
        messages.error(request, err)
        return redirect(reverse("accounts:login"))


class AccountLoginView(SuccessMessageMixin, LoginView):

    """ Account Log in View Definition """

    template_name = "accounts/login.html"

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.info(self.request, "Welcome")
        return response


@method_decorator(login_required, "get")
@method_decorator(login_required, "post")
class AccountLogoutView(SuccessMessageMixin, LogoutView):

    """ Account Log out View Definition """

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.info(self.request, "Welcome")
        return response


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


@method_decorator(update_password_decorator, "get")
@method_decorator(update_password_decorator, "post")
class AccountUpdateView(SuccessMessageMixin, UpdateView):

    """ Account Update View Definition """

    model = User
    form_class = AccountUpdateForm
    context_object_name = "target_user"
    template_name = "accounts/update.html"
    success_message = "Updated successfully"

    def get_success_url(self):
        pk = self.object.pk
        return reverse_lazy("accounts:detail", kwargs={"pk": pk})


@method_decorator(ownership_decorators, "get")
@method_decorator(ownership_decorators, "post")
class AccountDeleteView(SuccessMessageMixin, DeleteView):

    """ Account Delete View Definition """

    model = User
    context_object_name = "target_user"
    success_url = reverse_lazy("accounts:login")
    template_name = "accounts/delete.html"
    success_message = "Deleted successfully"
