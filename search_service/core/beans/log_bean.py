# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Bean for log data."""


class LogBean:
    """Class for log bean."""

    def __init__(self, total_price, tax, items, shipping):
        """
        LogBean constructor.
        :param float total_price:
        :param float tax:
        :param list[core.beans.CartItemBean] items:
        :param core.beans.ShippingBean shipping:
        :return LogBean:
        """
        self._total_price = total_price
        self._tax = tax
        self._items = items
        self._shipping = shipping

    @property
    def total_price(self):
        """
        Getter for total price.
        :return float:
        """
        return self._total_price

    @property
    def tax(self):
        """
        Getter for tax.
        :return float:
        """
        return self._tax

    @property
    def items(self):
        """
        Getter for items.
        :return list[cartItemBean]:
        """
        return self._items

    @property
    def shipping(self):
        """
        Getter for shipping.
        :return list[ShippingBean]:
        """
        return self._shipping

    def to_dto(self):
        """
        Parses the data contained on this bean to data transfer object.
        :return dict:
        """
        return {
            'total_price': self.total_price,
            'tax': self.tax,
            'items': [item.to_dto() for item in self.items],
            'shipping': self.shipping.to_dto()
        }
