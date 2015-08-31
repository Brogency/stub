# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.sites.models import Site
from modeltranslation_grappelli.admin.mixin import CustomMinTabbedTranslationAdmin
import apps.page.translation
from django.contrib import admin
from django.contrib.flatpages.models import FlatPage
from apps.filestorage.admin.filestorage import ImageFileStorageInline, \
    DocumentFileStorageInline
from apps.page.models import EditorTypesEnum


class PageAdmin(CustomMinTabbedTranslationAdmin):
    list_display = ("url", "title")
    prepopulated_fields = {"url": ("title",)}
    fieldsets = (
        ("", {
            "fields": ("title", "url", "type_editor", "header_text", "content"),
        }),
    )
    inlines = [
        DocumentFileStorageInline,
        ImageFileStorageInline,
    ]

    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        if db_field.name == "sites":
            kwargs["initial"] = [Site.objects.get_current()]
        return super(PageAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_form(self, request, obj=None, **kwargs):
        form = super(PageAdmin, self).get_form(request, obj=obj, **kwargs)

        if obj is None:
            return form

        editor, opts = EditorTypesEnum.get_editor(obj.type_editor)

        for field, value in form.base_fields.items():
            if "content" in field or "header_text" in field:
                opts.update({"attrs": form.base_fields[field].widget.attrs})
                form.base_fields[field].widget = editor(**opts)

        return form


admin.site.unregister(FlatPage)
admin.site.register(FlatPage, PageAdmin)
