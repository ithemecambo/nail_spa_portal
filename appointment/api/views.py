from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from appointment.api.serializers import *


class TimeSlotViewSet(generics.ListAPIView):
    serializer_class = TimeSlotSerializer
    queryset = TimeSlot.objects.all()



class YearOfDateViewSet(APIView):

    def get_object(self, pk):
        try:
            return YearOfWeekDay.objects.get(pk=pk)
        except YearOfWeekDay.DoesNotExist:
            return None

    def get(self, request, *args, **kwargs):
        yearOfWeekDays = YearOfWeekDay.objects.all()
        serializer = YearOfWeekDaySerializer(yearOfWeekDays, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            'week_day': request.data.get('week_day'),
            'time_slots': request.data.get('time_slots')
        }
        serializer = YearOfWeekDaySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AppointmentViewSet(APIView):
    def get_object(self, pk):
        try:
            return Appointment.objects.get(pk=pk)
        except Appointment.DoesNotExist:
            return None

    def get(self, request, *args, **kwargs):
        appointments = Appointment.objects.all()
        serializer = AppointmentSerializer(appointments, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        # data = {
        #     'shop_id': request.data.get('shop_id'),
        #     'staff_id': request.data.get('staff_id'),
        #     'profile_id': request.data.get('profile_id'),
        #     'booking_day': request.data.get('booking_day'),
        #     'booking_time': request.data.get('booking_time'),
        #     'full_name': request.data.get('full_name'),
        #     'phone': request.data.get('phone'),
        #     'notes': request.data.get('notes'),
        #     'appointment_status': request.data.get('appointment_status')
        # }
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AppointmentDetailViewSet(APIView):
    def get(self, request, *args, **kwargs):
        appointment = Appointment.objects.get(pk=kwargs['id'])
        serializer = AppointmentSerializer(appointment, many=True, context={'request': request})
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        appointment = Appointment.objects.get(pk=kwargs['id'])
        serializer = AppointmentSerializer(appointment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        appointment = Appointment.objects.get(pk=kwargs['id']).delete()
        return Response({'message': f'Appointment with ID :  {kwargs["id"]} is deleted'})


class BookingViewSet(APIView):
    def get(self, request, *args, **kwargs):
        bookings = Booking.objects.all()
        serializer = BookingSerializer(bookings, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ViewerBookingViewSet(generics.ListAPIView):
    serializer_class = ViewerBookingSerializer
    queryset = Booking.objects.all()


class AppointmentViewByWeekDayViewSet(APIView):
    def get(self, request, *args, **kwargs):
        years = YearOfWeekDay.objects.filter(week_day=kwargs.get('week_day'))
        staffs = StaffProfile.objects.all()
        time_slots = YearOfWeekDaySerializer(years, many=True)
        staff_data = ViewerStaffSerializer(staffs, many=True)

        response_data = {}
        response_data['time_slots'] = time_slots.data
        response_data['nail_specialists'] = staff_data.data
        response_data['services'] = []
        return Response(data=response_data, status=status.HTTP_200_OK)


class ViewAccountViewSet(generics.ListAPIView):
    serializer_class = ViewerStaffSerializer
    queryset = StaffProfile.objects.all()


class MyViewerBookingByIdViewSet(APIView):
    def get(self, request, *args, **kwargs):
        bookings = Booking.objects.filter(appointment_id__profile_id=kwargs.get('profile_id'))
        serializer = ViewerBookingSerializer(bookings, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class MyViewerBookingViewSet(APIView):
    def get(self, request, *args, **kwargs):
        # appointment_status
        bookings = Booking.objects.filter(appointment_id__profile_id=kwargs.get('profile_id')).filter(appointment_id__appointment_status=kwargs.get('status'))
        serializer = ViewerBookingSerializer(bookings, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

