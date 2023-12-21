from rest_framework import serializers
from appointment.models import *


class TimeSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeSlot
        fields = ['id', 'time', 'status']


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        # fields = ['id', 'parent', 'name', 'price', 'symbol', 'photo_url',
        #           'is_selected', 'description']
        fields = ['id']


class BookingSerializer(serializers.ModelSerializer):
    packages = ServiceSerializer(read_only=True, many=True)
    class Meta:
        model = Booking
        fields = ['appointment_id', 'packages']

    def create(self, validated_data):
        packages = self.initial_data['packages']

        services = []
        # packages = validated_data.pop('packages')
        for package in packages:
            # services.append(Service.objects.get(pk=package['id']))
            try:
                services.append(Service.objects.get(pk=package['id']))
            except TypeError as error:
                print(f'Exception: {str(error)}')
            # print(packages)
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
    # staff_id = ViewerStaffSerializer(read_only=True)
    # profile_id = ViewerProfileSerializer(read_only=True)
    class Meta:
        model = Appointment
        fields = ['id', 'shop_id', 'staff_id', 'profile_id', 'booking_day', 'booking_time',
                  'amount', 'notes', 'full_name', 'phone', 'appointment_status']


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


class ViewerAppointmentSerializer(serializers.ModelSerializer):
    staff_id = ViewerStaffSerializer(read_only=True)
    profile_id = ViewerProfileSerializer(read_only=True)
    class Meta:
        model = Appointment
        fields = '__all__'


class ViewerBookingSerializer(serializers.ModelSerializer):
    appointment_id = ViewerAppointmentSerializer(read_only=True)
    packages = ServiceSerializer(read_only=True, many=True)
    class Meta:
        model = Booking
        fields = '__all__'


class MyViewerBookingSerializer(serializers.ModelSerializer):
    appointments = ViewerAppointmentSerializer(read_only=True)
    # packages = ViewerServiceSerializer(many=True, read_only=True)
    bookings = ViewerBookingSerializer(many=True, read_only=True)

    class Meta:
        model = Appointment
        fields = '__all__'
        # fields = ['id', 'shop_id', 'staff_id', 'profile_id', 'booking_day', 'booking_time',
        #           'amount', 'notes', 'appointment_status', 'bookings', 'appointment_id']


