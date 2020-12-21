# Django
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic import CreateView

# local Django
from .models import Profile
from .forms import ProfileCreationForm


class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreationForm
    context_object_name = "target_profile"
    template_name = "profile/create.html"

    def get_success_url(self):
        user_pk = self.request.user.pk
        return reverse_lazy("accounts:detail", kwargs={"pk": user_pk})

    def form_valid(self, form):
        profile = form.save(commit=False)
        profile.user = self.request.user
        profile.save()
        return super().form_valid(form)
