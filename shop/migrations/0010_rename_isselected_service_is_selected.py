# Generated by Django 4.2.7 on 2023-12-15 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0009_service_isselected"),
    ]

    operations = [
        migrations.RenameField(
            model_name="service", old_name="isSelected", new_name="is_selected",
        ),
    ]
