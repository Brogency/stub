# -*- coding: utf-8 -*-
import apps.page.translation
from django.contrib import admin
from django.contrib.flatpages.models import FlatPage
from modeltranslation_grappelli.admin.mixin import CustomMinTabbedTranslationAdmin
from apps.filestorage.admin.filestorage import ImageFileStorageInline, \
    DocumentFileStorageInline
from apps.page.models import EditorTypesEnum


class PageAdmin(CustomMinTabbedTranslationAdmin):
    list_display = ("url", "title")
    fieldsets = (
        ("", {
            "fields": ("url", "title", "type_editor", "header_text", "content",
                       "sites"),
        }),
        ("Advanced options", {
            "fields": ("enable_comments",
                       "registration_required",
                       "template_name"),
        }),
    )
    inlines = [
        DocumentFileStorageInline,
        ImageFileStorageInline,
    ]

    def get_form(self, request, obj=None, **kwargs):
        form = super(PageAdmin, self).get_form(request, obj=obj, **kwargs)

        if obj is None:
            return form

        # getting editor widget and option for this
        editor, opts = EditorTypesEnum.get_editor(obj.type_editor)

        for field, value in form.base_fields.items():
            if "content" in field or "header_text" in field:
                opts.update({"attrs": form.base_fields[field].widget.attrs})
                form.base_fields[field].widget = editor(**opts)

        return form


admin.site.unregister(FlatPage)
admin.site.register(FlatPage, PageAdmin)
