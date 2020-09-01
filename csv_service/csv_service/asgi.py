# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Csv_service asgi module."""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'csv_service.settings')

application = get_asgi_application()
