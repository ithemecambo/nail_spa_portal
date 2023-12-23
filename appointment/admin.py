from django.contrib import admin
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
    filter_horizontal = ['time_slots']


class AppointmentAdmin(admin.ModelAdmin):
    form = AppointmentCreateForm
    model = Appointment
    formfield_overrides = {
        models.DateField: {'widget': PastDatePickerWidget}
    }
    list_display = [
        'id',
        '__str__',
        'full_name',
        'phone',
        'status',
    ]
    list_display_links = [
        '__str__',
        'full_name',
        'phone',
    ]
    ordering = ['-booking_day', '-booking_time']
    list_per_page = 15


class BookingAdmin(admin.ModelAdmin):
    list_display = ['id', 'appointment_id', 'status']
    list_display_links = ['id', 'appointment_id']
    list_per_page = 15


admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(YearOfWeekDay, YearOfWeekDayAdmin)
admin.site.register(TimeSlot, TimeSlotAdmin)
admin.site.register(Booking, BookingAdmin)
