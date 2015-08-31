# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.text import slugify
from ..forms.feedback import FeedbackForm
from ..models import Type
from django import template
from django.core.context_processors import csrf


register = template.Library()

@register.inclusion_tag(
    'feedback/feedback_form.html',
    takes_context=True
)
def feedback_form(context, name='default'):
    kwargs = {}
    kwargs.update(csrf(context['request']))
    name = slugify(name)
    try:
        type = Type.objects.get(slug=name)
    except Type.DoesNotExist:
        type = Type.objects.create(slug=name)
    form = FeedbackForm(initial={"type": type})
    return {'form': form}
