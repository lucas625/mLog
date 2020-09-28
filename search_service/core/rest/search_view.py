# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""REST-API for searching on elk."""

from rest_framework import status
from rest_framework import views
from rest_framework.response import Response

from core.bos import SearchBusiness


class SearchApiView(views.APIView):
    """REST-API for searching on elk."""

    http_method_names = ['post']

    def post(self, request, *args, **kwargs): # FIXME: change to get and fix the issues tha will arise.
        """
        Gets log data from elk.
        :param Request request:
        :returns Response:
        """
        try:
            days = request.data.get('days') if request.data.get('days') else None
            log_beans = SearchBusiness.search(days)
            response = Response([log_bean.to_dto() for log_bean in log_beans], status=status.HTTP_200_OK)
        except Exception as exc:
            import traceback; traceback.print_exc()
            response = Response(
                data='Failed to search on elastic search.', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return response
