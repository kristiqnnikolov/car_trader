# user_profile urls.py
from django.urls import path
from .views import (
    RegistrationView,
    IndexView,
    CustomLoginView,
    CustomLogoutView,
    ProfileView,
    ProfileEditView,
    SearchView,
)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("register/", RegistrationView.as_view(), name="register"),
    path("search/", SearchView.as_view(), name="search"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    path("profile/edit/", ProfileEditView.as_view(), name="profile-edit"),
    path("profile/<slug:user_slug>/", ProfileView.as_view(), name="profile"),
]
