# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.sites.models import Site

from django.db import models
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _


class Feedback(models.Model):
    type = models.ForeignKey(
        'feedback.Type',
        verbose_name=_('Type'),
    )
    name = models.CharField(
        max_length=255,
        verbose_name=_('Contact name'),
    )
    email = models.EmailField(
        verbose_name=_('Contact email'),
    )
    message = models.TextField(
        verbose_name=_('Message'),
    )
    created_at = models.DateTimeField(
        verbose_name=_('Created date'),
        auto_now_add=True,
    )

    class Meta:
        verbose_name = _('Feedback')
        verbose_name_plural = _('Feedback')

    def __unicode__(self):
        return str(self.pk)
