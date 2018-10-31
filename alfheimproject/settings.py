"""
Django settings for alfheim_panel project.

Generated by 'django-admin startproject' using Django 2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

from .local_settings import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = SECRETS['secret_key']

# Since this feature will be used often, we will provide a special variable for it.
# Is caching framework enabled? Check /alfheimproject/conf/config.json
CACHING = CONFIG['cache']['enabled']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main_api.apps.MainApiConfig',
    'core.apps.CoreConfig',
    'eamod_api.apps.EamodApiConfig',
    'donations_api.apps.DonationsApiConfig',
    'tools.apps.ToolsConfig',
    'rest_framework',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Cache entrie site?
if CONFIG['cache']['cache_entrie_site']:
    MIDDLEWARE.insert(0, 'django.middleware.cache.UpdateCacheMiddleware')
    MIDDLEWARE.append('django.middleware.cache.FetchFromCacheMiddleware')

ROOT_URLCONF = 'alfheimproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'alfheimproject.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'core.validators.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': CONFIG['security']['validation']['min_password_length']
        }
    },
    {
        'NAME': 'core.validators.MaximumLengthValidator',
        'OPTIONS': {
            'max_length': CONFIG['security']['validation']['max_password_length']
        }
    },
    {
        'NAME': 'core.validators.MinimumNumberValidator',
        'OPTIONS': {
            'min_num': CONFIG['security']['validation']['password_min_number']
        }
    },
    {
        'NAME': 'core.validators.MinimumLowerValidator',
        'OPTIONS': {
            'min_lower': CONFIG['security']['validation']['password_min_lower']
        }
    },
    {
        'NAME': 'core.validators.MinimumUpperValidator',
        'OPTIONS': {
            'min_upper': CONFIG['security']['validation']['password_min_upper']
        }
    },
    {
        'NAME': 'core.validators.MinimumSymbolValidator',
        'OPTIONS': {
            'min_symbol': CONFIG['security']['validation']['password_min_symbol']
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

PASSWORD_HASHERS = CONFIG['security']['master_account']['password_hashers']

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = CONFIG['server']['conf']['server_domain'] + '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# Mail settings
EMAIL_HOST = SECRETS['smtp']['email_host']
EMAIL_PORT = SECRETS['smtp']['email_port']
EMAIL_USE_SSL = SECRETS['smtp']['email_use_ssl']
EMAIL_HOST_USER = SECRETS['smtp']['email_host_user']
EMAIL_HOST_PASSWORD = SECRETS['smtp']['email_host_password']

if CACHING:
    CACHES = {
        'default': {
            'BACKEND': CONFIG['cache']['backend'],
            'LOCATION': os.path.join(BASE_DIR, CONFIG['cache']['storage_path']),
            'TIMEOUT': CONFIG['cache']['default_timeout'],
            'OPTIONS': {
                'MAX_ENTRIES': CONFIG['cache']['max_entries']
            }
        }
    }
