"""
WSGI config for protestmapping project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
import django
import django_postgrespool
import dj_static

from dj_static import Cling
from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "protestmapping.settings")

application = django.setup()
application = Cling(get_wsgi_application())
application = DjangoWhiteNoise(application)