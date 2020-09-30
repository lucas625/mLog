# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""REST-API for searching on elk."""

from rest_framework import status
from rest_framework import views
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from core.bos import SearchBusiness


class SearchApiView(views.APIView):
    """REST-API for searching on elk."""

    http_method_names = ['post']
    parser_classes = [JSONParser]

    def post(self, request, *args, **kwargs): # FIXME: change to get and fix the issues tha will arise.
        """
        Gets log data from elk.
        The data must be like:
            {
                "start_date": "YYYY-MM-DD",
                "end_date": "YYYY-MM-DD"
            }
        :param Request request:
        :returns Response:
        """
        try:
            start_date = request.data.get('start_date')
            end_date = request.data.get('end_date')
            log_beans = SearchBusiness.search(start_date, end_date)
            response = Response([log_bean.to_dto() for log_bean in log_beans], status=status.HTTP_200_OK)
        except Exception as exc:
            response = Response(
                data='Failed to search on elastic search.', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return response
