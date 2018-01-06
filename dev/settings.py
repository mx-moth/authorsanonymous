from dj_database_url import parse

from authorsanonymous.settings import *  # noqa

SECRET_KEY = 'super secret shhhhh'
DEBUG = True

ALLOWED_HOSTS = ['aa.vcap.me', '*', 'localhost']
BASE_URL = 'http://aa.vcap.me'

DATA_ROOT = '/app/data/'

DATABASES = {
    'default': parse('postgres://postgres@database/postgres'),
}

MEDIA_ROOT = DATA_ROOT + 'media/'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'mail'
EMAIL_PORT = 25
