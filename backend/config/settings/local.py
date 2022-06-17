from .base import *

DEBUG = True

INSTALLED_APPS += ['debug_toolbar', ]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']