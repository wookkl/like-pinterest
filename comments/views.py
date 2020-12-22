# Django
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# local Django
from .models import Comment
from .forms import CommentCreateForm
from .decorators import comment_ownership_required
from articles.models import Article

ownership_decorators = [login_required, comment_ownership_required]


@method_decorator(login_required, "get")
@method_decorator(login_required, "post")
class CommentCreateView(CreateView):

    """ Comment Create View Definition """

    model = Comment
    form_class = CommentCreateForm
    template_name = "comments/create.html"

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.article = Article.objects.get(pk=self.request.POST["article_pk"])
        comment.writer = self.request.user
        comment.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("articles:detail", kwargs={"pk": self.object.article.pk})


@method_decorator(ownership_decorators, "get")
@method_decorator(ownership_decorators, "post")
class CommentDeleteView(DeleteView):

    """ Comment Delete View Definition """

    model = Comment
    context_object_name = "target_comment"
    template_name = "comments/delete.html"

    def get_success_url(self):
        return reverse_lazy("articles:detail", kwargs={"pk": self.object.article.pk})
