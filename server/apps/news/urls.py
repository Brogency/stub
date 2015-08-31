# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from apps.news.views import NewsDetailView
from apps.news.views import NewsListView


urlpatterns = patterns(
    '',
    url(r'^$', NewsListView.as_view(), name='list'),
    url(r'^(?P<slug>[\w-]+)/$', NewsDetailView.as_view(), name='detail'),
)

