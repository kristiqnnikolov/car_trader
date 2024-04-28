# user_profile forms.py
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
from .models import CustomUser

UserModel = get_user_model()


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Потребителско име"}),
    )
    password = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={"placeholder": "Парола"}),
    )
    error_messages = {
        "invalid_login": ("Грешно потребителско име или парола!"),
    }


# <------- REGISTRATION FORM ------>
class RegistrationForm(UserCreationForm):
    MIN_LENGTH_VALIDATOR = 3
    username = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Потребителско име"}),
        label="",
        help_text="",
        validators=[
            MinLengthValidator(
                MIN_LENGTH_VALIDATOR,
                message=_("Потребителското име трябва да е с дължина над 3 символа."),
            )
        ],
    )

    email = forms.EmailField(
        widget=forms.TextInput(attrs={"placeholder": "Имейл"}),
        label="",
        help_text="",
        error_messages={"invalid": _("Невалиден имейл адрес.")},
    )
    phone_number = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": _("Телефонен номер"), "maxlength": "10"}
        ),
        label="",
        help_text="",
        validators=[
            MaxLengthValidator(
                10,
                message=_("Телефонният номер трябва да бъде с дължина до 10 символа."),
            )
        ],
    )
    password1 = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={"placeholder": "Парола"}),
        help_text="Паролата трябва да съдържа число и специален символ, общо минимум 8 символа",
    )

    password2 = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={"placeholder": "Потвърди парола"}),
    )

    error_messages = {
        "password_mismatch": _("Паролите не съвпадат"),
    }

    class Meta:
        model = UserModel
        fields = ("email", "phone_number", "username")
        field_classes = {"username": UsernameField}


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())