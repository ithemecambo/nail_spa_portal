from rest_framework import serializers

from appointment.models import *


class TimeSlotSerializer(serializers.Serializer):
    class Meta:
        model = TimeSlot
        fields = '__all__'


# class YearOfDateSerializer(serializers.Serializer):
#     class Meta:
#         model = YearOfDate
#         fields = '__all__'
#

