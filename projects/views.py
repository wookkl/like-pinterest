# Django
from django.shortcuts import render
from django.views.generic import DetailView, CreateView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.list import MultipleObjectMixin

# local Django

from .models import Project
from .form import ProjectCreateForm
from articles.models import Article
from subscriptions.models import Subscription


@method_decorator(login_required, "get")
@method_decorator(login_required, "post")
class ProjectCreateView(CreateView):

    """ Project Create View """

    model = Project
    template_name = "projects/create.html"
    form_class = ProjectCreateForm

    def get_success_url(self):
        return reverse_lazy("projects:detail", kwargs={"pk": self.object.pk})


class ProjectListView(ListView):

    """ Project List View """

    model = Project
    template_name = "projects/list.html"
    context_object_name = "project_list"
    paginate_by = 50
    paginate_orphans = 5


class ProjectDetailView(DetailView, MultipleObjectMixin):

    """ Project Detail View """

    model = Project
    template_name = "projects/detail.html"
    context_object_name = "target_project"
    paginate_by = 25
    paginate_orphans = 5

    def get_context_data(self, **kwargs):
        object_list = Article.objects.filter(project=self.get_object())
        project = self.object
        user = self.request.user
        if user.is_authenticated:
            subscription = Subscription.objects.filter(project=project, user=user)

        return super(ProjectDetailView, self).get_context_data(
            object_list=object_list, subscription=subscription, **kwargs
        )
