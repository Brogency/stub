# -*- coding: utf-8 -*-

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.flatpages',
    'grappelli',
    'django.contrib.admin',
    'easy_thumbnails',
    'modeltranslation_grappelli',
    'redactor',
    'codemirror',
    'daterange_filter',
)

LOCAL_APPS = (
    'main',
    'filestorage',
    'page',
)
MIGRATION_PATH = 'config.migrations.'

MIGRATION_MODULES = {
    'flatpages': MIGRATION_PATH + 'flatpages',
}

for item in LOCAL_APPS:
    MIGRATION_MODULES[item] = MIGRATION_PATH + item
    INSTALLED_APPS += ('apps.{0}'.format(item),)

