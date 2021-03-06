# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import CreateView
from django.core.urlresolvers import reverse
from apps.feedback.models import Feedback
from apps.feedback.forms.feedback import FeedbackForm


class FeedbackCreateView(CreateView):
    model = Feedback
    form_class = FeedbackForm

    def get_success_url(self):
        return reverse('feedback:success')
