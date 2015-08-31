# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from .views import FeedbackCreateView
from .views import SuccessView


urlpatterns = patterns(
    '',
    url(r'^create/$', FeedbackCreateView.as_view(), name='create'),
    url(r'^success/$', SuccessView.as_view(), name='success'),
)

