from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from ..user_profile.models import CustomUser
from ..user_profile.views import (
    ProfileView,
    IndexView,
    ProfileEditView,
    RegistrationView,
)
from django.urls import reverse
from django.contrib.auth import get_user_model
from ..user_profile.forms import RegistrationForm, LoginForm
from .forms import AdForm, AdEditForm
from .models import Ad


class AdFormTest(TestCase):
    def test_ad_form_valid(self):
        form_data = {
            "brand": "BMW",
            "model": "X5",
            "info": "Test ad",
            "mileage": 50000,
            "price": 10000,
        }
        form = AdForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_ad_form_invalid(self):
        form_data = {
            "brand": "BMW",
            "model": "",
            "info": "Test ad",
            "mileage": 50000,
            "price": 10000,
        }
        form = AdForm(data=form_data)
        self.assertFalse(form.is_valid())


class AdEditFormTest(TestCase):
    def test_ad_edit_form_valid(self):
        ad = Ad.objects.create(
            brand="BMW", model="X5", info="Test ad", mileage=50000, price=10000
        )
        form_data = {
            "brand": "Audi",
            "model": "Q7",
            "info": "Updated ad",
        }
        form = AdEditForm(instance=ad, data=form_data)
        self.assertFalse(form.is_valid())

    def test_ad_edit_form_invalid(self):
        ad = Ad.objects.create(
            brand="BMW", model="X5", info="Test ad", mileage=50000, price=10000
        )
        form_data = {
            "brand": "",
            "model": "Q7",
            "info": "Updated ad",
            "mileage": 60000,
            "price": 15000,
        }
        form = AdEditForm(instance=ad, data=form_data)
        self.assertFalse(form.is_valid())


class AdModelTest(TestCase):
    def test_ad_creation(self):
        user = CustomUser.objects.create(username="testuser", email="test@example.com")
        ad = Ad.objects.create(
            user=user,
            brand="BMW",
            model="X5",
            info="Test ad",
            description="Test description",
            engine="Gasoline",
            price=10000,
            mileage=50000,
            eurostandard="Euro 5",
            gearbox="Automatic",
            coupe_type="SUV",
            currency="EUR",
            wheel="Left",
            doors="5",
            month_of_production="January",
            year_of_production="2022",
            color="Black",
            region="Sofia",
        )
        self.assertEqual(ad.brand, "BMW")
        self.assertEqual(ad.model, "X5")
        self.assertEqual(ad.info, "Test ad")
        self.assertEqual(ad.description, "Test description")
        self.assertEqual(ad.engine, "Gasoline")
        self.assertEqual(ad.price, 10000)
        self.assertEqual(ad.mileage, 50000)
        self.assertEqual(ad.eurostandard, "Euro 5")
        self.assertEqual(ad.gearbox, "Automatic")
        self.assertEqual(ad.coupe_type, "SUV")
        self.assertEqual(ad.currency, "EUR")
        self.assertEqual(ad.wheel, "Left")
        self.assertEqual(ad.doors, "5")
        self.assertEqual(ad.month_of_production, "January")
        self.assertEqual(ad.year_of_production, "2022")
        self.assertEqual(ad.color, "Black")
        self.assertEqual(ad.region, "Sofia")
