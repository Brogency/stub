# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from modeltranslation.translator import translator, TranslationOptions
from .models import News, Category


class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description', 'description')


class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


translator.register(News, NewsTranslationOptions)
translator.register(Category, CategoryTranslationOptions)
