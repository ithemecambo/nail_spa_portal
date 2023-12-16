from django import forms
from shop.models import *


class ServiceCreateForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = [
            'parent',
            'name',
            'price',
            'symbol',
            'photo_url',
            'description',
        ]


class ShopCreateForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = [
            'staffs',
            'services',
            'shop_name',
            'website',
            'tel',
            'fax',
            'email',
            'twitter',
            'facebook',
            'linkedin',
            'instagram',
            'address',
            'latitude',
            'longitude',
            'banner_url',
            'logo_url',
            'about',
            'status'
        ]


class BusinessHourCreateForm(forms.ModelForm):
    class Meta:
        model = BusinessHour
        fields = ['day', 'hour']


class GalleryCreateForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ['photo_url']


class PromotionCreateForm(forms.ModelForm):
    class Meta:
        model = Promotion
        fields = ['service_id', 'title', 'subtitle', 'discount', 'color', 'photo_url']


class PlatformCreateForm(forms.ModelForm):
    class Meta:
        model = Platform
        fields = ['platform_name', 'device', 'ip', 'uuid']


class NotificationCreateForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = ['platform_id', 'title', 'subtitle', 'photo_url', 'message']
