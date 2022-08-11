import json
from rest_framework import generics
from django.shortcuts import render

from .serializers import LentaSerializer


class GetDataApi(generics.ListAPIView):
    with open("D:\Git\Work_with_django_REST_framework\drfproject\parser_lenta\ovoshchi.json", encoding="utf-8") as file:
        queryset = json.load(file)
    serializer_class = LentaSerializer
