from django.urls import path
from .views import (
    TimeSlotViewSet,
    AppointmentViewSet,
    BookingViewSet,
    ViewerBookingViewSet,
    AppointmentDetailViewSet,
    AppointmentViewByWeekDayViewSet,
    MyViewerBookingByIdViewSet,
    MyViewerBookingViewSet,
    ViewAccountViewSet,
)

urlpatterns = [
    path('getTimeSlots/', TimeSlotViewSet.as_view(), name='timeSlots'),
    path('getAppointmentByWeekDays/<str:week_day>/', AppointmentViewByWeekDayViewSet.as_view(),
         name='getAppointmentByWeekDays'),
    path('appointment/', AppointmentViewSet.as_view(), name='appointment'),
    path('appointment/<int:id>/', AppointmentDetailViewSet.as_view(), name='update-appointment'),

    path('booking/', BookingViewSet.as_view(), name='booking'),
    path('getBookings/', ViewerBookingViewSet.as_view(), name='bookings'),
    path('staffs/', ViewAccountViewSet.as_view(), name='staffs'),

    path('myBookingIds/<int:profile_id>/', MyViewerBookingByIdViewSet.as_view(), name='myBookingIds'),
    path('myBookings/<int:profile_id>/<str:status>/', MyViewerBookingViewSet.as_view(), name='myBookings'),
]
