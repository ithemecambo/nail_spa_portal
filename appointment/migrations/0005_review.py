# Generated by Django 4.2.7 on 2023-12-25 02:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        (
            "appointment",
            "0004_alter_appointment_options_appointment_full_name_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="Review",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("status", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "full_name",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="Full Name"
                    ),
                ),
                (
                    "email",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="Email"
                    ),
                ),
                (
                    "phone",
                    models.CharField(
                        blank=True, max_length=20, null=True, verbose_name="Phone"
                    ),
                ),
                (
                    "rating_num",
                    models.IntegerField(default=0, verbose_name="Rating Number"),
                ),
                (
                    "comment",
                    models.TextField(blank=True, null=True, verbose_name="Comment"),
                ),
                (
                    "appointment_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reviews",
                        to="appointment.appointment",
                        verbose_name="Appointment",
                    ),
                ),
            ],
            options={"abstract": False,},
        ),
    ]
