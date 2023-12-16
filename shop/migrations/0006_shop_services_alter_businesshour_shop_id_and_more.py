# Generated by Django 4.2.7 on 2023-12-07 06:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0005_alter_gallery_shop_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="shop",
            name="services",
            field=models.ManyToManyField(to="shop.service", verbose_name="Service"),
        ),
        migrations.AlterField(
            model_name="businesshour",
            name="shop_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="businessHours",
                to="shop.shop",
                verbose_name="Shop",
            ),
        ),
        migrations.AlterField(
            model_name="promotion",
            name="shop_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="promotions",
                to="shop.shop",
                verbose_name="Shop",
            ),
        ),
    ]