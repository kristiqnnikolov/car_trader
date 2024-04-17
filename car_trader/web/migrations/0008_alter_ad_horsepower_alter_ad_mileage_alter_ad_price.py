# Generated by Django 5.0.2 on 2024-02-18 17:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_alter_ad_brand_alter_ad_horsepower_alter_ad_info_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='horsepower',
            field=models.CharField(default=12, validators=[django.core.validators.MaxValueValidator(1000)]),
        ),
        migrations.AlterField(
            model_name='ad',
            name='mileage',
            field=models.CharField(default='value'),
        ),
        migrations.AlterField(
            model_name='ad',
            name='price',
            field=models.CharField(default=0, validators=[django.core.validators.MaxValueValidator(1000000)]),
        ),
    ]
