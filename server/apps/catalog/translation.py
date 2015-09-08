# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from modeltranslation.translator import translator, TranslationOptions
from .models import Catalog, Category


class CatalogTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description', 'description')


class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


translator.register(Catalog, CatalogTranslationOptions)
translator.register(Category, CategoryTranslationOptions)
