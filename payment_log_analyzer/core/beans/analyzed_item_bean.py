# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Bean for analyzed item data."""


class AnalyzedItemBean:
    """Class for analyzed item bean."""

    def __init__(self, name, appearance_on_transactions, average_price, total_count, total_price):
        """
        CartItemBean constructor.
        :param str name:
        :param int appearance_on_transactions:
        :param float average_price:
        :param int total_count:
        :param float total_price:
        :return AnalyzedItemBean:
        """
        self._name = name
        self._appearance_on_transactions = appearance_on_transactions
        self._average_price = average_price
        self._total_count = total_count
        self._total_price = total_price

    @property
    def name(self):
        """
        Getter for name.
        :return str:
        """
        return self._name

    @property
    def appearance_on_transactions(self):
        """
        Getter for appearance on transactions.
        :return int:
        """
        return self._appearance_on_transactions

    @property
    def average_price(self):
        """
        Getter for average price.
        :return float:
        """
        return self._average_price

    @property
    def total_count(self):
        """
        Getter for total count.
        :return int:
        """
        return self._total_count

    @property
    def total_price(self):
        """
        Getter for total price.
        :return float:
        """
        return self._total_price

    def to_dto(self):
        """
        Parses the data contained on this bean to data transfer object.
        :return dict:
        """
        return dict(
            name=self.name,
            appearance_on_transactions=self.appearance_on_transactions,
            average_price=self.average_price,
            total_count=self.total_count,
            total_price=self.total_price)
