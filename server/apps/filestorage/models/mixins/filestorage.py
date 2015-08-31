# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.contenttypes.generic import GenericRelation
from django.db import models
from django.utils import translation
from ..filestorage import RelativeFileStorage
from image import ImageThumbnailMixin


class FileStorageMixin(models.Model):
    file_set = GenericRelation(RelativeFileStorage)

    class Meta:
        abstract = True

    def get_documents(self):
        return self.file_set \
            .exclude(document__extension__in=ImageThumbnailMixin.IMAGE_EXTENSIONS) \
            .filter(languages__contains=translation.get_language())

    def get_images(self):
        return self.file_set \
            .filter(document__extension__in=ImageThumbnailMixin.IMAGE_EXTENSIONS) \
            .filter(languages__contains=translation.get_language())