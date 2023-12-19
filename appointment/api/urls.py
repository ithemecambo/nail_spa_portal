from django.urls import path
from .views import (
    TimeSlotViewSet,
    AppointmentViewSet,
)

urlpatterns = [
    path('getTimeSlots/', TimeSlotViewSet.as_view(), name='timeSlots'),
    path('appointment/', AppointmentViewSet.as_view(), name='appointment')
]
