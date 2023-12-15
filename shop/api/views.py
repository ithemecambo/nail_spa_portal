from rest_framework.response import Response

from . import serializers
from rest_framework import generics, viewsets
from shop.models import *
from .serializers import ServiceSerializer


class ShopViewSet(generics.ListAPIView):
    serializer_class = serializers.ShopSerializer
    queryset = Shop.objects.all()


class ServiceViewSet(generics.ListAPIView):
    serializer_class = serializers.ServiceSerializer
    queryset = Service.objects.filter(parent=None).order_by('parent')



