import json
from django.forms import model_to_dict
from django.views.generic import TemplateView
from rest_framework import generics
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product
from .serializers import *


class GetDataApi(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = LentaSerializer


class GetDataApi2(APIView):
    def get(self, request):
        with open("parser_lenta/ovoshchi.json", encoding="utf-8") as file:
            products_dict = json.load(file)
        return Response(products_dict)

    def post(self, request):
        new_product = Product.objects.create(
            name=request.data['name'],
            slug=request.data['slug'],
            price=request.data['price']
        )
        return Response({'post': model_to_dict(new_product)})


class GetDataApi3(APIView):
    def get(self, request):
        products = Product.objects.all()
        return Response({'posts': LentaSerializer2(products, many=True).data})

    def post(self, request):
        serializer = LentaSerializer2(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({'error': "Method PUT not allowed"})

        try:
            instance = Product.objects.get(pk=pk)
        except:
            return Response({'error': "Method PUT not allowed"})

        serializer = LentaSerializer2(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({'error': "Method DELETE not allowed"})

        try:
            instance = Product.objects.get(pk=pk)
            instance.delete()
        except:
            return Response({'error': "Method DELETE not allowed"})

        return Response({'post': "Delete product " + str(pk)})
