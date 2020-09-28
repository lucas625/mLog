# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Core app URL Configuration."""

from core.rest import PaymentLogAnalyzerApiView
from django.urls import path

app_name = 'core'

urlpatterns = [
    path('', PaymentLogAnalyzerApiView.as_view(), name='analyze'),
]
