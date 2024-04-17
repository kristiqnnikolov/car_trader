# Generated by Django 5.0.2 on 2024-02-18 19:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0022_alter_carbrand_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='horse_power',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(1000)]),
        ),
    ]
