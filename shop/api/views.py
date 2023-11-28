from . import serializers
from rest_framework import generics
from shop.models import *


class ShopViewSet(generics.ListAPIView):
    serializer_class = serializers.ShopSerializer
    queryset = Shop.objects.all()


class ServiceViewSet(generics.ListAPIView):
    serializer_class = serializers.ServiceSerializer
    queryset = Service.objects.all()

