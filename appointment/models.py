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


class Booking(BaseModel):
    appointment_id = models.ForeignKey(Appointment, on_delete=models.CASCADE,
                                       verbose_name='Booking', related_name='bookings')
    packages = models.ManyToManyField(Service, verbose_name='Booking Service', related_name='bookings')

    class Meta:
        verbose_name = 'Booking'
        verbose_name_plural = 'Bookings'
        unique_together = ['appointment_id']

    def __str__(self):
        return f'{self.appointment_id.__str__()}'


