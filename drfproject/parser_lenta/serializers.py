from rest_framework import serializers
from .models import Product


class LentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'price', 'slug')


class LentaSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Product
        # fields = ('name', 'price', 'slug')
        fields = "__all__"

    # name = serializers.CharField()
    # slug = serializers.SlugField()
    # price = serializers.FloatField()
    #
    # def create(self, validated_data):
    #     return Product.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get("name", instance.name)
    #     instance.slug = validated_data.get("slug", instance.slug)
    #     instance.price = validated_data.get("price", instance.price)
    #     instance.save()
    #     return instance
