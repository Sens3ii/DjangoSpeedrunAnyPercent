from rest_framework import serializers

from api.models import Category


class CategoryBaseSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'icon', 'description', 'created_at', 'updated_at']
