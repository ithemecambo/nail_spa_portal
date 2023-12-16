# Generated by Django 4.2.7 on 2023-11-28 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="service",
            name="description",
            field=models.CharField(
                blank=True, max_length=250, null=True, verbose_name="Description"
            ),
        ),
        migrations.AddField(
            model_name="service",
            name="price",
            field=models.FloatField(blank=True, null=True, verbose_name="Price"),
        ),
        migrations.AddField(
            model_name="service",
            name="symbol",
            field=models.CharField(
                blank=True, max_length=2, null=True, verbose_name="Symbol"
            ),
        ),
    ]