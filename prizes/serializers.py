from rest_framework import serializers
from .models import DailyPrize, Medal, Badge


class DailyPrizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyPrize
        fields = "__all__"


class MedalSerializer(serializers.ModelSerializer):
    progression_rate = serializers.FloatField()

    class Meta:
        model = Medal
        exclude = ["id"]


class BadgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Badge
        fields = "__all__"
