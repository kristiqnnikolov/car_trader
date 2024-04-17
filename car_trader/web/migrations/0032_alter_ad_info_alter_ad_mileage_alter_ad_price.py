# Generated by Django 5.0.2 on 2024-02-18 19:50

import car_trader.web.models
import django.core.validators
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0031_alter_ad_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='info',
            field=car_trader.web.models.MyCustomCharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='ad',
            name='mileage',
            field=car_trader.web.models.MyCustomIntegerField(blank=True, default=10, null=True, validators=[django.core.validators.MaxValueValidator(1000000), django.core.validators.MaxValueValidator(1000000)]),
        ),
        migrations.AlterField(
            model_name='ad',
            name='price',
            field=car_trader.web.models.MyCustomIntegerField(default=10, validators=[django.core.validators.MaxValueValidator(1000000), django.core.validators.MaxValueValidator(1000000)]),
        ),
    ]
