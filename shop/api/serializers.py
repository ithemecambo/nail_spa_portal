from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework_recursive.fields import RecursiveField
from shop.models import *


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ['id', 'photo_url']


class BusinessHoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessHour
        fields = ['id', 'day', 'hour']


class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    # parent = NestedServiceSerializer()
    children = RecursiveField(many=True)
    class Meta:
        model = Service
        fields = ['id', 'parent', 'name', 'price', 'symbol', 'photo_url', 'description', 'children']


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'name', 'photo_url', 'children']


class ShopSerializer(serializers.ModelSerializer):
    users = AccountSerializer(many=True, read_only=True)
    galleries = GallerySerializer(many=True, read_only=True)
    business_hours = BusinessHoursSerializer(many=True, read_only=True)
    services = PackageSerializer(many=True, read_only=True)
    promotions = PromotionSerializer(many=True, read_only=True)
    class Meta:
        model = Shop
        fields = [
            'id', 'shop_name', 'tel', 'fax', 'email', 'website', 'twitter', 'facebook',
            'linkedin', 'instagram', 'address', 'latitude', 'longitude', 'banner_url', 'logo_url',
            'about', 'promotions', 'users', 'services', 'galleries', 'business_hours'
        ]


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


