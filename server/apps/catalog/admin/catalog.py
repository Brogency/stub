# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from modeltranslation_grappelli.admin.mixin import CustomMinTabbedTranslationAdmin
from apps.filestorage.admin.filestorage import DocumentFileStorageInline
from apps.filestorage.admin.filestorage import ImageFileStorageInline
from ..models import Catalog


class CatalogAdmin(CustomMinTabbedTranslationAdmin):
    list_display = ('pk', 'title_ru', 'hidden', 'created',)
    list_editable = ('hidden', 'created',)
    list_filter = ('hidden', 'created',)
    list_display_links = ('pk', 'title_ru',)
    search_fields = ('title', 'short_description',)
    prepopulated_fields = {"slug": ("title",)}
    inlines = [
        DocumentFileStorageInline,
        ImageFileStorageInline,
    ]


admin.site.register(Catalog, CatalogAdmin)
