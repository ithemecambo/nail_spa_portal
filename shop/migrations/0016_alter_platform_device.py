# Generated by Django 4.2.7 on 2023-12-16 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0015_alter_shop_staffs"),
    ]

    operations = [
        migrations.AlterField(
            model_name="platform",
            name="device",
            field=models.CharField(max_length=100, verbose_name="Device"),
        ),
    ]