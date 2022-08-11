from rest_framework import serializers


class LentaSerializer(serializers.Serializer):
    name = serializers.CharField()
    price = serializers.FloatField
    url = serializers.CharField()
