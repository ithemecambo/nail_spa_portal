from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.mail import send_mail
from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe


USER_GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female')
)


class AccountManager(BaseUserManager):

    def create_user(self, email, password, is_active=False, is_staff=False, is_admin=False):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email))
        user.is_active = is_active
        user.is_staff = is_staff
        user.is_admin = is_admin
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_staffuser(self, email, password):
        user = self.create_user(email, password=password, )
        user.staff = True
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        return self.create_user(email, password, is_active=True, is_staff=True, is_admin=True)


class Account(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=30, null=True, verbose_name='First Name')
    last_name = models.CharField(max_length=30, null=True, verbose_name='Last Name')
    username = models.CharField(max_length=50, blank=False, null=False, verbose_name='Username')
    email = models.EmailField(unique=True, null=False, verbose_name='Email')
    password = models.CharField(max_length=128, verbose_name='Password')
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name='Date Joined')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created Date')
    updated_at = models.DateTimeField(auto_now=True, null=True, verbose_name='Updated Date')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    # 'username', 'password'
    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'

    def __str__(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()
    get_full_name.short_description = 'Full Name'

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def get_email(self):
        if self.email == '':
            return '__'
        return f'{self.email}'

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    def admin(self):
        return self.is_admin
    admin.boolean = True

    def staff(self):
        return self.is_staff
    staff.boolean = True

    def active(self):
        return self.is_active
    active.boolean = True

    def get_absolute_url(self):
        return reverse('account-detail', kwargs={
            'email': self.email.replace('/', '-'),
            'pk': self.id
        })


class Profile(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name='Phone')
    bio = models.TextField(blank=True, null=True, verbose_name='Bio')
    address = models.CharField(max_length=250, blank=True, null=True, verbose_name='Address')
    house_no = models.CharField(max_length=20, blank=True, null=True, verbose_name='House #')
    street_no = models.CharField(max_length=20, blank=True, null=True, verbose_name='Street #')
    city = models.CharField(max_length=20, blank=True, null=True, verbose_name='City')
    state = models.CharField(max_length=20, blank=True, null=True, verbose_name='State')
    zipcode = models.CharField(max_length=20, blank=True, null=True, verbose_name='Zip Code')
    status = models.BooleanField(default=True)
    photo_url = models.ImageField(upload_to='users/profiles/%Y-%m-%d/', blank=True, null=True,
                              verbose_name='Photo', help_text='Allowed size is 10MG')

    def __str__(self):
        return f'{self.user.username}'

    def name(self):
        return f'[{self.user.id}] - {self.user.first_name} {self.user.last_name}'

    def profile(self):
        if self.photo_url:
            return mark_safe('<img src="%s" style="width: 26px; height: 25px; border-radius: 100px; "/>' % self.photo_url.url)
        else:
            return '__'
    profile.short_description = 'Profile'


class StaffProfile(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE, related_name='staff')
    nickname = models.CharField(max_length=30, verbose_name='Nickname')
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name='Phone')
    fax = models.CharField(max_length=20, blank=True, null=True, verbose_name='Fax')
    ssn = models.CharField(max_length=15, blank=False, null=False, verbose_name='Social Security Number')
    license_no = models.CharField(max_length=30, blank=True, null=True, verbose_name='License No')
    expiration_date = models.CharField(max_length=20, blank=True, null=True, verbose_name='Expiration Date')
    address = models.CharField(max_length=250, verbose_name='Address')
    color = models.CharField(max_length=10, default='#')
    status = models.BooleanField(default=True)
    photo_url = models.ImageField(upload_to='users/staffs/%Y-%m-%d/', blank=True, null=True,
                              verbose_name='Photo', help_text='Allowed size is 10MG')

    def __str__(self):
        return f'{self.nickname}'

    def name(self):
        return f'{self.user.first_name} {self.user.first_name}'

    def profile(self):
        if self.photo_url:
            return mark_safe('<img src="%s" style="width: 26px; height: 25px; border-radius: 100px; "/>' % self.photo_url.url)
        else:
            return '__'
    profile.short_description = 'Profile'


