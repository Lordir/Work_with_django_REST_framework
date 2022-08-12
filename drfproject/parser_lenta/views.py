import json
from django.views.generic import TemplateView
from rest_framework import generics
from django.shortcuts import render

from .models import Product
from .serializers import LentaSerializer


class GetDataApi(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = LentaSerializer
