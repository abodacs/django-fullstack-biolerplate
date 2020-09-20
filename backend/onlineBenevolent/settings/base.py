# https://docs.djangoproject.com/en/3.1/ref/settings/

import os
from datetime import timedelta
from pathlib import PurePath
from typing import Tuple

from django.utils.translation import ugettext_lazy as ugt

from decouple import config
from dj_database_url import parse as db_url


# Build paths inside the project like this: BASE_DIR.joinpath('some')
# `pathlib` is better than writing: dirname(dirname(dirname(__file__)))
# backend/
BASE_DIR = PurePath(__file__).parent.parent.parent


def base_dir_join(*args):
    return os.path.join(BASE_DIR, *args)


SITE_ID = 1

SECURE_HSTS_PRELOAD = True

DEBUG = True

SECRET_KEY = config("DJANGO_SECRET_KEY")

ADMINS = (("Admin", "foo@example.com"),)

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]

# APP CONFIGURATION
# ------------------------------------------------------------------------------
DJANGO_APPS: Tuple[str, ...] = (
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.admin",
)

LOCAL_APPS: Tuple[str, ...] = (
    "common",
    "apps.users",
    "apps.meta",
    "apps.projects",
    "apps.delivery",
)

THIRD_PARTY_APPS: Tuple[str, ...] = (
    "corsheaders",
    "rest_framework",
    "rest_framework_simplejwt.token_blacklist",
    # 'django_extensions',
)
# CORS
# ------------------------------------------------------------------------------
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True  # to accept cookies via ajax request
CORS_ORIGIN_WHITELIST = [
    # the domain for front-end app(you can add more than 1)
    "http://localhost:3000",
]
CORS_ALLOWED_ORIGIN_REGEXES = [
    r"^https://\w+\.heroku\.com$",
]

# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

AUTH_USER_MODEL = "users.User"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "onlineBenevolent.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [base_dir_join("templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

ASGI_APPLICATION = "onlineBenevolent.asgi.application"

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]

# DJANGO REST FRAMEWORK
# ------------------------------------------------------------------------------

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 20,
}

SIMPLE_JWT_SIGNING_KEY = config("SIMPLE_JWT_SIGNING_KEY", cast=str, default=SECRET_KEY)

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=1),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    "SIGNING_KEY": SIMPLE_JWT_SIGNING_KEY,
    "AUTH_HEADER_TYPES": ("Bearer",),
    "USER_ID_CLAIM": "id",
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
}

# Email
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    "default": config("DATABASE_URL", cast=db_url),
}
DATABASES["default"]["ENGINE"] = config("DATABASE_ENGINE", cast=str, default=None)
DATABASES["default"]["CONN_MAX_AGE"] = config("POSTGRES_CONN_MAX_AGE", cast=int, default=60)

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = (
    ("en", ugt("English")),
    ("ar", ugt("Arabic")),
)

STATICFILES_DIRS = (base_dir_join("static"),)

if DEBUG:
    INSTALLED_APPS += ("drf_yasg",)

    # drf_yasg
    SWAGGER_SETTINGS = {
        "DEFAULT_INFO": "onlineBenevolent.urls.api_info",
        "REFETCH_SCHEMA_WITH_AUTH": True,
        "SECURITY_DEFINITIONS": {
            "api_key": {"type": "apiKey", "in": "header", "name": "Authorization"}
        },
    }

# Celery
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_ACKS_LATE = True
CELERY_TIMEZONE = TIME_ZONE
