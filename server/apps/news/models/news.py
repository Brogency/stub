# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext as _
from multiselectfield import MultiSelectField
from django.conf import settings
from redactor.fields import RedactorField
from apps.filestorage.models.mixins.filestorage import FileStorageMixin


class News(FileStorageMixin):
    DEFAULT = 'D'
    IMPORTANT = 'I'
    NEWS_TYPE = (
        (DEFAULT, _('Default')),
        (IMPORTANT, _('Important')),
    )
    type = models.CharField(
        max_length=1,
        choices=NEWS_TYPE,
        default=DEFAULT,
    )
    available_languages = MultiSelectField(
        max_length=50,
        default='ru',
        choices=settings.LANGUAGES,
        verbose_name=_('Available languages'),
    )
    title = models.CharField(
        max_length=200,
        verbose_name=_('Title'),
    )
    category = models.ForeignKey(
        'news.Category',
        verbose_name=_('Category'),
        blank=True,
        null=True,
    )
    image = models.ImageField(
        upload_to='news/%Y/%m/%d',
        blank=True,
        null=True,
    )
    slug = models.SlugField(
        verbose_name=_('Slug'),
    )
    short_description = models.TextField(
        verbose_name=_('Short description'),
    )
    description = RedactorField(
        verbose_name=_('Description'),
    )
    hidden = models.BooleanField(
        default=False,
        verbose_name=_('Hidden'),
    )
    created = models.DateTimeField(
        verbose_name=_('Created'),
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = _("News")
        verbose_name_plural = _("News")

    def __unicode__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse('news:news.detail', args=(self.pk,))

@receiver(pre_save, sender=News)
def create_initial(sender, instance, **kwargs):
    if not instance.id:
        instance.created = datetime.datetime.today()
