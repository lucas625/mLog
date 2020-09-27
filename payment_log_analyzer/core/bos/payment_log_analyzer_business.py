# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Business layer for analyzing the payment log."""


import requests

from django.conf import settings

from core.beans import AnalyzedItemBean
from core.beans import CartItemBean
from core.beans import LogBean
from core.beans import ShippingBean


class PaymentLogAnalyzerBusiness:
    """Class for business layer for analyzing the payment log."""

    @staticmethod
    def analyze(days):
        """
        Function to analyze the payment logs and return a csv file with the results.
        :param int days: the total number of days before today to analyze.
        :return File:
        """
        log_beans = PaymentLogAnalyzerBusiness._get_logs_data(days)
        analyzed_item_beans = PaymentLogAnalyzerBusiness._analyze_items(log_beans)
        # TODO: call the csv service on the analyzed items (parse their format to the required on the csv service).

    @staticmethod
    def _analyze_items(log_beans):
        """
        Analyzes the items.
        :param list[LogBean] log_beans:
        :return list[AnalyzedItemBean]:
        """
        full_list_of_items = PaymentLogAnalyzerBusiness._generate_full_list_of_items(log_beans)
        grouped_list_of_items = PaymentLogAnalyzerBusiness._generate_grouped_list_of_items(full_list_of_items)
        # TODO: parse grouped list of items to AnalyzedItemBean

    @staticmethod
    def _generate_full_list_of_items(log_beans):
        """
        Gets all items in a log beans list and creates a list with them.
        :param list[LobBean] log_beans:
        :return list[CartItemBean]:
        """
        full_list_of_items = []
        for log_bean in log_beans:
            full_list_of_items += log_bean.items
        return full_list_of_items

    @staticmethod
    def _generate_grouped_list_of_items(item_beans):
        """
        Groups a list of items by their name.
        :param list[CartItemBean] item_beans:
        :return list[list[CartItemBean]]:
        """
        grouped_list_of_items = []

        for item in item_beans:
            item_exist = False
            item_list_index = None

            for (index, item_list) in enumerate(grouped_list_of_items):
                if item_list[0].name == item.name:
                    item_exist = True
                    item_list_index = index
                    break

            if item_exist:
                grouped_list_of_items[item_list_index].append(item)
            else:
                grouped_list_of_items.append([item])
        return grouped_list_of_items

    @staticmethod
    def _get_logs_data(days):
        """
        Function to get the logs data.
        :param int days:
        :return list[LogBean]:
        """
        logs_data = requests.post(url=settings.SEARCH_SERVICE_URL, data=dict(days=days))
        return PaymentLogAnalyzerBusiness._parse_logs_data_to_beans(logs_data)

    @staticmethod
    def _parse_logs_data_to_beans(logs_data):
        """
        Parses the logs data to beans.
        :param list[dict] logs_data:
        :return list[LogBean]:
        """
        logs_bean_list = []
        for log_data in logs_data:
            items = [
                CartItemBean(
                    name=item['name'],
                    individual_price=item['individual_price'],
                    number_of_items=item['number_of_items'])
                for item in log_data['items']]
            shipping = ShippingBean(to=log_data['to'], price=log_data['price'])
            log_bean = LogBean(total_price=log_data['total_price'], tax=log_data['tax'], items=items, shipping=shipping)
            logs_bean_list.append(log_bean)
        return logs_bean_list
