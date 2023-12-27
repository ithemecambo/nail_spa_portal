from django.utils.html import format_html

from account.models import *
from shop.models import *


class TimeSlot(BaseModel):
    time = models.CharField(max_length=15, verbose_name='Time')

    class Meta:
        verbose_name = 'TimeSlot'
        verbose_name_plural = 'TimeSlots'
        unique_together = ['time']

    def __str__(self):
        return f'{self.time}'


class YearOfWeekDay(BaseModel):
    week_day = models.CharField(max_length=25, blank=True, null=True)
    time_slots = models.ManyToManyField(TimeSlot, verbose_name='Time Slots',
                                        related_name='time_slots')
    is_booking = models.BooleanField(default=False, blank=True, null=True)

    class Meta:
        verbose_name = 'YearOfWeekDay'
        verbose_name_plural = 'YearOfWeekDays'
        ordering = ['created_at']

    def __str__(self):
        return f'{self.time_slots}'


APPOINTMENT_STATUS_CHOICES = (
    ('Pending', 'Pending'),
    ('Upcoming', 'Upcoming'),
    ('Completed', 'Completed'),
    ('Cancelled', 'Cancelled'),
)


class Appointment(BaseModel):
    shop_id = models.ForeignKey(Shop, on_delete=models.CASCADE, verbose_name='Shop',
                                related_name='appointments')
    staff_id = models.ForeignKey(StaffProfile, on_delete=models.CASCADE, verbose_name='Staff',
                                 related_name='appointments')
    profile_id = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Profile',
                                   related_name='appointments')
    booking_day = models.DateField(verbose_name='Booking Day')
    booking_time = models.CharField(max_length=10, verbose_name='Booking Time')
    full_name = models.CharField(max_length=50, blank=True, null=True, default='', verbose_name='Full Name')
    phone = models.CharField(max_length=20, blank=True, null=True, default='', verbose_name='Phone')
    amount = models.FloatField(blank=False, null=False, verbose_name='Amount', default=0)
    notes = models.TextField(verbose_name='Notes', blank=True, null=True)
    appointment_status = models.CharField(choices=APPOINTMENT_STATUS_CHOICES, max_length=30, default='Upcoming',
                                          verbose_name='Appointment Status')

    class Meta:
        verbose_name = 'Appointment'
        verbose_name_plural = 'Appointments'
        ordering = ['-booking_day', 'booking_time']

    def __str__(self):
        return f'{self.booking_day}\t|\t{self.booking_time}'

    def profile(self):
        return f'[{self.profile_id.id}] - {self.profile_id.user.first_name} {self.profile_id.user.last_name}'

    def check_appointment_status(self):
        if self.appointment_status == 'Pending':
            return format_html('<span style="color: #546E7A; font-weight: bold;">{0}</span>',
                               self.appointment_status.upper())
        elif self.appointment_status == 'Upcoming':
            return format_html('<span style="color: #2979FF; font-weight: bold;">{0}</span>',
                               self.appointment_status.upper())
        elif self.appointment_status == 'Completed':
            return format_html('<span style="color: #43A047; font-weight: bold;">{0}</span>',
                               self.appointment_status.upper())
        return format_html('<span style="color: #DD2C00; font-weight: bold;">{0}</span>',
                           self.appointment_status.upper())

    check_appointment_status.short_description = 'appointment_status'


class Booking(BaseModel):
    appointment_id = models.ForeignKey(Appointment, on_delete=models.CASCADE,
                                       verbose_name='Booking', related_name='bookings')
    packages = models.ManyToManyField(Service, verbose_name='Booking Service', related_name='bookings')

    class Meta:
        verbose_name = 'Booking'
        verbose_name_plural = 'Bookings'
        unique_together = ['appointment_id']

    def __str__(self):
        return f'{self.appointment_id}'

    def appointment_status(self):
        if self.appointment_id.appointment_status == 'Pending':
            return format_html('<span style="color: #546E7A; font-weight: bold;">{0}</span>',
                               self.appointment_id.appointment_status.upper())
        elif self.appointment_id.appointment_status == 'Upcoming':
            return format_html('<span style="color: #2979FF; font-weight: bold;">{0}</span>',
                               self.appointment_id.appointment_status.upper())
        elif self.appointment_id.appointment_status == 'Completed':
            return format_html('<span style="color: #43A047; font-weight: bold;">{0}</span>',
                               self.appointment_id.appointment_status.upper())
        return format_html('<span style="color: #DD2C00; font-weight: bold;">{0}</span>',
                           self.appointment_id.appointment_status.upper())
    appointment_status.short_description = 'appointment_status'

    def who_make_an_appointment(self):
        return f'[{self.appointment_id.profile_id.id}] - {self.appointment_id.profile_id.user.first_name} ' \
               f'{self.appointment_id.profile_id.user.last_name}'
    who_make_an_appointment.short_description = 'who_make_an_appointment'


class Review(BaseModel):
    appointment_id = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name='reviews',
                                       verbose_name='Appointment')
    profile_id = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='reviews',
                                   verbose_name='Profile')
    rating_num = models.IntegerField(default=0, verbose_name='Rating Number')
    comment = models.TextField(blank=True, null=True, verbose_name='Comment')

    def __str__(self):
        return f'{self.appointment_id} | {self.profile_id}'

    def get_full_name(self):
        return f'{self.profile_id.user.first_name} {self.profile_id.user.last_name}'
    get_full_name.short_description = 'Full Name'

    def get_phone_number(self):
        return f'{self.profile_id.phone}'
    get_phone_number.short_description = 'Phone'

    def get_email_address(self):
        return f'{self.profile_id.user.email}'
    get_email_address.short_description = 'Email'

    def make_an_appointment(self):
        return f'{self.appointment_id.booking_day} | {self.appointment_id.booking_time}'
    make_an_appointment.short_description = 'Appointment'

    # ⭐ ★☆ 💫
    def rating_star(self):
        if self.rating_num == 1:
            return '⭐'
        elif self.rating_num == 2:
            return '⭐⭐'
        elif self.rating_num == 3:
            return '⭐⭐⭐'
        elif self.rating_num == 4:
            return '⭐⭐⭐⭐'
        elif self.rating_num == 5:
            return '⭐⭐⭐⭐⭐'
        else:
            return '⭐⭐⭐⭐⭐'
    rating_star.short_description = 'Star'
