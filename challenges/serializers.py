from rest_framework import serializers
from .models import (Challenge, ModeratePhysicalChallenge, IntensePhysicalChallenge,
                     MentalChallenge, SocialChallenge, Instructor)


class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = "__all__"


class ModeratePhysicalChallengeSerializer(serializers.ModelSerializer):
    instructor = InstructorSerializer()
    class Meta:
        model = ModeratePhysicalChallenge
        fields = "__all__"


class IntensePhysicalChallengeSerializer(serializers.ModelSerializer):
    instructor = InstructorSerializer()
    class Meta:
        model = IntensePhysicalChallenge
        fields = "__all__"


class MentalChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MentalChallenge
        fields = "__all__"


class SocialChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialChallenge
        fields = "__all__"


class ChallengeSerializer(serializers.ModelSerializer):
    moderate_physical = ModeratePhysicalChallengeSerializer()
    intense_physical = IntensePhysicalChallengeSerializer()
    mental = MentalChallengeSerializer()
    social = SocialChallengeSerializer()

    class Meta:
        model = Challenge
        fields = "__all__"
