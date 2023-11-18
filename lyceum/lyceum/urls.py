import django.conf
import django.conf.urls.static
import django.contrib
import django.contrib.staticfiles.urls
import django.urls

import about.urls
import catalog.urls
import homepage.urls

urlpatterns = [
    django.urls.path('', django.urls.include(homepage.urls)),
    django.urls.path('admin/', django.contrib.admin.site.urls),
    django.urls.path('catalog/', django.urls.include(catalog.urls)),
    django.urls.path(
        'about/',
        django.urls.include(about.urls),
    ),
]

if django.conf.settings.DEBUG:
    if django.conf.settings.MEDIA_ROOT:
        urlpatterns += django.conf.urls.static.static(
            django.conf.settings.MEDIA_URL,
            document_root=django.conf.settings.MEDIA_ROOT,
        )
    urlpatterns += django.contrib.staticfiles.urls.staticfiles_urlpatterns()

if django.conf.settings.DEBUG:
    urlpatterns += (
        django.urls.path(
            '__debug__/',
            django.urls.include('debug_toolbar.urls'),
        ),
    )
