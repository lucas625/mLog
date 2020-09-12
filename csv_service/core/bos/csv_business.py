# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Business layer for generating a csv file."""

import csv
import uuid
import os

from csv_service.settings import MEDIA_ROOT

class CsvBusiness:
    """Class for business layer for generating a csv file."""

    @staticmethod
    def generate_csv(csv_bean):
        """
        Function for generating a csv file.
        :param CsvBean csv_bean:
        :return File:
        """
        csv_file_path = CsvBusiness._write_csv(csv_bean)
        with open(csv_file_path, 'r') as csv_file:
            csv_file_data = csv_file.read()
        os.remove(csv_file_path)
        return csv_file_data

    @staticmethod
    def _write_csv(csv_bean):
        """
        Function for writing a csv file.
        :param CsvBean csv_bean:
        :return str:
        """
        csv_path = CsvBusiness._generate_csv_path(csv_bean)
        
        with open(csv_path, 'w') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=csv_bean.fieldnames)
            writer.writeheader()
            writer.writerows(csv_bean.rows)
        return csv_path

    @staticmethod
    def _generate_csv_path(csv_bean):
        """
        Generates the path to the csv file.
        :param CsvBean csv_bean: the csv as bean.
        :return str:
        """
        base_path = os.path.join(MEDIA_ROOT, 'csvs')
        if not os.path.exists(base_path):
            os.makedirs(base_path)
        return os.path.join(base_path, '{}.csv'.format(uuid.uuid4()))
