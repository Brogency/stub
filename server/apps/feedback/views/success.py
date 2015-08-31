# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import TemplateView


class SuccessView(TemplateView):
    template_name = 'feedback/feedback_success.html'
