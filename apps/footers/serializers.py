from rest_framework import serializers
from .models import Footer


class FooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Footer
        fields = ["id", "site", "content", "created_at", "updated_at"]
        read_only_fields = ["id", "site", "created_at", "updated_at"]