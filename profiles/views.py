# Django
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin

# local Django
from .models import Profile
from .forms import ProfileCreateForm, ProfileUpdateForm
from .decorators import profile_ownership_required

ownership_decorators = [login_required, profile_ownership_required]


@method_decorator(login_required, "get")
@method_decorator(login_required, "post")
class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreateForm
    context_object_name = "target_profile"
    template_name = "profile/create.html"

    def get_success_url(self):
        user_pk = self.object.user.pk
        return reverse_lazy("accounts:detail", kwargs={"pk": user_pk})

    def form_valid(self, form):
        profile = form.save(commit=False)
        profile.user = self.request.user
        profile.save()
        return super().form_valid(form)


@method_decorator(ownership_decorators, "get")
@method_decorator(ownership_decorators, "post")
class ProfileUpdateView(SuccessMessageMixin, UpdateView):
    model = Profile
    form_class = ProfileUpdateForm
    context_object_name = "target_profile"
    template_name = "profile/update.html"
    success_message = _("Updated successfully")

    def get_success_url(self):
        user_pk = self.object.user.pk
        return reverse_lazy("accounts:detail", kwargs={"pk": user_pk})
