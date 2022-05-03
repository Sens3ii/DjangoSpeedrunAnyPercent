import traceback

from rest_framework import serializers
from rest_framework.serializers import raise_errors_on_nested_writes
from rest_framework.utils import model_meta

from api.models import Category, Item


class CategoryBaseSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'icon', 'description', 'created_at', 'updated_at']


class CategorySerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField()

    class Meta:
        model = Category
        fields = ('id',)


class ItemBaseSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    price = serializers.FloatField()
    name = serializers.CharField()
    short_description = serializers.CharField()
    full_description = serializers.CharField()
    rating = serializers.FloatField(read_only=True)
    rating_count = serializers.IntegerField(read_only=True)
    category_id = serializers.IntegerField()

    def create(self, validated_data):
        return Item.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.price = validated_data.get('price', instance.price)
        instance.name = validated_data.get('name', instance.name)
        instance.short_description = validated_data.get('short_description', instance.short_description)
        instance.full_description = validated_data.get('full_description', instance.full_description)
        return instance


class ItemRetrieveResponseSerializer(ItemBaseSerializer):
    images = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    category = serializers.StringRelatedField()


class ItemListResponseSerializer(ItemBaseSerializer):
    images = serializers.StringRelatedField(many=True, read_only=True)
    category = serializers.StringRelatedField()