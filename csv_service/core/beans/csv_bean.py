# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Bean for csv data."""


class CsvBean:
    """Class for csv bean."""

    def __init__(self, fieldnames, rows):
        """
        CsvBean constructor.
        :param list[str] fieldnames:
        :param list[dict] rows:
        :return CsvBean:
        """
        self._fieldnames = fieldnames
        self._rows = rows

    @property
    def fieldnames(self):
        """
        Getter for fieldnames.
        :return list[str]:
        """
        return self._fieldnames

    @property
    def rows(self):
        """
        Getter for rows.
        :return list[dict]:
        """
        return self._rows
