from django.urls import path
from shop.api.views import (
    ShopViewSet,
    ServiceViewSet,
)

app_name = 'shop'

urlpatterns = [
    path('getNailSpa/', ShopViewSet.as_view(), name='nailSpa'),
    path('getServices/', ServiceViewSet.as_view(), name='services'),
]

