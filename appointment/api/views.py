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
        serializer = serializers.YearOfWeekDaySerializer(yearOfWeekDays, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            'week_day': request.data.get('week_day'),
            'time_slots': request.data.get('time_slots')
        }
        serializer = serializers.YearOfWeekDaySerializer(data=data)
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
        serializer = serializers.AppointmentSerializer(appointments, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            'shop_id': request.data.get('shop_id'),
            'staff_id': request.data.get('staff_id'),
            'profile_id': request.data.get('profile_id'),
            'booking_day': request.data.get('booking_day'),
            'booking_time': request.data.get('booking_time'),
            'notes': request.data.get('notes'),
            'appointment_status': request.data.get('appointment_status')
        }
        serializer = serializers.AppointmentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

