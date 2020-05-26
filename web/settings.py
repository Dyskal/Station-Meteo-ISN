from os.path import join, dirname, abspath

BASE_DIR = dirname(dirname(abspath(__file__)))

SECRET_KEY = 'a1yqk8@r)pm6i+j*ncxp^=rs^y*i_as-!d3c%h$+%vg1vay@1d'

DEBUG = True

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "82.64.251.1"]

INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'web.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [join(BASE_DIR, 'templates')],
    },
]

WSGI_APPLICATION = 'web.wsgi.application'

STATIC_ROOT = join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    join(BASE_DIR, 'static'),
)
