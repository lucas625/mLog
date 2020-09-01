# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Bean for csv data."""


class CsvBean:
    """Class for csv bean."""

    def __init__(self, enterprise_name, rows=None, csv_file=None):
        """
        CsvBean constructor.
        :param str enterprise_name:
        :param list[list] rows:
        :param File csv_file:
        :return CsvBean:
        """
        self._enterprise_name = enterprise_name
        self._rows = rows
        self._csv_file = csv_file

    @property
    def enterprise_name(self):
        """
        Getter for enterprise_name.
        :return str:
        """
        return self._enterprise_name

    @property
    def rows(self):
        """
        Getter for rows.
        :return list[list]:
        """
        return self._rows

    @property
    def csv_file(self):
        """
        Getter for csv_file.
        :return File:
        """
        return self._csv_file

    @csv_file.setter
    def csv_file(self, csv_file):
        """
        Setter for csv_file.
        :param File csv_file:
        """
        self._csv_file = csv_file
