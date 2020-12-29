from django.http import HttpResponse
from django.utils import translation
from django.conf import settings


def switch_language(request):
    lang = request.GET.get("lang", None)
    if lang is not None:
        translation.activate(lang)

        response = HttpResponse(status=200)
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang)
        return response
    return HttpResponse(status=400)
