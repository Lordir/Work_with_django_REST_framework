from rest_framework import serializers
from .models import Product


class LentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'price', 'slug')
