from django.core import serializers
from rest_framework import serializers

from api.models import Category, Item, Image, Review
from sso.models import User
from utils.validators import validate_extension


class CategoryBaseSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'icon', 'description', 'created_at', 'updated_at']


class CategoryNestedBaseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()


class CategoryNestedSerializer(CategoryNestedBaseSerializer):
    icon = serializers.CharField()
    description = serializers.CharField()


class ImageNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('image',)


class ItemBaseSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    price = serializers.FloatField()
    name = serializers.CharField(max_length=64)
    short_description = serializers.CharField(max_length=128)
    full_description = serializers.CharField(max_length=512)
    rating = serializers.FloatField(read_only=True)
    rating_count = serializers.IntegerField(read_only=True)
    category_id = serializers.IntegerField()
    images = ImageNestedSerializer(many=True, read_only=True)

    def validate_category_id(self, value):
        if value and not Category.objects.filter(id=value).exists():
            raise serializers.ValidationError("Such category does not exists")
        return value

    def validate_price(self, value):
        if value and value <= 0:
            raise serializers.ValidationError("Price should be above zero")
        return value

    def create(self, validated_data):
        images = self.context.get('view').request.FILES
        item = Item.objects.create(**validated_data)
        for image in images.values():
            try:
                validate_extension(image)
            except:
                raise serializers.ValidationError("Not allowed extension")
            Image.objects.create(item=item, image=image)
        return item

    def update(self, instance, validated_data):
        instance.price = validated_data.get('price', instance.price)
        instance.name = validated_data.get('name', instance.name)
        instance.short_description = validated_data.get('short_description', instance.short_description)
        instance.full_description = validated_data.get('full_description', instance.full_description)
        instance.category_id = validated_data.get('category_id', instance.category_id)
        instance.save()
        return instance


class ItemRetrieveResponseSerializer(ItemBaseSerializer):
    images = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    category = CategoryNestedSerializer()


class ItemListResponseSerializer(ItemBaseSerializer):
    images = serializers.StringRelatedField(many=True, read_only=True)
    category = CategoryNestedBaseSerializer()


class CommentBaseSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    content = serializers.CharField()
    item_id = serializers.IntegerField()
    user_id = serializers.IntegerField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    rating = serializers.IntegerField()

    def validate_item_id(self, value):
        if value and not Item.objects.filter(id=value).exists():
            raise serializers.ValidationError("Such item does not exists")
        return value

    def validate_rating(self, value):
        if value >= 0 and value <= 5:
            return value
        raise serializers.ValidationError("Rating should be [0-5]")

    def create(self, validated_data):
        user = self.context['request'].user
        if not user:
            raise serializers.ValidationError("Not authentificated")
        return Review.objects.create(user_id=user.id, **validated_data)

    def update(self, instance, validated_data):
        instance.content = validated_data.get('content', instance.content)
        instance.rating = validated_data.get('rating', instance.rating)
        instance.save()
        return instance


class CommentGetSerializer(CommentBaseSerializer):
    item = serializers.SlugRelatedField(read_only=True, slug_field='name')
    user = serializers.SlugRelatedField(read_only=True, slug_field='email')


class CommentUpdateSerializer(CommentBaseSerializer):
    item_id = serializers.IntegerField(read_only=True)
