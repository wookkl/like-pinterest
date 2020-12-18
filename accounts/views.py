# Django
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse, reverse_lazy

# local Django
from . import models


class AccountCreateView(CreateView):
    model = models.Account
    form_class = UserCreationForm
    success_url = reverse_lazy("core:home")
    template_name = "accounts/create.html"
