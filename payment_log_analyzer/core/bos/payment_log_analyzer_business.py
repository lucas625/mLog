# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Business layer for analyzing the payment log."""

from django.conf import settings
import requests

from core.beans import AnalyzedItemBean
from core.beans import CartItemBean
from core.beans import LogBean
from core.beans import ShippingBean


class PaymentLogAnalyzerBusiness:
    """Class for business layer for analyzing the payment log."""

    @staticmethod
    def analyze(start_date, end_date):
        """
        Function to analyze the payment logs and return a csv file with the results.
        :param str start_date: formated as YYYY-MM-DD.
        :param str end_date: formated as YYYY-MM-DD.
        :return File:
        """
        log_beans = PaymentLogAnalyzerBusiness._get_logs_data(start_date, end_date)
        analyzed_item_beans = PaymentLogAnalyzerBusiness._analyze_items(log_beans)
        return PaymentLogAnalyzerBusiness._get_csv(analyzed_item_beans)

    @staticmethod
    def _get_csv(analyzed_item_beans):
        """
        Function to generate the csv.
        :param list[AnalyzedItemBean] analyzed_item_beans:
        :return File:
        """
        data_transfer_object = {
            'field_names': ['name', 'appearance_on_transactions', 'average_price', 'total_count', 'total_price'],
            'rows': [analyzed_item.to_dto() for analyzed_item in analyzed_item_beans]
        }
        return requests.post(url='{}/api/csv/generate/'.format(settings.CSV_SERVICE_URL), json=data_transfer_object)

    @staticmethod
    def _analyze_items(log_beans):
        """
        Analyzes the items.
        :param list[LogBean] log_beans:
        :return list[AnalyzedItemBean]:
        """
        full_list_of_items = PaymentLogAnalyzerBusiness._generate_full_list_of_items(log_beans)
        grouped_list_of_items = PaymentLogAnalyzerBusiness._generate_grouped_list_of_items(full_list_of_items)
        return PaymentLogAnalyzerBusiness._generate_list_of_analyzed_items_beans(grouped_list_of_items)

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
    def _generate_list_of_analyzed_items_beans(grouped_list_of_items):
        """
        Function to generate a list of analyzed item beans.
        :param list[list[CartItemBean]] grouped_list_of_items:
        :return list[AnalyzedItemBean]:
        """
        analyzed_items_list = []
        for grouped_items in grouped_list_of_items:
            name = grouped_items[0].name
            occurrences = len(grouped_items)
            total_price = 0
            total_count = 0
            for item in grouped_items:
                total_count += item.number_of_items
                total_price += item.number_of_items * item.individual_price
            average_price = total_price / total_count
            analyzed_items_list.append(
                AnalyzedItemBean(
                    name=name,
                    appearance_on_transactions=occurrences,
                    average_price=average_price,
                    total_count=total_count,
                    total_price=total_price))
        sorted_analyzed_items_list = sorted(analyzed_items_list, key=lambda k: k.appearance_on_transactions, reverse=True)
        return sorted_analyzed_items_list

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
    def _get_logs_data(start_date, end_date):
        """
        Function to get the logs data.
        :param str start_date: formated as YYYY-MM-DD.
        :param str end_date: formated as YYYY-MM-DD.
        :return list[LogBean]:
        """
        logs_data = requests.post(
            url='{}/api/search/'.format(settings.SEARCH_SERVICE_URL),
            json=dict(start_date=start_date, end_date=end_date)).json()
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
            shipping = ShippingBean(to=log_data['shipping']['to'], price=log_data['shipping']['price'])
            log_bean = LogBean(total_price=log_data['total_price'], tax=log_data['tax'], items=items, shipping=shipping)
            logs_bean_list.append(log_bean)
        return logs_bean_list
