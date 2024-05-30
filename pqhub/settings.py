"""
Django settings for pqhub project.

Generated by 'django-admin startproject' using Django 4.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
from decouple import config
from datetime import timedelta
from pathlib import Path
import os
import dj_database_url
import asyncio
import aioredis

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# postgres://tutcov_user:0RdsS2TrlF47jK03bBYHi8djODA5x1ez@dpg-cp7niao21fec73dm5d0g-a.oregon-postgres.render.com/tutcov

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-njr!v8g1qp09^a-w+e4gucn+!3%qfgt(ag96w^w+@=ytdj+iwb'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "*"]

# /manage.py spectacular --file schema.yml
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tutdb.apps.TutdbConfig',
    'authapp',
    'chat',
    'channels',
    'rest_framework',
    "drf_spectacular",
    'drf_yasg',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema", # new
    # 'DEFAULT_THROTTLE_CLASSES': [
    #     'tutdb.throttles.CustomUserRateThrottle',
    #     'rest_framework.throttling.UserRateThrottle'
    # ],
    # 'DEFAULT_THROTTLE_RATES': {
    #     'anon': '100/day',
    #     'user': '100/day'
    # },
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 2
}


SPECTACULAR_SETTINGS = {
"TITLE": "TUTCOV API Project",
"DESCRIPTION": "A comprehensive documentation on all endpoints in tutcov",
"VERSION": "1.0.0",
# OTHER SETTINGS
}




ASGI_APPLICATION = 'pqhub.asgi.application'


AUTHENTICATION_BACKENDS = [
    'pqhub.backends.CustomUserModelBackend',
    'django.contrib.auth.backends.ModelBackend',
]

AUTH_USER_MODEL = "authapp.User"


SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(hours=12),
    'SLIDING_TOKEN_LIFETIME': timedelta(hours=24),
    'SLIDING_TOKEN_REFRESH_LIFETIME_GRACE_PERIOD': timedelta(minutes=30),  # To allow refresh if within 30 mins of expiry
    'SLIDING_TOKEN_REFRESH_EPOCH_GRACE_PERIOD': timedelta(hours=1),  # To allow refresh if within 1 hour of epoch
}


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'pqhub.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'pqhub.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     # db for postgresql
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': config('DB_NAME'), # name of db
#         'USER': config('DB_USER'), # user of db
#         'PASSWORD': config('DB_PASSWORD'), # password of db
#         'HOST': 'localhost',
#         'PORT': '5432',
#     },
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


DATABASES['default'] = dj_database_url.parse("postgres://tutcov_user:0RdsS2TrlF47jK03bBYHi8djODA5x1ez@dpg-cp7niao21fec73dm5d0g-a.oregon-postgres.render.com/tutcov")


CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        # format: redis://redis-container-name:port/db-number
        "LOCATION": "redis://localhost:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    }
}

CHANNEL_LAYERS = {
    'default': {
    'BACKEND': 'channels_redis.core.RedisChannelLayer',
    'CONFIG': {
    'hosts': [('127.0.0.1', 6379)],
    },
    },
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'

TIME_ZONE = 'Africa/Lagos'


USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIR = [
    os.path.join(BASE_DIR, 'static'),
]

MEDIA_URL = "media/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Mail settings for smtp
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'  # Specify your SMTP server
# EMAIL_PORT = 587  # Port for sending emails (use 587 for TLS, 465 for SSL)
# EMAIL_USE_TLS = True  # Use TLS (True/False based on your email provider)
# EMAIL_USE_SSL = False  # Use SSL (True/False based on your email provider)
# EMAIL_HOST_USER = config('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
# DEFAULT_FROM_EMAIL = config('EMAIL_HOST_USER')  # Sender's email address

# APPEND_SLASH=False

DEFAULT_FROM_EMAIL = config("DEFAULT_FROM_EMAIL")
EMAIL_BACKEND = "sendgrid_backend.SendgridBackend"
SENDGRID_SANDBOX_MODE_IN_DEBUG = False
SENDGRID_API_KEY = config("NEW_SENDGRID_API_KEY")

# DEFAULT_FROM_EMAIL = config("DEFAULT_FROM_EMAIL")
# EMAIL_BACKEND = "sendgrid_backend.SendgridBackend"
# SENDGRID_SANDBOX_MODE_IN_DEBUG = False
# SENDGRID_API_KEY = config("NEW_SENDGRID_API_KEY")



EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = config('MY_EMAIL')
EMAIL_HOST_PASSWORD = config('MY_PASSWORD')
EMAIL_PORT = 587
EMAIL_DEBUG = True
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False


async def main():
    # Connect to your internal Redis instance using the REDIS_URL environment variable
    # The REDIS_URL is set to the internal Redis URL e.g. redis://red-343245ndffg023:6379
    redis = aioredis.from_url(os.environ['REDIS_URL'])
    await redis.set("my-key", "aioredis")
    value = await redis.get("my-key")
    print(value)


if __name__ == "__main__":
    asyncio.run(main())
    
