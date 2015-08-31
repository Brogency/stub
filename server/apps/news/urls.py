# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from apps.news.views import NewsDetailView
from apps.news.views import NewsListView


urlpatterns = patterns(
    '',
    url(r'^$', NewsListView.as_view(), name='news.list'),
    url(r'^(?P<pk>\d+)/$', NewsDetailView.as_view(), name='news.detail'),
)

