# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext as _


class Category(models.Model):
    name = models.TextField(
        verbose_name=_("name")
    )
    hidden = models.BooleanField(
        default=False,
        verbose_name=_("hidden"),
    )

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categorys")
        app_label = 'filestorage'

    def __unicode__(self):
        return self.name
