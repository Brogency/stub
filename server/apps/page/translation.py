# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from modeltranslation.translator import translator, TranslationOptions
from django.contrib.flatpages.models import FlatPage


class FlatPageTranslationOptions(TranslationOptions):
    fields = ('title', 'content', 'header_text',)


translator.register(FlatPage, FlatPageTranslationOptions)
