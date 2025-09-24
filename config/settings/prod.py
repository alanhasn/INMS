from .base import *

# Production-specific settings
DEBUG = False
ALLOWED_HOSTS = [] 

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