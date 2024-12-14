from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data: dict) -> User:
        return get_user_model().objects.create_user(**validated_data)
