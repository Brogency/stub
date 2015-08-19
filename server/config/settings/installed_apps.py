# -*- coding: utf-8 -*-

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'grappelli',
    'django.contrib.admin',

)

LOCAL_APPS = (
    'apps.main',
)

INSTALLED_APPS += LOCAL_APPS
