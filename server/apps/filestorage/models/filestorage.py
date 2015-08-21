# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
import os
from django.conf import settings
from django.contrib.contenttypes.generic import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _
from django.db import models
from multiselectfield import MultiSelectField
from funcy import last
from .mixins.image import ImageThumbnailMixin
from django.template import defaultfilters


class FileStorage(ImageThumbnailMixin):
    document = models.FileField(
        upload_to='filestorage/',
        verbose_name=_('Document'),
    )
    hidden = models.BooleanField(
        default=False,
        verbose_name=_('Hidden'),
    )
    extension = models.CharField(
        max_length=10,
        verbose_name=_('Extension'),
        null=True,
        blank=True,
    )
    description = models.CharField(
        max_length=150,
        verbose_name=_('Description'),
        blank=True,
        null=True,
    )
    category = models.ForeignKey(
        'filestorage.Category',
        verbose_name=_('Category'),
        blank=True,
        null=True,
    )
    created = models.DateTimeField(
        verbose_name=_('Created'),
        blank=True,
        null=True,
    )

    class Meta:
        app_label = 'filestorage'
        verbose_name = _('FileStorage')
        verbose_name_plural = _('FileStorages')

    def __unicode__(self):
        return os.path.basename(self.document.name)

    @property
    def ext(self):
        """For ImageThumbnailMixin."""
        return self.extension

    @property
    def doc(self):
        """For ImageThumbnailMixin."""
        return self.document

    @property
    def size(self):
        return defaultfilters.filesizeformat(self.document.size)


class RelativeFileStorage(ImageThumbnailMixin):
    document = models.ForeignKey(
        FileStorage,
        verbose_name=_('File')
    )
    languages = MultiSelectField(
        choices=settings.LANGUAGES,
        max_length=50,
        verbose_name=_('Show for this lang'),
        blank=True,
        null=True,
    )
    order = models.PositiveIntegerField(
        db_index=True,
        default=0,
        verbose_name=_('Order'),
    )

    content_type = models.ForeignKey(
        ContentType
    )
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey(
        'content_type',
        'object_id'
    )

    @staticmethod
    def autocomplete_search_fields():
        return ("document__id__iexact", 'document__document__icontains', )

    class Meta:
        ordering = ['order']
        app_label = 'filestorage'
        verbose_name = _('RelativeFileStorage')
        verbose_name_plural = _('RelativeFileStorages')

    def __unicode__(self):
        return self.document.__unicode__()

    @property
    def ext(self):
        """For ImageThumbnailMixin."""
        return self.document.extension

    @property
    def doc(self):
        """For ImageThumbnailMixin."""
        return self.document.document

    @property
    def size(self):
        return defaultfilters.filesizeformat(self.document.document.size)


@receiver(pre_save, sender=FileStorage)
def create_initial_story(sender, instance, **kwargs):
    if not instance.id:
        instance.created = datetime.datetime.today()
    instance.extension = last(instance.__unicode__().split('.')).upper()
