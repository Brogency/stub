# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext as _


class Type(models.Model):
    slug = models.SlugField(
        verbose_name=_('Slug')
    )
    email = models.EmailField(
        verbose_name=_('Notify email'),
        blank=True,
        null=True,
    )
    title = models.CharField(
        max_length=255,
        verbose_name=_('Notify title'),
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = _("Type")
        verbose_name_plural = _("Types")

    def __unicode__(self):
        return self.slug

    # your custom methods
