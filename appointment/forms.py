from datetime import date
from django import forms
from django.contrib.admin.widgets import AdminTimeWidget, FilteredSelectMultiple

from appointment.models import *


class TimeSlotCreateForm(forms.ModelForm):
    class Meta:
        model = TimeSlot
        fields = ['time']


class YearOfDateCreateForm(forms.ModelForm):
    time_slots = forms.ModelMultipleChoiceField(queryset=TimeSlot.objects.all())
    class Meta:
        model = YearOfWeekDay
        fields = ['week_day', 'time_slots']

    # def __init__(self, *args, **kwargs):
    #     forms.ModelForm.__init__(self, *args, **kwargs)
    #     self.fields['time_slots'].queryset = TimeSlot


class DatePickerWidget(forms.DateInput):
    DATA_INPUT_WIDGET_REQUIRED_FORMAT = '%Y-%m-%d'

    def __init__(self, attrs={}, format=None):
        attrs.update (
            {
                'class': 'form-control',
                'type': 'date'
            }
        )
        self.format = format or self.DATA_INPUT_WIDGET_REQUIRED_FORMAT
        super().__init__(attrs, format=self.format)


class PastDatePickerWidget(DatePickerWidget):
    def __init__(self, attrs={}, format=None):
        attrs.update({'min': date.today()})
        super().__init__(attrs, format=format)


class AppointmentCreateForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = [
            'shop_id',
            'full_name',
            'phone',
            'booking_day',
            'booking_time',
            'amount',
            'notes'
        ]
        widget = {
            'booking_hour': AdminTimeWidget(format='%H:%M')
        }
