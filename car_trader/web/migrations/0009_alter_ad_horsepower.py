# Generated by Django 5.0.2 on 2024-02-18 17:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_alter_ad_horsepower_alter_ad_mileage_alter_ad_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='horsepower',
            field=models.CharField(validators=[django.core.validators.MaxValueValidator(1000)]),
        ),
    ]