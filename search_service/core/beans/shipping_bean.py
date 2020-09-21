# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Bean for shipping data."""


class ShippingBean:
    """Class for shipping item bean."""

    def __init__(self, to, price):
        """
        ShippingBean constructor.
        :param str to:
        :param float price:
        :return ShippingBean:
        """
        self._to = to
        self._price = price

    @property
    def to(self):
        """
        Getter for to.
        :return str:
        """
        return self._to

    @property
    def price(self):
        """
        Getter for price.
        :return float:
        """
        return self._price

    def to_dto(self):
        """
        Parses the data contained on this bean to data transfer object.
        :return dict:
        """
        return {
            'to': self.to,
            'price': self.price
        }
