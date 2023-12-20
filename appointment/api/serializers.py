from rest_framework import serializers
from appointment.models import *


class TimeSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeSlot
        fields = ['id', 'time', 'status']


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'name']


class BookingSerializer(serializers.ModelSerializer):
    packages = ServiceSerializer(read_only=True, many=True)
    class Meta:
        model = Booking
        fields = ['appointment_id', 'packages']

    def create(self, validated_data):
        packages = self.initial_data['packages']

        services = []
        for package in packages:
            services.append(Service.objects.get(pk=package['id']))

        booking = Booking.objects.create(**validated_data)
        booking.packages.set(services)
        return booking


class ViewerAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'


class ViewerStaffSerializer(serializers.ModelSerializer):
    user = ViewerAccountSerializer(read_only=True)
    class Meta:
        model = StaffProfile
        fields = '__all__'


class ViewerProfileSerializer(serializers.ModelSerializer):
    user = ViewerAccountSerializer(read_only=True)
    class Meta:
        model = Profile
        fields = '__all__'


class AppointmentSerializer(serializers.ModelSerializer):
    # appointments = BookingSerializer(many=True, read_only=True)
    staff_id = ViewerStaffSerializer(read_only=True)
    profile_id = ViewerProfileSerializer(read_only=True)
    class Meta:
        model = Appointment
        fields = ['id', 'shop_id', 'staff_id', 'profile_id', 'booking_day', 'booking_time',
                  'amount', 'notes', 'appointment_status']


class ViewerServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class YearOfWeekDaySerializer(serializers.ModelSerializer):
    time_slots = TimeSlotSerializer(many=True, read_only=True)
    staff_members = ViewerStaffSerializer(many=True, read_only=True)
    class Meta:
        model = YearOfWeekDay
        fields = ['id', 'week_day', 'time_slots', 'is_booking', 'staff_members']


class ViewerBookingSerializer(serializers.ModelSerializer):
    appointment_id = AppointmentSerializer(read_only=True)
    packages = ViewerServiceSerializer(many=True, read_only=True)
    class Meta:
        model = Appointment
        fields = ['appointment_id', 'packages']


