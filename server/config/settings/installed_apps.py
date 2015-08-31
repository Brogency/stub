# -*- coding: utf-8 -*-
from __future__ import unicode_literals

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
    'modeltranslation',
    'modeltranslation_grappelli',
    'redactor',
    'codemirror',
    'daterange_filter',
)

LOCAL_APPS = (
    'apps.main',
    'apps.filestorage',
    'apps.page',
    'apps.news',
    'apps.feedback',
)

INSTALLED_APPS += LOCAL_APPS

MIGRATION_PATH = 'config.migrations.'

MIGRATION_MODULES = {
    'flatpages': MIGRATION_PATH + 'flatpages',
    'filestorage': MIGRATION_PATH + 'filestorage',
}
