# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Core app URL Configuration."""

from core.rest import SearchApiView
from django.urls import path

app_name = 'core'

urlpatterns = [
    path('', SearchApiView.as_view(), name='search'),
]
