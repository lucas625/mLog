# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Bean for cart item data."""


class CartItemBean:
    """Class for cart item bean."""

    def __init__(self, name, number_of_items, individual_price):
        """
        CartItemBean constructor.
        :param str name:
        :param int number_of_items:
        :param float individual_price:
        :return CartItemBean:
        """
        self._name = name
        self._number_of_items = number_of_items
        self._individual_price = individual_price

    @property
    def name(self):
        """
        Getter for name.
        :return str:
        """
        return self._name

    @property
    def number_of_items(self):
        """
        Getter for number of items.
        :return int:
        """
        return self._number_of_items

    @property
    def individual_price(self):
        """
        Getter for individual price.
        :return float:
        """
        return self._individual_price

    def to_dto(self):
        """
        Parses the data contained on this bean to data transfer object.
        :return dict:
        """
        return {
            'name': self.name,
            'number_of_items': self.number_of_items,
            'individual_price': self.individual_price
        }
