from rest_framework import generics
from rest_framework.views import APIView

from appointment.api.serializers import *


class TimeSlotViewSet(generics.ListAPIView):
    serializer_class = TimeSlotSerializer
    queryset = TimeSlot.objects.all()



class YearOfDateViewSet(APIView):

    def post(self, request, *args, **kwargs):
        timeslots = TimeSlot.objects.all()
