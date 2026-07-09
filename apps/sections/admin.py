from django.contrib import admin
from .models import Section


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ("page", "block_type", "order", "updated_at")
    list_filter = ("block_type", "page__site")
    ordering = ("page", "order")