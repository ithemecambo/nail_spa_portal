from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from account.models import *


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def staff_member_create_profile(sender, instance, created, **kwargs):
    if created:
        StaffProfile.objects.create(user=instance)
