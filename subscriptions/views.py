# Django
from django.views.generic import RedirectView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.urls import reverse

# local Django

from projects.models import Project
from .models import Subscription


@method_decorator(login_required, "get")
class SubscriptionRedirectView(RedirectView):

    """ Subscribe Redirect View Definition """

    def get_redirect_url(self, *args, **kwargs):
        return reverse(
            "projects:detail", kwargs={"pk": self.request.GET.get("project_pk")}
        )

    def get(self, request, *args, **kwargs):
        project = get_object_or_404(Project, pk=request.GET.get("project_pk"))
        user = self.request.user
        subscription = Subscription.objects.filter(project=project, user=user)

        if subscription.exists():
            subscription.delete()
        else:
            Subscription(user=user, project=project).save()
        return super(SubscriptionRedirectView, self).get(request, *args, **kwargs)
