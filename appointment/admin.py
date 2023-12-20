from django.contrib import admin
from django.forms import CheckboxSelectMultiple

from appointment.forms import *


class TimeSlotAdmin(admin.ModelAdmin):
    form = TimeSlotCreateForm
    list_display = ['id', 'time', 'status']
    list_display_links = ['id', 'time']
    list_per_page = 12
    ordering = ['id']


class YearOfWeekDayAdmin(admin.ModelAdmin):
    form = YearOfDateCreateForm
    list_display = ['week_day', ]
    # list_display_links = ['week_day']
    # list_per_page = 12
    filter_horizontal = ['time_slots']

    # formfield_overrides = {
    #     models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    # }


class AppointmentAdmin(admin.ModelAdmin):
    form = AppointmentCreateForm
    model = Appointment
    formfield_overrides = {
        models.DateField: {'widget': PastDatePickerWidget}
    }
    list_display = [
        '__str__',
        'status',
    ]
    ordering = ['-booking_day']


admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(YearOfWeekDay, YearOfWeekDayAdmin)
admin.site.register(TimeSlot, TimeSlotAdmin)
admin.site.register(Booking)
