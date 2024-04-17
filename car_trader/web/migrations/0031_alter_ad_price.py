# Generated by Django 5.0.2 on 2024-02-18 19:47

import car_trader.web.validators
import django.core.validators
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0030_remove_ad_horse_power'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='price',
            field=car_trader.web.validators.MyCustomIntegerField(default=10, validators=[django.core.validators.MaxValueValidator(1000000)]),
        ),
    ]
