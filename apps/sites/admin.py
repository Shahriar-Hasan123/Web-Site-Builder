from django.contrib import admin
from .models import Site


@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "user", "status", "is_domain_verified", "created_at")
    list_filter = ("status", "is_domain_verified")
    search_fields = ("name", "slug", "domain")
    prepopulated_fields = {"slug": ("name",)}
    readonly_fields = ("user", "created_at", "updated_at")

    def save_model(self, request, obj, form, change):
        """Automatically set the user field to the current user"""
        if not change:  # Only on creation
            obj.user = request.user
        super().save_model(request, obj, form, change)