from rest_framework import serializers

from sso.models import User


class UserBaseSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'date_joined', 'avatar', 'date_of_birth', 'password']


class UserSignUpSerializer(UserBaseSerializer):
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
