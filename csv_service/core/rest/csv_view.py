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
        The data must be like data: {enterprise_name: 'name_here', rows: [[el1, el2...], [eln, eln+1...], ...]}.
        :param Request request:
        :returns File:
        """
        try:
            data = request.POST.dict
            csv_bean = CsvBean(enterprise_name=data.get('enterprise_name'), rows=data.get('rows'))
            csv_file = CsvBusiness.generate_csv(csv_bean)
            response = FileResponse(data=csv_file, status=status.HTTP_200_OK)
        except:
            response = Response(data='Failed to generate CSV.', status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        return response
