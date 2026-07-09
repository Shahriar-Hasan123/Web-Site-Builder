from django.contrib import admin
from .models import Header


@admin.register(Header)
class HeaderAdmin(admin.ModelAdmin):
    list_display = ("site", "updated_at")