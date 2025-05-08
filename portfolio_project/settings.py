"""
Django settings for portfolio_project project (Database-less version).
"""

from pathlib import Path
import os
import environ # Import django-environ

# Initialize django-environ
env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Take environment variables from .env file if it exists
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/stable/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY', default='django-insecure-fallback-key-for-db-less-demo')

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = env('DEBUG') # Reads from .env or defaults to False
DEBUG = 'True'
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['.herokuapp.com', '127.0.0.1', 'localhost'])


# Application definition

INSTALLED_APPS = [
    # 'django.contrib.admin', # Removed
    # 'django.contrib.auth', # Removed
    # 'django.contrib.contenttypes', # Removed
    # 'django.contrib.sessions', # Removed
    # 'django.contrib.messages', # Removed
    'django.contrib.staticfiles',
    # 'django.contrib.humanize', # Can be kept if you use its filters not dependent on DB
    'portfolio', # Our portfolio app
    'whitenoise.runserver_nostatic', # For serving static files with WhiteNoise
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # WhiteNoise middleware
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    # 'django.contrib.auth.middleware.AuthenticationMiddleware', # Removed
    # 'django.contrib.messages.middleware.MessageMiddleware', # Removed
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'portfolio_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                # 'django.contrib.auth.context_processors.auth', # Removed
                # 'django.contrib.messages.context_processors.messages', # Removed
            ],
        },
    },
]

WSGI_APPLICATION = 'portfolio_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/stable/ref/settings/#databases

# For a database-less setup, you can use an in-memory SQLite database
# or an empty dictionary if no Django components try to access it.
# Heroku might still expect DATABASE_URL, so dj_database_url can handle it.
import dj_database_url

DATABASES = {
    'default': dj_database_url.config(
        default=f"sqlite:///{os.path.join(BASE_DIR, 'db.sqlite3')}", # Fallback for local if needed
        conn_max_age=600
    )
}
# If Heroku sets DATABASE_URL to something like a dummy postgres URL, dj_database_url will parse it.
# If DATABASE_URL is not set, it falls back to the local SQLite.
# For a truly DB-less Heroku deployment where you don't want even a dummy Postgres:
# You might need to set DATABASE_URL in Heroku config vars to 'sqlite:///:memory:'
# or handle it more explicitly here:
# if 'DATABASE_URL' in os.environ:
#     DATABASES['default'] = dj_database_url.config(conn_max_age=600)
# else:
#     DATABASES['default'] = {'ENGINE': 'django.db.backends.sqlite3', 'NAME': ':memory:'}
# For this demo, let's assume Heroku might provide a DATABASE_URL, and we'll just configure it
# but not use it. Or, if it's not provided, it falls back to a local SQLite which also won't be used.
# The simplest for "no database interaction" is:
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': ':memory:',
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/stable/ref/settings/#auth-password-validators
# Not needed as auth app is removed.
# AUTH_PASSWORD_VALIDATORS = [ ... ]


# Internationalization
# https://docs.djangoproject.com/en/stable/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/stable/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') # For collectstatic and WhiteNoise

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'portfolio', 'static'), # Ensure app static dirs are found
]

# WhiteNoise configuration for static files in production
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# Media files (User uploads) - Not used in this database-less version
# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Default primary key field type
# https://docs.djangoproject.com/en/stable/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField' # Still good to have
