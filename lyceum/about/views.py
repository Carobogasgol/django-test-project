import django.shortcuts

__all__ = []


def about(request):
    template = 'about/about.html'
    context = {}
    return django.shortcuts.render(request, template, context)
