import os

from dj_database_url import parse

from authorsanonymous.settings import *  # noqa

SECRET_KEY = 'super secret shhhhh'
DEBUG = True

ALLOWED_HOSTS = ['authorsanonymous.vcap.me', '*', 'localhost']
BASE_URL = 'http://authorsanonymous.vcap.me'

DATA_ROOT = os.getenv('TEST_DATA')

# Connect to the docker database by default, can be overridden in Travis.
DATABASES = {
    'default': parse(os.environ.get(
        'DATABASE_URL',
        'postgres://postgres@database/postgres',
    )),
}

MEDIA_ROOT = DATA_ROOT + 'media/'

# Disable email in testing
EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'
