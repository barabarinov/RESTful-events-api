from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Event


class EventSerializer(serializers.ModelSerializer):
    guests = serializers.PrimaryKeyRelatedField(
        many=True, queryset=get_user_model().objects.all(), required=False
    )

    class Meta:
        model = Event
        fields = "__all__"
        read_only_fields = ("organizer",)
