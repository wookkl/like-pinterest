# Django
from django.http import HttpResponseForbidden

# local Django
from .models import Comment


def comment_ownership_required(func):

    """ comment Ownership requirement Decorator Definition """

    def decorated(request, *args, **kwargs):
        comment = Comment.objects.get(pk=kwargs["pk"])
        if not comment.writer == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)

    return decorated
