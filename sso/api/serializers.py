import logging
import re

from rest_framework import serializers

from sso.models import User

logger = logging.getLogger(__name__)


class UserBaseSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True
    )

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'date_joined', 'avatar', 'date_of_birth', 'password']


class UserSignUpSerializer(UserBaseSerializer):
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def validate_password(self, value):
        reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,120}$"
        pat = re.compile(reg)
        mat = re.search(pat, value)
        if not mat:
            raise serializers.ValidationError("Weak password")
        return value
