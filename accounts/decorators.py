# Djangp
from django.http import HttpResponseForbidden
from django.contrib.auth.models import User


def account_ownership_required(func):

    """ Account Ownership requirement Decorator Definition """

    def decorated(request, *args, **kwargs):
        user = User.objects.get(pk=kwargs["pk"])
        if not user == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)

    return decorated
