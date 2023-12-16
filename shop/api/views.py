from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView

from . import serializers
from rest_framework import generics, viewsets, status
from shop.models import *


class ShopViewSet(generics.ListAPIView):
    serializer_class = serializers.ShopSerializer
    queryset = Shop.objects.all()


class ServiceViewSet(generics.ListAPIView):
    serializer_class = serializers.ServiceSerializer
    queryset = Service.objects.filter(parent=None).order_by('parent')


class PlatformViewSet(APIView):
    def get_object(self, pk):
        try:
            return Platform.objects.get(pk=pk)
        except Platform.DoesNotExist:
            return None

    def get(self, request, *args, **kwargs):
        platforms = Platform.objects.all()
        serializer = serializers.PlatformSerializer(platforms, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            'uuid': request.data.get('uuid'),
            'platform_name': request.data.get('platform_name'),
            'device': request.data.get('device'),
            'ip': request.data.get('ip')
        }
        serializer = serializers.PlatformSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NotificationViewSet(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def get_object(self, pk):
        try:
            return Notification.objects.get(pk=pk)
        except Notification.DoesNotEx:
            return None

    def get(self, request, *args, **kwargs):
        notifications = Notification.objects.all()
        serializer = serializers.NotificationSerializer(notifications, many=True)
        notification_data = {
            'status': True,
            'results': serializer.data
        }
        return Response(data=notification_data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            'platform_id': request.data.get('platform_id'),
            'title': request.data.get('title'),
            'subtitle': request.data.get('subtitle'),
            'photo_url': request.data.get('photo_url'),
            'message': request.data.get('message'),
        }
        serializer = serializers.NotificationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)




