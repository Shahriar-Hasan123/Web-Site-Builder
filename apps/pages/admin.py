from django.contrib import admin
from .models import Page

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ("title", "site", "slug", "status", "is_homepage", "order")
    list_filter = ("status", "is_homepage", "site")
    search_fields = ("title", "slug")
    prepopulated_fields = {"slug": ("title",)}