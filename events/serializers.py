from rest_framework import serializers
from .models import Event
from challenges.serializers import InstructorSerializer


class EventSerializer(serializers.ModelSerializer):
    instructor = InstructorSerializer(many=True)

    class Meta:
        model = Event
        fields = "__all__"
