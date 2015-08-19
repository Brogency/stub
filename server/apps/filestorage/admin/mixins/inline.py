# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.contenttypes.generic import GenericTabularInline
from grappelli.forms import GrappelliSortableHiddenMixin

from apps.filestorage.models.filestorage import RelativeFileStorage
from apps.filestorage.models.mixins.image import ImageThumbnailMixin


class FileStorageInlineMixin(GrappelliSortableHiddenMixin,
                             GenericTabularInline):
    FILE_TYPES = ('image', 'document',)

    model = RelativeFileStorage
    fields = ()
    raw_id_fields = ('document',)
    sortable_field_name = 'order'
    file_type = None

    autocomplete_lookup_fields = {
        'fk': ['document'],
    }

    def get_queryset(self, request):
        if self.file_type is None or self.file_type not in self.FILE_TYPES:
            raise Exception(
                "Property document_type is None, "
                "must have one of this values .")

        queryset = super(FileStorageInlineMixin, self).get_queryset(request)

        if self.file_type == 'image':
            return queryset.filter(
                document__extension__in=ImageThumbnailMixin.IMAGE_EXTENSIONS)
        elif self.file_type == 'document':
            return queryset.exclude(
                document__extension__in=ImageThumbnailMixin.IMAGE_EXTENSIONS)