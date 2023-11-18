import http

import django.http
import django.shortcuts

__all__ = []


def home(request):
    template = 'homepage/homepage.html'
    context = {}
    return django.shortcuts.render(request, template, context)


def coffee(request):
    return django.http.HttpResponse(
        'Я чайник',
        status=http.HTTPStatus.IM_A_TEAPOT,
    )
