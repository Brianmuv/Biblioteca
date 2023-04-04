from .base import *
# SECURITY WARNING: don't run with debung tuner on in production!
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbbiblioteca',
        'USER' : 'brianmuv',
        'PASSWORD' : 'brianmuv2023',
        'HOST' : 'localhost',
        'PORT' : '5432'
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
