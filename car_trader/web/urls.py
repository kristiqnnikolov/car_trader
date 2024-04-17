# urls.py
from django.urls import path
from .views import (
    RegistrationView,
    IndexView,
    CustomLoginView,
    CustomLogoutView,
    ProfileView,
    ProfileEditView,
    AdCreateView,
    EditAdView,
    SearchView,
    ViewAd,
)
from .views import error_404_view

handler404 = 'car_trader.web.views.error_404_view'

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("register/", RegistrationView.as_view(), name="register"),
    path("search/", SearchView.as_view(), name="search"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    path("profile/edit/", ProfileEditView.as_view(), name="profile-edit"),
    path("profile/<slug:user_slug>/", ProfileView.as_view(), name="profile"),
    path("profile/<slug:user_slug>/add-ad/", AdCreateView.as_view(), name="add-ad"),
    path("edit-ad/<int:pk>/", EditAdView.as_view(), name="edit-ad"),
    path("ad/<int:pk>/", ViewAd.as_view(), name="ad"),
]
