# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from modeltranslation.translator import translator, TranslationOptions
from .models import FileStorage


class FileStorageTranslationOptions(TranslationOptions):
    fields = ('description',)


translator.register(FileStorage, FileStorageTranslationOptions)
