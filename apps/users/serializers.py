from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from .models import AuthUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=AuthUser
        fields = ["id", "username", "email", "password"]

        extra_kwarg = {
            "first_name": {"write_only": True},
            "last_name": {"write_only": True},
            "password": {"write_only": True},
            "is_active": {"default": True},
        }

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data['password'])
        return super().update(instance, validated_data)