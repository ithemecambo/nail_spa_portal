# Generated by Django 4.2.7 on 2023-12-15 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0005_alter_profile_user_alter_staffprofile_user"),
        ("shop", "0010_rename_isselected_service_is_selected"),
    ]

    operations = [
        migrations.AlterField(
            model_name="shop",
            name="users",
            field=models.ManyToManyField(
                to="account.staffprofile", verbose_name="User"
            ),
        ),
    ]