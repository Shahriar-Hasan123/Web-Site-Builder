from rest_framework import serializers
from .models import Page
from sections.serializers import SectionSerializer

class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ["id", "site", "title", "slug", "is_homepage","status", "seo_meta", "order", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]


class PageDetailSerializer(PageSerializer):
    sections = SectionSerializer(many=True, read_only=True)

    class Meta(PageSerializer.Meta):
        fields = PageSerializer.Meta.fields + ["sections"]
