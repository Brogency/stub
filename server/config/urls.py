# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = patterns(
    '',
    url(r'^redactor/', include('redactor.urls')),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^pages/', include('django.contrib.flatpages.urls')),
)

# for internal apps
urlpatterns += patterns(
    '',
    url(r'^', include('apps.main.urls', namespace='main')),
)

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
