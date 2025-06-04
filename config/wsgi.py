"""
WSGI config for network_management_system project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from decouple import config  # Load environment variables from .env file

os.environ.setdefault('DJANGO_SETTINGS_MODULE', config('DJANGO_SETTINGS_MODULE'))

application = get_wsgi_application()
