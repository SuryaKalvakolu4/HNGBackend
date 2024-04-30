from rest_framework import serializers
from .models import GetStarted, PhysicalHIW, MentalHIW, SocialHIW, PrizesHIW, BadgesHIW, FAQ


class GetStartedSerializer(serializers.ModelSerializer):
    name = serializers.CharField(default="get_started_hiw")
    class Meta:
        model = GetStarted
        exclude = ['id']


class PhysicalHIWSerializer(serializers.ModelSerializer):
    name = serializers.CharField(default="physical_hiw")
    class Meta:
        model = PhysicalHIW
        exclude = ['id']


class MentalHIWSerializer(serializers.ModelSerializer):
    name = serializers.CharField(default="mental_hiw")
    class Meta:
        model = MentalHIW
        exclude = ['id']


class SocialHIWSerializer(serializers.ModelSerializer):
    name = serializers.CharField(default="social_hiw")
    class Meta:
        model = SocialHIW
        exclude = ['id']


class PrizesHIWSerializer(serializers.ModelSerializer):
    name = serializers.CharField(default="prizes_hiw")
    class Meta:
        model = PrizesHIW
        exclude = ['id']


class BadgesHIWSerializer(serializers.ModelSerializer):
    name = serializers.CharField(default="badge_hiw")
    class Meta:
        model = BadgesHIW
        exclude = ['id']


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = "__all__"


class HowItWorksSerializer(serializers.Serializer):
    get_started = GetStartedSerializer(required=False)
    physical_hiw = PhysicalHIWSerializer(required=False)
    mental_hiw = MentalHIWSerializer(required=False)
    social_hiw = SocialHIWSerializer(required=False)
    prizes_hiw = PhysicalHIWSerializer(required=False)
    badges_hiw = BadgesHIWSerializer(required=False)
