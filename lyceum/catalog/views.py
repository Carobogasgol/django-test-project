import django.shortcuts

__all__ = []


def item_list(request):
    template = 'catalog/list.html'

    context = {}
    return django.shortcuts.render(request, template, context)


def item_detail(request, pk):
    return django.shortcuts.render(request, 'catalog/detail.html')
