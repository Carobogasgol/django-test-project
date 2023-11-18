from django.utils.translation import gettext_lazy as _
import os
import pathlib

import dotenv

__all__ = []


dotenv.load_dotenv()


def load_bool(name, default):
    env_value = os.getenv(name, str(default)).lower()
    return env_value in ('true', 'yes', 'i', 'y', 't')


BASE_DIR = pathlib.Path(__file__).resolve().parent.parent

ALLOW_REVERSE = load_bool('DJANGO_ALLOW_REVERSE', True)


SECRET_KEY = os.getenv('DJANGO_SECRET', 'not_so_secret')

DEBUG = load_bool('DJANGO_DEBUG', True)

ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', '*').split(',')

# Application definition

INSTALLED_APPS = [
    'homepage.apps.HomepageConfig',
    'catalog.apps.CatalogConfig',
    'about.apps.AboutConfig',
    'core.apps.CoreConfig',
    'django_cleanup.apps.CleanupConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sorl.thumbnail',
    'ckeditor',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'lyceum.middleware.ReverseRussianMiddleware',
]

if DEBUG:
    INSTALLED_APPS.append('debug_toolbar')
    MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')

INTERNAL_IPS = os.getenv('DJANGO_INTERNAL_IPS', '127.0.0.1').split(',')

ROOT_URLCONF = 'lyceum.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'lyceum.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.'
        + 'UserAttributeSimilarityValidator',
    },
    {
        'NAME': (
            'django.contrib.auth.password_validation.MinimumLengthValidator'
        ),
    },
    {
        'NAME': (
            'django.contrib.auth.password_validation.CommonPasswordValidator'
        ),
    },
    {
        'NAME': (
            'django.contrib.auth.password_validation.NumericPasswordValidator'
        ),
    },
]

LANGUAGES = [
    ('en', _('English')),
    ('ru', _('Russian')),
]
LOCALE_PATHS = (BASE_DIR / 'locale', )

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static_dev']

MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = 'static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static_ck')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


CKEDITOR_BASEPATH = '/static/ckeditor/ckeditor/'
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
            [
                'NumberedList',
                'BulletedList',
                '-',
                'Outdent',
                'Indent',
                '-',
                'JustifyLeft',
                'JustifyCenter',
                'JustifyRight',
                'JustifyBlock',
            ],
            ['Link', 'Unlink'],
            ['RemoveFormat', 'Source'],
        ],
    },
}
