# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from ..models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Category, CategoryAdmin)
