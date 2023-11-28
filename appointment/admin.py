from django.contrib import admin
from appointment.forms import *


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


admin.site.register(Appointment, AppointmentAdmin)
