# Generated by Django 4.2.7 on 2023-12-20 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("appointment", "0003_alter_booking_unique_together"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="appointment",
            options={
                "ordering": ["-booking_day", "booking_time"],
                "verbose_name": "Appointment",
                "verbose_name_plural": "Appointments",
            },
        ),
        migrations.AddField(
            model_name="appointment",
            name="full_name",
            field=models.CharField(
                blank=True,
                default="",
                max_length=50,
                null=True,
                verbose_name="Full Name",
            ),
        ),
        migrations.AddField(
            model_name="appointment",
            name="phone",
            field=models.CharField(
                blank=True, default="", max_length=20, null=True, verbose_name="Phone"
            ),
        ),
    ]
