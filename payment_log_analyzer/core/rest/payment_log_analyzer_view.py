# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""REST-API for analyzing the payment log."""

from django.http import FileResponse
from rest_framework import status
from rest_framework import views
from rest_framework.response import Response

from core.bos import PaymentLogAnalyzerBusiness


class PaymentLogAnalyzerApiView(views.APIView):
    """REST-API for analyzing the payment log."""

    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        """
        Analyzes the payment log.
        :param Request request:
        :returns Response:
        """
        try:
            days = request.data.get('days') if request.data.get('days') else None
            csv_file = PaymentLogAnalyzerBusiness.analyze(days)
            response = FileResponse(csv_file, status=status.HTTP_200_OK)
        except Exception as exc:
            response = Response(
                data='Failed to analyze the payment log.', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return response
