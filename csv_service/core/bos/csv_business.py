# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Business layer for generating a csv file."""

import csv
import uuid
import os

from core.daos import CsvDao
from csv_service.settings import MEDIA_ROOT

class CsvBusiness:
    """Class for business layer for generating a csv file."""

    @staticmethod
    def generate_csv(csv_bean):
        """
        Function for generating a csv file.
        :param CsvBean csv_bean:
        :return File:
        :raises IntegrityError:
        :raises ValidationError:
        """
        csv_bean.csv_file = CsvBusiness._write_csv(csv_bean)
        saved_csv_bean = CsvDao.save(csv_bean)
        return saved_csv_bean.csv_file

    @staticmethod
    def _write_csv(csv_bean):
        """
        Function for writing a csv file.
        :param CsvBean csv_bean:
        :return str:
        """
        base_path = os.path.join(MEDIA_ROOT, 'csvs', csv_bean.enterprise_name)
        if not os.path.exists(base_path):
            os.makedirs(base_path)
        csv_path = os.path.join(base_path, '{}.csv'.format(uuid.uuid4()))
        with open(csv_path, 'w') as f:
            writer = csv.writer(f)
            writer.writerows(csv_bean.rows)
        return csv_path
