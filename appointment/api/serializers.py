from rest_framework import serializers
from appointment.models import *


class TimeSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeSlot
        fields = ['id', 'time', 'status']


class YearOfWeekDaySerializer(serializers.ModelSerializer):
    time_slots = TimeSlotSerializer(many=True, read_only=True)
    class Meta:
        model = YearOfWeekDay
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['name']


class BookingSerializer(serializers.ModelSerializer):
    packages = ServiceSerializer(many=True)
    class Meta:
        model = Booking
        fields = ['appointment_id', 'packages']


class AppointmentSerializer(serializers.ModelSerializer):
    # appointments = BookingSerializer(many=True, read_only=True)
    class Meta:
        model = Appointment
        fields = '__all__'




