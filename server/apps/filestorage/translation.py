# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from modeltranslation.translator import translator, TranslationOptions
from .models import FileStorage, Category


class FileStorageTranslationOptions(TranslationOptions):
    fields = ('description',)


class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


translator.register(FileStorage, FileStorageTranslationOptions)
translator.register(Category, CategoryTranslationOptions)
