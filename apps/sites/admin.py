from django.contrib import admin
from .models import Site


@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    list_display = ("name", "subdomain", "owner", "is_published", "created_at")
    list_filter = ("is_published",)
    search_fields = ("name", "subdomain")
    prepopulated_fields = {"subdomain": ("name",)}