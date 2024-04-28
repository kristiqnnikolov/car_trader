# ads urls.py
from django.urls import path
from .views import (
    AdCreateView,
    EditAdView,
    ViewAd,
)

urlpatterns = (
    path("profile/<slug:user_slug>/add-ad/", AdCreateView.as_view(), name="add-ad"),
    path("edit-ad/<int:pk>/", EditAdView.as_view(), name="edit-ad"),
    path("ad/<int:pk>/", ViewAd.as_view(), name="ad"),
)
