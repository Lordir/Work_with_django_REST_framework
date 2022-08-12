import json
from django.views.generic import TemplateView
from rest_framework import generics
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product
from .serializers import LentaSerializer


class GetDataApi(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = LentaSerializer


class GetDataApi2(APIView):
    def get(self, request):
        with open("parser_lenta/ovoshchi.json", encoding="utf-8") as file:
            products_dict = json.load(file)
        return Response(products_dict)
