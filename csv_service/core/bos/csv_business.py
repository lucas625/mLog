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
        csv_path = os.path.join(MEDIA_ROOT, 'csvs', csv_bean.enterprise_name, uuid.uuid4()+'.csv')
        with open(csv_path, 'wb') as f:
            writer = csv.writer(f)
            writer.writerows(csv_bean.rows)
        csv_bean.csv_file = csv_path
        saved_csv_bean = CsvDao.save(csv_bean)
        return saved_csv_bean.csv_file


