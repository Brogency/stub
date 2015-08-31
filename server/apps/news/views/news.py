# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import DetailView
from django.views.generic import ListView
from django.core.urlresolvers import reverse
from apps.news.models import News


class NewsListView(ListView):
    model = News
    paginate_by = 10

    def get_queryset(self):
        """Override this method or remove."""
        return super(NewsListView, self).get_queryset()

    def get_context_data(self, **kwargs):
        """Override this method or remove."""
        context = super(NewsListView, self).get_context_data(**kwargs)
        context.update({})
        return context



class NewsDetailView(DetailView):
    model = News
    slug_field = 'slug'

    def get_object(self, queryset=None):
        """Override this method or remove."""
        return super(NewsDetailView, self).get_object(queryset=queryset)

    def get_context_data(self, **kwargs):
        """Override this method or remove."""
        context = super(NewsDetailView, self).get_context_data(**kwargs)
        context.update({})
        return context
