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
        'profile',
        'full_name',
        'phone',
        'check_appointment_status',
        'status',
    ]
    list_display_links = [
        '__str__',
        'profile',
        'full_name',
        'phone',
    ]
    search_fields = ['booking_day', 'booking_time']
    ordering = ['-booking_day', '-booking_time']
    list_filter = ['appointment_status', 'status']
    list_per_page = 12


class BookingAdmin(admin.ModelAdmin):
    list_display = ['id', 'appointment_id', 'who_make_an_appointment', 'appointment_status', 'status']
    search_fields = ['appointment_id__booking_day', 'appointment_id__booking_time']
    list_display_links = ['id', 'appointment_id', 'who_make_an_appointment']
    list_filter = ['appointment_id__appointment_status', 'status']
    list_per_page = 12


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['make_an_appointment', 'get_full_name', 'get_phone_number', 'get_email_address', 'rating_star']
    list_display_links = ['make_an_appointment', 'get_full_name', 'get_phone_number', 'get_email_address']
    list_filter = ['rating_num', 'status']
    search_fields = ['comment']
    list_per_page = 12


admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(YearOfWeekDay, YearOfWeekDayAdmin)
admin.site.register(TimeSlot, TimeSlotAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(Review, ReviewAdmin)
