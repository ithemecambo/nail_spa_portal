# Generated by Django 4.2.7 on 2023-12-15 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0005_alter_profile_user_alter_staffprofile_user"),
        ("shop", "0012_alter_shop_users"),
    ]

    operations = [
        migrations.RemoveField(model_name="shop", name="users",),
        migrations.AddField(
            model_name="shop",
            name="staffs",
            field=models.ManyToManyField(
                to="account.staffprofile", verbose_name="Staff"
            ),
        ),
    ]