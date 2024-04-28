# ads forms.py
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UsernameField, get_user_model
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from .models import Ad

UserModel = get_user_model()

class AdForm(forms.ModelForm):

    class Meta:
        model = Ad
        fields = "__all__"

    def get_extras_fields(self):
        extras_fields = []
        for field in self._meta.fields:
            if isinstance(field, models.BooleanField):
                extras_fields.append(field.name)
        return extras_fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["brand"].error_messages = {"required": "Изберете бранд!"}
        self.fields["model"].error_messages = {"required": "Изберете модел!"}
        self.fields["engine"].error_messages = {
            "required": 'Полето "Двигател" е задължително!'
        }
        self.fields["price"].error_messages = {
            "required": 'Полето "Цена" е задължително!'
        }
        self.fields["mileage"].error_messages = {
            "required": 'Полето "Пробег" е задължително!'
        }
        self.fields["eurostandard"].error_messages = {
            "required": 'Полето "Евростандарт" е задължително!'
        }
        self.fields["gearbox"].error_messages = {
            "required": 'Полето "Скоростна кутия" е задължително!'
        }
        self.fields["coupe_type"].error_messages = {
            "required": 'Полето "Тип купе" е задължително!'
        }
        self.fields["currency"].error_messages = {
            "required": 'Полето "Валута" е задължително!'
        }
        self.fields["wheel"].error_messages = {
            "required": 'Полето "Волан" е задължително!'
        }
        self.fields["doors"].error_messages = {
            "required": 'Полето "Врати" е задължително!'
        }
        self.fields["month_of_production"].error_messages = {"required": ""}
        self.fields["year_of_production"].error_messages = {
            "required": 'Полетата "Месец и година на производство" са задължителни!'
        }
        self.fields["color"].error_messages = {
            "required": 'Полето "Цвят" е задължително!'
        }
        self.fields["region"].error_messages = {
            "required": 'Полето "Регион" е задължително!'
        }


class AdEditForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = [
            "brand",
            "model",
            "info",
            "mileage",
            "price",
            "currency",
            "engine",
            "coupe_type",
            "eurostandard",
            "wheel",
            "gearbox",
            "doors",
            "color",
            "month_of_production",
            "year_of_production",
            "region",
            "ABS",
            "airbags",
            "traction_control",
            "adaptive_lights",
            "parking_sensor",
            "isofix",
            "GPS",
            "descent_control",
            "gas_as_fuel",
            "metan_as_fuel",
            "leasing",
            "fully_serviced",
            "central_locking",
            "velour_interior",
            "el_mirrors",
            "el_windows",
            "el_seats",
            "el_wheel",
            "el_front_screen",
            "LED_headlights",
            "alloy_wheels",
            "spoiler",
            "description",
            "auto_start_stop_function",
            "bluetooth",
            "steptronic_tiptronic",
            "USB",
            "keyless",
            "differential_lock",
            "air_conditioning",
            "climate_control",
            "board_cpu",
            "multi_wheel",
            "navigation",
            "four_by_four",
            "seats_7",
            "alarm",
            "paid_casco",
            "paid_tax",
            "image",
        ]
