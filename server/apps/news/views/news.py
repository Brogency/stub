# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.core.paginator import InvalidPage
from django.http import Http404
from django.views.generic import DetailView
from django.views.generic import ListView
from apps.news.models import News
from django.utils.translation import ugettext as _


class NewsListView(ListView):
    model = News
    paginate_by = 1
    ordering = ['created']

    def get_queryset(self):
        qs = super(NewsListView, self).get_queryset()
        return qs.filter(hidden=False, created__lte=datetime.now())

    def paginate_queryset(self, queryset, page_size):
        paginator = self.get_paginator(
            queryset, page_size, orphans=self.get_paginate_orphans(),
            allow_empty_first_page=self.get_allow_empty())
        page_kwarg = self.page_kwarg
        page = self.kwargs.get(page_kwarg) or self.request.GET.get(page_kwarg) or 'last'
        try:
            page_number = int(page)
        except ValueError:
            if page == 'last':
                page_number = paginator.num_pages
            else:
                raise Http404(_("Page is not 'last', nor can it be converted to an int."))
        try:
            page = paginator.page(page_number)
            return (paginator, page, page.object_list, page.has_other_pages())
        except InvalidPage as e:
            raise Http404(_('Invalid page (%(page_number)s): %(message)s') % {
                'page_number': page_number,
                'message': str(e)
            })


class NewsDetailView(DetailView):
    model = News
    slug_field = 'slug'
