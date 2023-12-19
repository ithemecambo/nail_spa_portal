from django.urls import path
from .views import (
    TimeSlotViewSet,
)

urlpatterns = [
    path('getTimeSlots/', TimeSlotViewSet.as_view(), name='timeSlots'),
]
