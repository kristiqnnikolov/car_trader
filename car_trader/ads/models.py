# ads models.py
from django.db import models
from django.conf import settings
from ..user_profile.models import MyCustomCharField
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


def user_directory_path(instance, filename):
    if instance.user:
        return f"{instance.user.username}/{filename}"
    else:
        return f"unknown_user/{filename}"

class Ad(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="ads",
        blank=True,
        null=True,
    )

    brand = models.CharField(choices=BRAND_CHOICES)
    model = models.CharField(choices=MODEL_CHOICES)
    info = MyCustomCharField()

    description = models.TextField(default="Въведете описание")
    engine = models.CharField(choices=ENGINE_CHOICES, default=ENGINE_CHOICES[0][0])
    price = MyCustomIntegerField()
    mileage = MyCustomIntegerField(blank=True, null=True)
    horsepower = MyCustomIntegerField(default="100")

    eurostandard = models.CharField(
        choices=EUROSTANDARD_CHOICES, default=EUROSTANDARD_CHOICES[0][0]
    )
    gearbox = models.CharField(choices=GEARBOX_CHOICES, default=GEARBOX_CHOICES[0][0])

    coupe_type = models.CharField(choices=COUPE_CHOICES, default=COUPE_CHOICES[0][0])

    currency = models.CharField(
        choices=CURRENCY_CHOICES, default=CURRENCY_CHOICES[0][0]
    )
    wheel = models.CharField(choices=WHEEL_CHOICES, default=WHEEL_CHOICES[0][0])

    doors = models.CharField(choices=DOORS_CHOICES, default=DOORS_CHOICES[0][0])

    month_of_production = models.CharField(
        choices=MONTH_CHOICES, default=MONTH_CHOICES[0][0]
    )
    year_of_production = models.CharField(
        choices=YEAR_CHOICES, default=YEAR_CHOICES[0][0]
    )
    color = models.CharField(choices=COLOR_CHOICES, default=COLOR_CHOICES[0][0])

    region = models.CharField(choices=REGION_CHOICES, default=REGION_CHOICES[0][0])
    image = models.ImageField(
        upload_to=user_directory_path, default="default_image.jpg"
    )
    # <------------------- Extras ------------------->
    ABS = models.BooleanField(default=False)
    airbags = models.BooleanField(default=False, verbose_name="Airbags")
    traction_control = models.BooleanField(default=False, verbose_name="Автоконтрол")
    adaptive_lights = models.BooleanField(
        default=False, verbose_name="Адаптивни светлини"
    )
    parking_sensor = models.BooleanField(default=False, verbose_name="Парктроник")
    isofix = models.BooleanField(default=False, verbose_name="Isofix")
    GPS = models.BooleanField(default=False)
    descent_control = models.BooleanField(
        default=False, verbose_name="Система за контрол на спускането"
    )
    gas_as_fuel = models.BooleanField(default=False, verbose_name="Газова уредба")
    metan_as_fuel = models.BooleanField(default=False, verbose_name="Метанова уредба")
    leasing = models.BooleanField(default=False, verbose_name="Лизинг")
    fully_serviced = models.BooleanField(
        default=False, verbose_name="Напълно обслужена"
    )
    central_locking = models.BooleanField(
        default=False, verbose_name="Централно заключване"
    )
    velour_interior = models.BooleanField(default=False, verbose_name="Велурен салон")
    el_mirrors = models.BooleanField(default=False, verbose_name="Ел. Огледала")
    el_windows = models.BooleanField(default=False, verbose_name="Ел. Стъкла")
    el_seats = models.BooleanField(
        default=False, verbose_name="Ел. регулиране на седалките"
    )
    el_wheel = models.BooleanField(default=False, verbose_name="Отопление на волана")
    el_front_screen = models.BooleanField(
        default=False, verbose_name="Подгрев на предното стъкло"
    )
    LED_headlights = models.BooleanField(default=False, verbose_name="LED фарове")
    alloy_wheels = models.BooleanField(default=False, verbose_name="Лети джанти")
    spoiler = models.BooleanField(default=False, verbose_name="Спойлер")
    auto_start_stop_function = models.BooleanField(
        default=False, verbose_name="Auto Start-Stop функция"
    )
    bluetooth = models.BooleanField(default=False, verbose_name="Bluetooth")
    steptronic_tiptronic = models.BooleanField(
        default=False, verbose_name="Steptronic/Tiptronic"
    )
    USB = models.BooleanField(default=False)
    keyless = models.BooleanField(default=False, verbose_name="Безключово палене")
    differential_lock = models.BooleanField(
        default=False, verbose_name="Блокаж на диференциала"
    )
    air_conditioning = models.BooleanField(default=False, verbose_name="Климатик")
    climate_control = models.BooleanField(default=False, verbose_name="Климатроник")
    board_cpu = models.BooleanField(default=False, verbose_name="Бордкомпютър")
    multi_wheel = models.BooleanField(
        default=False, verbose_name="Мултифункционален волан"
    )
    navigation = models.BooleanField(default=False, verbose_name="Навигация")
    four_by_four = models.BooleanField(default=False, verbose_name="4x4")
    seats_7 = models.BooleanField(default=False, verbose_name="7 местна")
    alarm = models.BooleanField(default=False, verbose_name="Аларма")
    paid_casco = models.BooleanField(default=False, verbose_name="Платено каско")
    paid_tax = models.BooleanField(default=False, verbose_name="Платен данък")

    def get_extras_fields(self):
        extras_fields = []
        for field in self._meta.fields:
            if isinstance(field, models.BooleanField):
                extras_fields.append(field.name)
        return extras_fields

    def __str__(self):
        return f"{self.brand} {self.model} - {self.info}"
