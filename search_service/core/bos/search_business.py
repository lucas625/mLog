# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Business layer for searching on elk."""

import json

from elasticsearch import Elasticsearch

from core.beans import LogBean
from core.beans import ShippingBean
from core.beans import CartItemBean
from search_service.settings import ELASTIC_SEARCH_URL
from search_service.settings import ELASTIC_AUTH_USERNAME
from search_service.settings import ELASTIC_AUTH_PASSWORD


class SearchBusiness:
    """Class for business layer for searching on elk."""

    @staticmethod
    def search(days=None):
        """
        Searches on elastic search.
        :param int days:
        :return list[LogBean]:
        """
        elastic_search_instance = SearchBusiness._initialize_elastic_search()

        search_body = SearchBusiness._generate_search_body(days)

        search_result = elastic_search_instance.search(index="logstash-*", body=search_body, size=500)

        return SearchBusiness._parse_search_result_to_log_beans(search_result)

    @staticmethod
    def _initialize_elastic_search():
        """
        Initializes elastic search.
        :return ElasticSearch:
        """
        return Elasticsearch(
            [ELASTIC_SEARCH_URL],
            http_auth=(ELASTIC_AUTH_USERNAME, ELASTIC_AUTH_PASSWORD)
        )

    @staticmethod
    def _generate_search_body(days=None):
        """
        Generates the search body for search on elk, also accepts the days parameter for filtering data.
        :param int days: the number of days before today to search on.
        :return dict:
        """
        if days:
            pass  # TODO: implement me.
        else:
            search_body = {
                "query": {
                    "query_string": {
                        "query": "total",
                        "default_field": "message"
                    }
                }
            }
        return search_body

    @staticmethod
    def _parse_search_result_to_log_beans(search_result):
        """
        Parses the search result to a list of log beans.
        :param dict search_result:
        :return list[LogBean]:
        """
        search_hits = search_result['hits']['hits']
        parsed_search_results = [SearchBusiness._parse_search_hit_data(search_hit) for search_hit in search_hits]
        return [
            SearchBusiness._parse_parsed_search_result_to_log_bean(parsed_result) for
            parsed_result in parsed_search_results
        ]

    @staticmethod
    def _parse_search_hit_data(search_hit):
        """
        Parses a search hit data.
        :param dict search_hit:
        :return dict:
        """
        log_information_as_str = search_hit['_source']['message']
        log_bean_information_as_str = log_information_as_str.split('INFO in payment: ')[1]
        log_bean_information_as_json_str = log_bean_information_as_str.replace('\'', '\"')
        return json.loads(log_bean_information_as_json_str)

    @staticmethod
    def _parse_parsed_search_result_to_log_bean(parsed_search_result):
        """
        Parses a parsed search result to log bean.
        :param dict parsed_search_result:
        :return LogBean:
        """
        cart_item_beans, shipping_bean = SearchBusiness._parse_items(parsed_search_result['items'])
        return LogBean(
            total_price=parsed_search_result['total'],
            tax=parsed_search_result['tax'],
            items=cart_item_beans,
            shipping=shipping_bean
        )

    @staticmethod
    def _parse_items(items):
        """
        Parses the list of items to their beans.
        :param list[dict] items:
        :return list[CartItemBean]:
        :return ShippingBean:
        """
        cart_item_beans = []
        shipping_bean = ShippingBean(to='', price=0)
        for item in items:
            if item['sku'] == 'SHIP':
                shipping_bean = ShippingBean(to=item['name'], price=item['price'])
            else:
                cart_item_bean = CartItemBean(
                    name=item['name'],
                    number_of_items=item['qty'],
                    individual_price=item['price']
                )
                cart_item_beans.append(cart_item_bean)

        return cart_item_beans, shipping_bean


