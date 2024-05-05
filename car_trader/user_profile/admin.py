from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    list_display = ("username", "email", "phone_number", "region")
    list_filter = ("region",)
    search_fields = ("username", "email", "phone_number", "region")
    ordering = ("username",)


admin.site.register(CustomUser, CustomUserAdmin)
