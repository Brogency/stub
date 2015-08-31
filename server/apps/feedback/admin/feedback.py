# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from apps.feedback.models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'type',)
    search_fields = ('message', )


admin.site.register(Feedback, FeedbackAdmin)
