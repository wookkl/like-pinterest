# Django
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

# local Django
from .models import Profile
from .forms import ProfileCreateForm, ProfileUpdateForm
from .decorators import profile_ownership_required

ownership_decorators = [login_required, profile_ownership_required]


@method_decorator(ownership_decorators, "get")
@method_decorator(ownership_decorators, "post")
class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreateForm
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


@method_decorator(ownership_decorators, "get")
@method_decorator(ownership_decorators, "post")
class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileUpdateForm
    context_object_name = "target_profile"
    template_name = "profile/update.html"

    def get_success_url(self):
        user_pk = self.request.user.pk
        return reverse_lazy("accounts:detail", kwargs={"pk": user_pk})
