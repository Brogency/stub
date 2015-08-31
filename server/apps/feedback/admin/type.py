# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from apps.feedback.models import Type


class TypeAdmin(admin.ModelAdmin):
    list_display = ('slug', 'email', 'title')


admin.site.register(Type, TypeAdmin)
