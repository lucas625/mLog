# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Csv_service URL Configuration"""

from django.conf import settings
from django.conf.urls.static import static
from django.urls import include
from django.urls import path


urlpatterns = [
    path('api/csv/', include('core.urls', namespace='core'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
