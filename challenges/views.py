from .models import Challenge
from .serializers import ChallengeSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.response import Response
from django.utils.translation import gettext as _


class ChallengeListView(generics.ListAPIView):
    queryset = Challenge.objects.all().order_by('-id')
    serializer_class = ChallengeSerializer
    permission_classes = (IsAuthenticated,)


class ChallengeDetailView(generics.RetrieveAPIView):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "day"
