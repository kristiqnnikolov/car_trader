from django.contrib import admin
from .models import Ad

class AdAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'price', 'description', 'user')
    list_filter = ('brand', 'model', 'price', 'user')
    search_fields = ('brand', 'model', 'description', 'user__username')
    ordering = ('-price',)
    # Add more customizations as needed

admin.site.register(Ad, AdAdmin)
