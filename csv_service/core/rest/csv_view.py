# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""REST-API for generating a csv file."""

from django.http import FileResponse
from rest_framework import status
from rest_framework import views
from rest_framework.response import Response

from core.beans import CsvBean
from core.bos import CsvBusiness


class CsvApiView(views.APIView):
    """REST-API for generating a csv file."""

    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        """
        Builds a csv file based on the arguments passed on the data.
        The data must be like:
            {
                field_names: ['name1', 'name2'],
                rows: [
                        {'name1': 'my name1', 'name2': 'my name2'},
                        {'name1: 'my name1 1', 'name2': 'my name2 1'},
                        ...
                ]
            }
        :param Request request:
        :returns File:
        """
        try:
            data = request.data
            csv_bean = CsvBean(fieldnames=data.get('fieldnames'), rows=data.get('rows'))
            csv_file_data = CsvBusiness.generate_csv(csv_bean)
            response = FileResponse(csv_file_data, status=status.HTTP_200_OK)
        except Exception as exc:
            response = Response(data='Failed to generate CSV.', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return response
