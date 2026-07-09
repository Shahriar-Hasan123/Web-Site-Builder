from rest_framework import serializers
from .models import Header


class HeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Header
        fields = ["id", "site", "content", "created_at", "updated_at"]
        read_only_fields = ["id", "site", "created_at", "updated_at"]