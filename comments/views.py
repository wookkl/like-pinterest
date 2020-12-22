# Django
from django.urls import reverse_lazy
from django.views.generic import CreateView

# local Django
from .models import Comment
from .forms import CommentCreateForm
from articles.models import Article


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
