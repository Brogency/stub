# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from modeltranslation_grappelli.admin.mixin import CustomMinTabbedTranslationAdmin
from ..models import Category


class CategoryAdmin(CustomMinTabbedTranslationAdmin):
    list_display = ('name',)


admin.site.register(Category, CategoryAdmin)
