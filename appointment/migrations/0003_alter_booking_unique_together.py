# Generated by Django 4.2.7 on 2023-12-19 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("appointment", "0002_alter_appointment_booking_time_and_more"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="booking", unique_together={("appointment_id",)},
        ),
    ]
