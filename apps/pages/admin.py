from django.contrib import admin
from .models import Page


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ("title", "site", "slug", "status", "page_type", "enable", "created_by")
    list_filter = ("status", "page_type", "enable", "site")
    search_fields = ("title", "slug")
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ("created_by", "updated_by", "created_at", "updated_at")

    def save_model(self, request, obj, form, change):
        """Automatically set created_by and updated_by fields"""
        obj.save(user=request.user)