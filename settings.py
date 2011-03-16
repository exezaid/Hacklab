import os

PROJECT_PATH = os.path.dirname(__file__)
PROJECT_NAME = 'Lug Tucuman'
project_path_join = lambda x: os.path.normpath(os.path.join(PROJECT_PATH, x))


DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Ezequiel', 'exe.zaid@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'prueba',
        'USER': 'prueba',
        'PASSWORD': 'prueba',
        'HOST': '192.168.1.60',
        'PORT': '',
    }
}


TIME_ZONE = 'America/Argentina/Tucuman'

LANGUAGE_CODE = 'es-AR'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

MEDIA_ROOT = project_path_join('statics/media')

MEDIA_URL = '/media/'

ADMIN_MEDIA_PREFIX = '/admin/media/'

SECRET_KEY = '$zn0j*c8iod@vkqqdl6g=m#e!=+h)7kx3@szu0@f6_6&llpo2c'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    project_path_join('statics/templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.flatpages',
    'django.contrib.redirects',
    'django.contrib.humanize',
    'django.contrib.markup',
    'django.contrib.comments',
    'apps.blog',
)

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 587
