"""
WSGI config for typeidea project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

project_env = os.environ.get('PROJECT_PROFILE', 'develop')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "student_sys.settings.%s" % project_env)

application = get_wsgi_application()
