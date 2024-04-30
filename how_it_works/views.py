from .models import GetStarted, PhysicalHIW, MentalHIW, SocialHIW, PrizesHIW, BadgesHIW, FAQ
from .serializers import *
from rest_framework.exceptions import NotFound
from rest_framework import generics
from rest_framework.response import Response
from django.forms.models import model_to_dict
from django.utils.translation import gettext as _


class HowItWorksView(generics.GenericAPIView):
    serializer_class = HowItWorksSerializer

    def get(self, request):
        data = []
        hiw_model_list = [GetStarted, PhysicalHIW, MentalHIW, SocialHIW, PrizesHIW, BadgesHIW]
        hiw_serializer_list = [GetStartedSerializer, PhysicalHIWSerializer, MentalHIWSerializer, SocialHIWSerializer, PrizesHIWSerializer, BadgesHIWSerializer]
        for hiw_model, hiw_serializer in zip(hiw_model_list, hiw_serializer_list):
            hiw_model_all = hiw_model.objects.all()
            if hiw_model_all.exists():
                data.append(hiw_serializer(hiw_model_all.last()).data)

        return Response(data)


class FAQView(generics.ListAPIView):
    queryset = FAQ.objects.all().order_by("-id")
    serializer_class = FAQSerializer
