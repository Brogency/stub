# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from ..models import Feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'message', 'type']
        widgets = {
            'type': forms.HiddenInput(),
        }
