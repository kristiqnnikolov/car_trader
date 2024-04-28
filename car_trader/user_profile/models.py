# user_profile models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils.text import slugify

from django.core.validators import (
    MinLengthValidator,
    MaxValueValidator,
    MinValueValidator,
)
from ..core.validators import (
    PHONE_NUMBER_LENGTH,
    INFO_MAX_LENGTH,
    MAX_PRICE,
    MAX_HORSEPOWER,
    MyCustomIntegerField,
)
from ..core.brand_model_choices import BRAND_CHOICES, MODEL_CHOICES
from ..core.other_choices import (
    REGION_CHOICES,
    ENGINE_CHOICES,
    EUROSTANDARD_CHOICES,
    COUPE_CHOICES,
    GEARBOX_CHOICES,
    CURRENCY_CHOICES,
    MILEAGE_CHOICES,
    MONTH_CHOICES,
    YEAR_CHOICES,
    COLOR_CHOICES,
    WHEEL_CHOICES,
    DOORS_CHOICES,
)


class CustomUser(AbstractUser):
    phone_number = models.CharField(
        validators=[
            MinLengthValidator(
                PHONE_NUMBER_LENGTH,
                message="Телефонният номер трябва да бъде с дължина от 10 цифри",
            )
        ],
        max_length=PHONE_NUMBER_LENGTH,
        blank=True,
    )
    region = models.CharField(blank=True, choices=REGION_CHOICES)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.username)
        super().save(*args, **kwargs)


class MyCustomIntegerField(models.IntegerField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("validators", []).append(MaxValueValidator(MAX_PRICE))
        kwargs.setdefault("default", 10)
        super().__init__(*args, **kwargs)


class MyCustomCharField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("max_length", INFO_MAX_LENGTH)
        kwargs.setdefault("blank", True)
        kwargs.setdefault("null", True)
        super().__init__(*args, **kwargs)

