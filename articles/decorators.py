# Django
from django.http import HttpResponseForbidden

# local Django
from .models import Article


def article_ownership_required(func):

    """ Article Ownership requirement Decorator Definition """

    def decorated(request, *args, **kwargs):
        article = Article.objects.get(pk=kwargs["pk"])
        if not article.writer == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)

    return decorated
