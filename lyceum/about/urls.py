import django.urls

import about.views


app_name = 'about'
urlpatterns = [
    django.urls.path('', about.views.about, name='about'),
]
