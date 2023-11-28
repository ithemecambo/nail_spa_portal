from django import forms
from shop.models import *


class ServiceCreateForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = [
            'parent',
            'name',
            'status',
            'photo_url'
        ]


class ShopCreateForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = [
            'users',
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



