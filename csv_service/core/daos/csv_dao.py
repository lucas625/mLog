# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""DAO layer for the csv model."""

from core.models import CsvModel
from core.beans import CsvBean


class CsvDao:
    """DAO layer for the csv model."""

    @staticmethod
    def save(csv_bean):
        """
        Saves the csv file on the database.
        :param CsvBean csv_bean:
        :return CsvBean:
        :raises IntegrityError:
        :raises ValidationError:
        """
        csv_instance = CsvModel.objects.create(enterprise_name=csv_bean.enterprise_name, csv_file=csv_bean.csv_file)
        return CsvBean(enterprise_name=csv_instance.enterprise_name, csv_file=csv_instance.csv_file)
