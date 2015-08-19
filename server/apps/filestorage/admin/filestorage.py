# -*- coding: utf-8 -*-
import apps.filestorage.translation
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from modeltranslation_grappelli.admin.mixin import CustomMinTabbedTranslationAdmin
from .mixins.inline import FileStorageInlineMixin
from apps.filestorage.models import FileStorage


class FileStorageAdmin(CustomMinTabbedTranslationAdmin):
    list_display = ('__unicode__', 'extension', 'description', 'image_tag',)
    list_filter = ('extension',)
    readonly_fields = ('extension',)
    search_fields = ('document',)


admin.site.register(FileStorage, FileStorageAdmin)


class ImageFileStorageInline(FileStorageInlineMixin):
    verbose_name = _('image')
    verbose_name_plural = _('Images')
    file_type = 'image'
    fields = ('document', 'languages', 'order', 'image_tag',)
    readonly_fields = ['image_tag']


class DocumentFileStorageInline(FileStorageInlineMixin):
    verbose_name = _('document')
    verbose_name_plural = _('Documents')
    file_type = 'document'
