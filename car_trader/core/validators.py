PHONE_NUMBER_LENGTH = 10
INFO_MAX_LENGTH = 100
MAX_HORSEPOWER = 1000
MAX_PRICE = 1000000
MAX_MILEAGE = 1000000
from django.db import models


class MyCustomIntegerField(models.PositiveIntegerField):
    def get_prep_value(self, value):
        return super().get_prep_value(value)
