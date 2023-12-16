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
        fields = ['id', 'parent', 'name', 'price', 'symbol', 'photo_url',
                  'is_selected', 'description', 'children']


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'parent', 'name', 'price', 'symbol', 'photo_url',
                  'is_selected', 'description']


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffProfile
        fields = '__all__'


class ShopSerializer(serializers.ModelSerializer):
    staffs = StaffSerializer(many=True, read_only=True)
    galleries = GallerySerializer(many=True, read_only=True)
    business_hours = BusinessHoursSerializer(many=True, read_only=True)
    services = PackageSerializer(many=True, read_only=True)
    promotions = PromotionSerializer(many=True, read_only=True)
    class Meta:
        model = Shop
        fields = [
            'id', 'shop_name', 'tel', 'fax', 'email', 'website', 'twitter', 'facebook',
            'linkedin', 'instagram', 'address', 'latitude', 'longitude', 'banner_url', 'logo_url',
            'about', 'promotions', 'staffs', 'services', 'galleries', 'business_hours'
        ]


class ShopDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'


class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = '__all__'


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'


