# Generated by Django 4.2.7 on 2023-12-15 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0005_alter_profile_user_alter_staffprofile_user"),
        ("shop", "0013_remove_shop_users_shop_staffs"),
    ]

    operations = [
        migrations.AlterField(
            model_name="shop",
            name="staffs",
            field=models.ManyToManyField(
                related_name="staffs", to="account.staffprofile", verbose_name="Staff"
            ),
        ),
    ]
