from django.urls import path
from shop.api.views import (
    ServiceViewSet,
)

app_name = 'shop'

urlpatterns = [
    path('services/', ServiceViewSet.as_view(), name='services'),
]

