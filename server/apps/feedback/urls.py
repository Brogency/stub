# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from apps.feedback.views import FeedbackCreateView


urlpatterns = patterns(
    '',
    url(r'^create/$', FeedbackCreateView.as_view(), name='feedback.create'),
)

