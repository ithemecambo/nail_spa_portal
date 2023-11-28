from rest_framework import serializers
from shop.models import *


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class BusinessHourSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessHour
        fields = ['day', 'hour']


class ShopDetailSerializer(serializers.ModelSerializer):
    service = ServiceSerializer()
    businessHour = BusinessHourSerializer()

    class Meta:
        model = Shop
        fields = '__all__'


