from decouple import Csv

from .base import *

# Production-specific settings
DEBUG = False
# Comma-separated in the env, e.g. ALLOWED_HOSTS=example.com,www.example.com
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='', cast=Csv())

# PostgreSQL Database for production
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('DB_NAME', default='INMS'),
        'USER': config('DB_USER', default='whoami'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST', default='localhost'),
        'PORT': config('DB_PORT', default='5432'),
    }
}

# Security hardening (see: python manage.py check --deploy)
# Assumes this is deployed behind HTTPS. If it's ever served over plain HTTP,
# SECURE_SSL_REDIRECT/HSTS below will break it -- don't enable until HTTPS is live.
SECURE_SSL_REDIRECT = config('SECURE_SSL_REDIRECT', default=True, cast=bool)
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = config('SECURE_HSTS_SECONDS', default=60 * 60 * 24 * 7, cast=int)  # 1 week to start
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True