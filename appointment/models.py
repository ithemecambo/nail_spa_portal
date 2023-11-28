from shop.models import *


class TimeSlot(BaseModel):
    time = models.CharField(max_length=15, verbose_name='Time')
    is_booking = models.BooleanField(default=False, blank=True, null=True)

    class Meta:
        verbose_name = 'TimeSlot'
        verbose_name_plural = 'TimeSlots'
        unique_together = ['time']

    def __str__(self):
        return f'{self.time} {self.is_booking}'


class Appointment(BaseModel):
    shop_id = models.ForeignKey(Shop, on_delete=models.CASCADE, verbose_name='Shop')
    booking_day = models.DateField(verbose_name='Booking Day')
    booking_time = models.ForeignKey(TimeSlot, on_delete=models.CASCADE, verbose_name='Booking Time')
    amount = models.FloatField(blank=False, null=False, verbose_name='Amount', default=0)

    class Meta:
        verbose_name = 'Appointment'
        verbose_name_plural = 'Appointments'

    def __str__(self):
        return f'{self.shop_id}\t|\t{self.booking_day}'


class Booking(BaseModel):
    appointment_id = models.ForeignKey(Appointment, on_delete=models.CASCADE,
                                       verbose_name='Booking')
    packages = models.ManyToManyField(Service, verbose_name='Booking Service')

    class Meta:
        verbose_name = 'Booking'
        verbose_name_plural = 'Bookings'

    def __str__(self):
        return f'{self.appointment_id.__str__()}'
