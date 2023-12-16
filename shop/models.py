from django.contrib.humanize.templatetags.humanize import intcomma
from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe
from account.models import Account, StaffProfile

DEVICE_CHOICES = (
    ('All', 'All'),
    ('Web', 'Web'),
    ('iOS', 'iOS'),
    ('Android', 'Android')
)


class BaseModel(models.Model):
    status = models.BooleanField(default=True, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        abstract = True


class Service(BaseModel):
    parent = models.ForeignKey('Service', related_name='children', on_delete=models.CASCADE,
                               null=True, blank=True, db_index=True)
    name = models.CharField(max_length=100, blank=False, null=False, verbose_name='Name')
    price = models.FloatField(blank=True, null=True, verbose_name='Price')
    symbol = models.CharField(max_length=2, blank=True, null=True, verbose_name='Symbol')
    photo_url = models.ImageField(upload_to='services/%Y-%m-%d/', verbose_name='Photo',
                                  help_text='Allows size is 20MB', blank=True, null=True)
    description = models.TextField(blank=True, null=True, verbose_name='Description')
    is_selected = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = 'Services'
        unique_together = ('name',)
        # ordering = ('id',)

    def __str__(self):
        full_path = [self.name]
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return ' -> '.join(full_path[::-1])

    def service_photo(self):
        if self.photo_url:
            return mark_safe('<img src="%s" style="width: 25px; height: 25px;"/>' % self.photo_url.url)
        else:
            return '__'
    service_photo.short_description = 'Logo'

    def service_name(self):
        if self.price is None:
            return self.name.upper()
        else:
            return self.name.title()
    service_name.short_description = 'Name'

    def service_price(self):
        if self.price is not None and self.symbol is not None:
            dollars = round(int(self.price), 0)
            return "${}{}".format(dollars, self.symbol)
        elif self.price is not None and self.symbol is None:
            dollars = round(int(self.price), 0)
            return "${}".format(dollars)
        else:
            return ''
    service_price.short_description = 'Price'


class Shop(BaseModel):
    staffs = models.ManyToManyField(StaffProfile, verbose_name='Staff')
    services = models.ManyToManyField(Service, verbose_name='Service')
    shop_name = models.CharField(max_length=100, blank=False, null=False, verbose_name='Shop Name')
    tel = models.CharField(max_length=20, blank=False, null=False, verbose_name='Tel')
    fax = models.CharField(max_length=20, blank=False, null=False, verbose_name='Fax')
    email = models.EmailField(max_length=100, blank=False, null=False, verbose_name='Email')
    website = models.CharField(max_length=100, blank=True, null=True, verbose_name='Website')
    twitter = models.CharField(max_length=120, blank=True, null=True, verbose_name='Twitter')
    facebook = models.CharField(max_length=120, blank=True, null=True, verbose_name='Facebook')
    linkedin = models.CharField(max_length=120, blank=True, null=True, verbose_name='LinkedIn')
    instagram = models.CharField(max_length=120, blank=True, null=True, verbose_name='Instagram')
    address = models.CharField(max_length=250, blank=False, null=False, verbose_name='Address')
    latitude = models.FloatField(blank=False, null=False, verbose_name='Latitude', default=0)
    longitude = models.FloatField(blank=False, null=False, verbose_name='Longitude', default=0)
    banner_url = models.ImageField(upload_to='shops/shops/banners/%Y-%m-%d/', verbose_name='Banner URL',
                                   blank=True, null=True, help_text='Allow size is 10MB')
    logo_url = models.ImageField(upload_to='shops/shops/logos/%Y-%m-%d/', verbose_name='Logo URL',
                                 blank=True, null=True, help_text='Allow size is 5MB')
    about = models.TextField(blank=True, null=True, verbose_name='About')

    class Meta:
        verbose_name = "Shop"
        verbose_name_plural = 'Shops'
        unique_together = ['shop_name', 'tel', 'email', 'address']

    def __str__(self):
        return f'{self.shop_name}'

    def shop_banner_photo(self):
        if self.banner_url:
            return mark_safe('<img src="%s" style="width: auto; height: 55px;" />' % self.banner_url.url)
        else:
            return '__'
    shop_banner_photo.short_description = 'Banner'

    def shop_logo_photo(self):
        if self.logo_url:
            return mark_safe('<img src="%s" style="width: auto; height: 55px;" />' % self.logo_url.url)
        else:
            return '__'
    shop_logo_photo.short_description = 'Logo'

    def get_absolute_url(self):
        return reverse('job-detail', kwargs={
            'shop_name': self.shop_name.replace('/', '-'),
            'pk': self.id
        })


class Gallery(BaseModel):
    shop_id = models.ForeignKey(Shop, related_name='galleries', on_delete=models.CASCADE, verbose_name='Shop')
    photo_url = models.ImageField(upload_to='shops/shops/galleries/%Y-%m-%d/', verbose_name='Photo',
                                  blank=True, null=True, help_text='Allow size is 20MB')

    class Meta:
        verbose_name = 'Gallery'
        verbose_name_plural = 'Galleries'

    def __str__(self):
        return f'{self.shop_id}'

    def gallery_photo(self):
        if self.photo_url:
            return mark_safe('<img src="%s" style="width: auto; height: 55px;" />' % self.photo_url.url)
        else:
            return '__'
    gallery_photo.short_description = 'Album'


class BusinessHour(BaseModel):
    shop_id = models.ForeignKey(Shop, related_name='business_hours', on_delete=models.CASCADE, verbose_name='Shop')
    day = models.CharField(max_length=25, blank=False, null=False, verbose_name='Day')
    hour = models.CharField(max_length=25, blank=False, null=False, verbose_name='Hour')

    class Meta:
        verbose_name = 'BusinessHour'
        verbose_name_plural = 'BusinessHours'

    def __str__(self):
        return f'{self.shop_id}'


# TODO: Refer to settings app
# TODO: Auto register when application is started open in the first installation or download from app store
class Platform(BaseModel):
    platform_name = models.CharField(choices=DEVICE_CHOICES, max_length=15, default='All',
                                     verbose_name='Platform Name')
    ip = models.CharField(max_length=20, blank=False, null=False, verbose_name='IP Address')
    device = models.CharField(max_length=100, blank=False, null=False, verbose_name='Device')
    uuid = models.CharField(max_length=250, blank=False, null=False, verbose_name='UUID')

    class Meta:
        verbose_name = 'Platform'
        verbose_name_plural = 'Platforms'

    def __str__(self):
        return f'{self.platform_name}'


# # TODO: Send broadcast ads specific our customers
class Notification(BaseModel):
    platform_id = models.ForeignKey(Platform, on_delete=models.CASCADE, verbose_name='Platform')
    title = models.CharField(max_length=100, verbose_name='Title')
    subtitle = models.CharField(max_length=250, verbose_name='Sub Title')
    photo_url = models.ImageField(upload_to='shops/notifications/%Y-%m-%d/', verbose_name='Photo URL',
                                  help_text='Allowed size is 20MB', blank=False, null=False)
    message = models.TextField(blank=True, null=True, verbose_name='Message')

    class Meta:
        verbose_name = 'Notification'
        verbose_name_plural = 'Notifications'

    def __str__(self):
        return f'{self.title}'

    def banner_notification_photo(self):
        if self.photo_url:
            return mark_safe('<img src="%s" style="width: auto; height:55px;" />' % self.photo_url.url)
        else:
            return '__'
    banner_notification_photo.short_description = 'Banner'


class Promotion(BaseModel):
    shop_id = models.ForeignKey(Shop, related_name='promotions', on_delete=models.CASCADE, verbose_name='Shop')
    service_id = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name='Service')
    title = models.CharField(max_length=100, blank=False, null=False, verbose_name='Title')
    subtitle = models.CharField(max_length=250, blank=False, null=False, verbose_name='SubTitle')
    discount = models.FloatField(null=False, blank=False, verbose_name='Discount')
    color = models.CharField(max_length=10, blank=False, null=False, verbose_name='Color',
                             help_text='Hex Color [Ex: #C3C3C3]', default='#')
    photo_url = models.ImageField(upload_to='shops/promotions/%Y-%m-%d/', verbose_name='Photo URL',
                                  blank=False, null=False, help_text='Allow size is 10MB')

    class Meta:
        verbose_name = 'Promotion'
        verbose_name_plural = 'Promotions'

    def __str__(self):
        return f'{self.title}'

    def banner_promotion_photo(self):
        if self.photo_url:
            return mark_safe('<img src="%s" style="width: auto; height: 55px;" />' % self.photo_url.url)
        else:
            return '__'
    banner_promotion_photo.short_description = 'Banner'
