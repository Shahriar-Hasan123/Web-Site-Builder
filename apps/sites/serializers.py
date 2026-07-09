from rest_framework import serializers
from .models import Site


class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = ["id", "owner", "name", "subdomain", "is_published", "created_at", "updated_at"]
        read_only_fields = ["id", "owner", "subdomain", "created_at", "updated_at"]
