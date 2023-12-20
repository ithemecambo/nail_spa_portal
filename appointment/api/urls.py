from django.urls import path
from .views import (
    TimeSlotViewSet,
    YearOfDateViewSet,
    AppointmentViewSet,
    BookingViewSet,
    ViewerBookingViewSet,
    AppointmentViewByWeekDayViewSet,
    ViewAccountViewSet
)

urlpatterns = [
    path('getTimeSlots/', TimeSlotViewSet.as_view(), name='timeSlots'),
    path('getAppointmentByWeekDays/<str:week_day>/', AppointmentViewByWeekDayViewSet.as_view(),
         name='getAppointmentByWeekDays'),
    path('appointment/', AppointmentViewSet.as_view(), name='appointment'),
    path('booking/', BookingViewSet.as_view(), name='booking'),
    path('getBookings/', ViewerBookingViewSet.as_view(), name='bookings'),
    path('staffs/', ViewAccountViewSet.as_view(), name='staffs')
]
