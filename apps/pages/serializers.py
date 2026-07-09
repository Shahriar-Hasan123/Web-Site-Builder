from rest_framework import serializers
from .models import Page
from sections.serializers import SectionSerializer

class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ["id", "site", "title", "slug", "is_homepage","status", "seo_meta", "order", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]

    def validate(self, data):
        slug = data.get("slug")
        site_id = self.get_site_id(data)

        if slug and site_id and self.slug_exists_for_site(slug, site_id):
            raise serializers.ValidationError(
                {"slug": "This slug is already used for this site."}
            )

        return data

    def validate_seo_meta(self, value):
        return value or {}

    def get_site_id(self, data):
        site = data.get("site")
        if site:
            return site.id

        view = self.context.get("view")
        if view:
            return view.kwargs.get("site_pk")

        if self.instance:
            return self.instance.site_id

        return None

    def slug_exists_for_site(self, slug, site_id):
        pages = Page.objects.filter(site_id=site_id, slug=slug)

        if self.instance:
            pages = pages.exclude(pk=self.instance.pk)

        return pages.exists()


class PageDetailSerializer(PageSerializer):
    """
    URL: /api/sites/{site_pk}/pages/
    """
    sections = SectionSerializer(many=True, read_only=True)

    class Meta(PageSerializer.Meta):
        fields = PageSerializer.Meta.fields + ["sections"]
