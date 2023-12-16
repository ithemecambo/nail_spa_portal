from django.urls import path
from shop.api.views import (
    ShopViewSet,
    ServiceViewSet,
    PlatformViewSet,
    NotificationViewSet,
)

app_name = 'shop'

urlpatterns = [
    path('getNailSpa/', ShopViewSet.as_view(), name='nailSpa'),
    path('getServices/', ServiceViewSet.as_view(), name='services'),

    path('getPlatforms/', PlatformViewSet.as_view(), name='platforms'),

    path('getNotifications/', NotificationViewSet.as_view(), name='notifications'),

]

