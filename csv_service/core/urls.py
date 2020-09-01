# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Core app URL Configuration."""

from core.rest import CsvApiView
from django.urls import path

app_name = 'core'

urlpatterns = [
    path('generate/', CsvApiView.as_view(), name='generate-csv'),
]
