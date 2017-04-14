# -*- coding: utf-8 -*-
from .base import *
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'tigertalk333db',
        'USER': 'tiger',
        'PASSWORD': 'ttalk',
        'HOST': '',
        'PORT': '',
    }
}
