# Django
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
    ListView,
)
from django.utils.decorators import method_decorator
from django.views.generic.edit import FormMixin
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin

# local Django
from .models import Article
from .decorators import article_ownership_required
from .forms import ArticleCreateForm, ArticleUpdateForm
from comments.forms import CommentCreateForm

ownership_decorators = [login_required, article_ownership_required]


@method_decorator(login_required, "get")
@method_decorator(login_required, "post")
class ArticleCreateView(SuccessMessageMixin, CreateView):

    """ Article Create View Definition """

    model = Article
    form_class = ArticleCreateForm
    template_name = "articles/create.html"
    success_message = "Created successfully"

    def form_valid(self, form):
        article = form.save(commit=False)
        article.writer = self.request.user
        article.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("articles:detail", kwargs={"pk": self.object.pk})


class ArticleDetailView(DetailView, FormMixin):

    """ Article Detail View Definition """

    model = Article
    template_name = "articles/detail.html"

    context_object_name = "target_article"
    form_class = CommentCreateForm


@method_decorator(ownership_decorators, "get")
@method_decorator(ownership_decorators, "post")
class ArticleUpdateView(SuccessMessageMixin, UpdateView):

    """Article Update View Definition """

    model = Article
    form_class = ArticleUpdateForm
    context_object_name = "target_article"
    template_name = "articles/update.html"
    success_message = "Updated successfully"

    def get_success_url(self):
        return reverse_lazy("articles:detail", kwargs={"pk": self.object.pk})


@method_decorator(ownership_decorators, "get")
@method_decorator(ownership_decorators, "post")
class ArticleDeleteView(SuccessMessageMixin, DeleteView):

    """Article Update View Definition """

    model = Article
    context_object_name = "target_article"
    template_name = "articles/delete.html"
    success_url = reverse_lazy("core:home")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.warning(self.request, "Deleted successfully")
        return response


class ArticleListView(ListView):

    """Article List View Definition """

    model = Article
    context_object_name = "article_list"
    template_name = "home.html"
    paginate_by = 25
    paginate_orphans = 5
