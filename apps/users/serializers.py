from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from .models import AuthUser


class UserSerializer(serializers.ModelSerializer):
    qtd_seguindo = serializers.SerializerMethodField()
    qtd_seguidores = serializers.SerializerMethodField()
    qtd_publicacao = serializers.SerializerMethodField()

    class Meta:
        model = AuthUser
        fields = [
            "id",
            "username",
            "email",
            "password",
            "first_name",
            "last_name",
            "ds_bio",
            "role",
            "img_profile",
            "img_background",
            "qtd_seguindo",
            "qtd_seguidores",
            "qtd_publicacao",
        ]

        extra_kwargs = {
            "password": {"write_only": True},
            "email": {"required": False},
            "first_name": {"required": False},
            "last_name": {"required": False},
            "ds_bio": {"required": False},
            "role": {"required": False},
            "img_profile": {"required": False},
            "img_background": {"required": False},
        }

    def get_qtd_seguindo(self, obj):
        return 0

    def get_qtd_seguidores(self, obj):
        return 0

    def get_qtd_publicacao(self, obj):
        return 0

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        user = super().create(validated_data)

        new_username = f"@{user.username}{user.id}"
        super().update(user, validated_data)

        user.username = new_username
        return user

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data['password'])
        return super().update(instance, validated_data)