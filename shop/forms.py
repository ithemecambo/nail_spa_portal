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
            'users',
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
