from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from .models import CustomUser, Ad
from .views import ProfileView, IndexView, ProfileEditView, RegistrationView
from django.urls import reverse
from django.contrib.auth import get_user_model
from .forms import RegistrationForm, LoginForm, AdForm, AdEditForm


UserModel = get_user_model()


# -------- view test ------------


class IndexViewTestCase(TestCase):
    def test_index_view(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)

    def test_index_view_context_latest_ads(self):
        response = self.client.get(reverse("index"))
        self.assertTrue("latest_ads" in response.context)


class ProfileViewTestCase(TestCase):
    def setUp(self):
        self.ad = Ad.objects.create(
            brand="Sample Brand", model="Sample Model", info="Sample Ad Information"
        )
        self.user = UserModel.objects.create_user(
            username="test_user", email="test@example.com", password="test_password"
        )
        self.client.force_login(self.user)

    def test_profile_view(self):
        response = self.client.get(
            reverse("profile", kwargs={"user_slug": self.user.slug})
        )
        self.assertEqual(response.status_code, 200)

    def test_profile_edit_view(self):
        response = self.client.get(reverse("profile-edit"))
        self.assertEqual(response.status_code, 200)

    def test_ad_create_view(self):
        response = self.client.get(
            reverse("add-ad", kwargs={"user_slug": self.user.slug})
        )
        self.assertEqual(response.status_code, 200)

    def test_ad_edit_view(self):
        ad = Ad.objects.create(user=self.user, brand="Test Brand", model="Test Model")
        response = self.client.get(reverse("edit-ad", kwargs={"pk": ad.pk}))
        self.assertEqual(response.status_code, 200)

    def test_registration_view(self):
        response = self.client.get(reverse("register"))
        self.assertEqual(response.status_code, 200)

    def test_logout_view(self):
        response = self.client.get(reverse("logout"))
        self.assertEqual(response.status_code, 405)

    def test_login_view(self):
        response = self.client.get(reverse("login"))
        self.assertEqual(response.status_code, 200)

    def test_search_view(self):
        response = self.client.get(reverse("search"))
        self.assertEqual(response.status_code, 200)

    def test_view_ad_view(self):
        response = self.client.get(reverse("ad", kwargs={"pk": self.ad.pk}))
        self.assertEqual(response.status_code, 200)


# -------- models tests ----------
class CustomUserModelTest(TestCase):
    def test_custom_user_creation(self):
        user = CustomUser.objects.create(username="testuser", email="test@example.com")
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "test@example.com")
        self.assertIsNotNone(user.slug)


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


# ----------- form tests -------------


class RegistrationFormTest(TestCase):
    def test_registration_form_valid(self):
        form_data = {
            "username": "test_user",
            "email": "test@example.com",
            "phone_number": "1234567890",
            "password1": "test_password123",
            "password2": "test_password123",
        }
        form = RegistrationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_registration_form_invalid(self):
        form_data = {
            "username": "test_user",
            "email": "invalid_email",  # Invalid email format
            "phone_number": "1234567890",
            "password1": "test_password123",
            "password2": "test_password123",
        }
        form = RegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())


class LoginFormTest(TestCase):
    def test_login_form_valid(self):
        form_data = {
            "username": "test_user",
            "password": "test_password123",
        }
        form = LoginForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_login_form_invalid(self):
        form_data = {
            "username": "test_user",
            "password": "",  # Empty password
        }
        form = LoginForm(data=form_data)
        self.assertFalse(form.is_valid())


class AdFormTest(TestCase):
    def test_ad_form_valid(self):
        form_data = {
            "brand": "BMW",
            "model": "X5",
            "info": "Test ad",
            "mileage": 50000,
            "price": 10000,
            # Missing other required fields...
        }
        form = AdForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_ad_form_invalid(self):
        form_data = {
            "brand": "BMW",
            "model": "",  # Empty model field
            "info": "Test ad",
            "mileage": 50000,
            "price": 10000,
            # Fill in other required fields...
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
            # Missing mileage and price, which are required fields
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
            # Fill in other required fields...
        }
        form = AdEditForm(instance=ad, data=form_data)
        self.assertFalse(form.is_valid())
