from .models import Section
from rest_framework import serializers

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Section
        fields = ["id", "page", "block_type", "content", "settings", "order", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]