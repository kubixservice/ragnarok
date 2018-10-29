import os
import logging
import commentjson
import paypalrestsdk

from . import __version__
from core.exceptions import RagnarokConfigError


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
formatter = '[%(levelname)s] %(asctime)s: %(name)s - %(message)s'
logging.basicConfig(filename='main.log', level=logging.DEBUG, format=formatter, filemode='w')
logger = logging.getLogger('alfheim.BasicLogger')

logger.debug('AlfheimPanel v{ver} started'.format(ver=__version__))

try:
    with open(os.path.join(BASE_DIR, 'alfheimproject/conf/config.json')) as config:
        CONFIG = commentjson.load(config)
except FileNotFoundError:
    raise RagnarokConfigError('config.json not found. Did you forgot to add it?')

try:
    with open(os.path.join(BASE_DIR, 'alfheimproject/conf/secrets.json')) as secrets:
        SECRETS = commentjson.load(secrets)
except FileNotFoundError:
    raise RagnarokConfigError('secrets.json not found. Did you forgot to add it?')

try:
    with open(os.path.join(BASE_DIR, 'alfheimproject/conf/donations.json')) as donations:
        DONATIONS = commentjson.load(donations)
except FileNotFoundError:
    raise RagnarokConfigError('donations.json not found. Did you forgot to add it?')

DEBUG = CONFIG['server']['conf']['debug']

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.{engine}'.format(engine=SECRETS['db_engine']),
        'NAME': SECRETS['db_database'],
        'USER': SECRETS['db_username'],
        'PASSWORD': SECRETS['db_password'],
        'HOST': SECRETS['db_host'],
        'PORT': SECRETS['db_port'],
    }
}

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
        'core.permissions.AllowHostOnly'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 20
}

paypalrestsdk.configure({
    "mode": DONATIONS['paypal']['mode'],
    "client_id": DONATIONS['paypal']['client_id'],
    "client_secret": DONATIONS['paypal']['client_secret']
})
