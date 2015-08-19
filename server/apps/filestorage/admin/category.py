# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from apps.filestorage.models import Category


class CategoryAdmin(admin.ModelAdmin):
    """Override this class or remove"""
    pass


admin.site.register(Category, CategoryAdmin)
