# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Csv model module."""

import os

from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import functions


def _validate_file_csv_extension(file_name_with_ext):
    """
    Validates if a file is csv.
    :param django.db.models.fields.files.FieldFile file_name_with_ext:
    :raises ValidationError: 
    """
    ext = os.path.splitext(file_name_with_ext.name)[-1]
    valid_extensions = ['.csv']
    if not ext.lower() in valid_extensions:
        raise ValidationError('{} extension is not supported.'.format(ext.upper()))


class CsvModel(models.Model):
    """Holds data for the csv model."""
    enterprise_name = models.CharField(max_length=100, verbose_name='Enterprise Name')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    csv_file = models.FileField(
        upload_to='csvs',
        validators=[_validate_file_csv_extension],
        verbose_name='CSV')

    class Meta:
        """Meta class for CsvModel."""
        models.CharField.register_lookup(functions.Length)

        constraints = [
            models.CheckConstraint(
                check=models.Q(enterprise_name__length__gt=0),
                name='csv_model_enterprise_name_length_greater_than_0'),
            models.CheckConstraint(
                check=models.Q(enterprise_name__length__lte=100),
                name='csv_model_enterprise_name_title_length_less_or_equal_than_100')]

