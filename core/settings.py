import os
from pathlib import Path
from datetime import timedelta
from decouple import config
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR,'templates')
print("base directory: ", BASE_DIR)
# STATIC_ROOT = os.path.join(BASE_DIR, "static")
DJANGO_SUPERUSER_USERNAME='admin' 
DJANGO_SUPERUSER_PASSWORD='admin.@' 
DJANGO_SUPERUSER_EMAIL="admin@happynation.com"
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = os.environ.get('SECRET_KEY') 
SECRET_KEY="django-insecure-y0goccaa0oss$gslh#w1-suxqk+i(y&d^k@gty60_a7p1(*b5j"

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'
DEBUG = True

ALLOWED_HOSTS = ["*"]
# hello added

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # apps
    "accounts",
    "challenges",
    "surveys",
    "prizes",
    "events",
    "how_it_works",
    "social_auth",

    # third party apps
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'social_django',
    'django_filters',
    'corsheaders',
    'ckeditor',
    'drf_yasg',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'django.middleware.locale.LocaleMiddleware'
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
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

WSGI_APPLICATION = 'core.wsgi.application'

X_FRAME_OPTIONS = 'SAMEORIGIN'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases


if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR,'db.sqlite3'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ.get('POSTGRES_DB'),
            'USER': os.environ.get('POSTGRES_USER'),
            'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
            'HOST': os.environ.get('POSTGRES_HOST'),
            'PORT': os.environ.get('POSTGRES_PORT'),
        }
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


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}


# JWT settings
REST_USE_JWT = True

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=1),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,
    "VERIFYING_KEY": None,
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
}


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

from django.utils.translation import gettext_lazy as _

LANGUAGE_CODE = 'en'

LANGUAGES = [
    ('en', _('English')),
    ('de', _('German')),
    ('es', _('Spanish')),
    ('fr', _('French')),
    # Add more languages as needed
]

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

TIME_ZONE = 'UTC'

USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
# STATIC_ROOT = BASE_DIR / STATIC_URL
if DEBUG:
    STATIC_ROOT = os.path.join(BASE_DIR, "static")
    
else:
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "static")
    ]

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'accounts.MyUser'

# Django email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_HOST_USER = 'lisa.yating@gmail.com'
EMAIL_HOST_PASSWORD = "fyro neyg mmnw lyld"
DEFAULT_FROM_EMAIL = 'lisa.yating@gmail.com'


SWAGGER_SETTINGS = {
    'USE_SESSION_AUTH': False,
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header',
        },
    },
    'PERSIST_AUTH': True,
}

# django-allauth settings
ACCOUNT_EMAIL_VERIFICATION = 'none'
SOCIALACCOUNT_EMAIL_VERIFICATION = 'none'
SOCIALACCOUNT_QUERY_EMAIL = True
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        },
        'OAUTH_PKCE_ENABLED': True,
    }
}

CORS_ALLOW_ALL_ORIGINS = True  # Allow requests from any origin
# added this
CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "PATCH",
    "POST",
    "PUT",
]
CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
    "cache-control",
    "pragma",
]
# or specify specific origins
# CORS_ALLOWED_ORIGINS = [
#     "http://localhost:8000",  # React development server
#     "http://68.183.71.87",
# ]


# SSL settings
# SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
USE_X_FORWARDED_HOST = True
USE_X_FORWARDED_PORT = True

# CSRF_COOKIE_DOMAIN = 'https://206.81.26.210'
# CSRF_COOKIE_SAMESITE = None


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '%(asctime)s - %(levelname)s - %(module)s - %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'logfile.log',
            'formatter': 'simple'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
    },
    'loggers': {
        'logger': {
            'handlers': ['file', 'console'],
            'level': 'DEBUG',
        },
    },
}
