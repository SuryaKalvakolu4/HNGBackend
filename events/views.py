from django.contrib.auth import get_user_model

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Event
from .serializers import EventSerializer

User = get_user_model()


class EventSignUpView(generics.RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated, ]

    def get(self, request, *args, **kwargs):
        event = self.get_object()
        user = request.user
        user.events.add(event)
        user.save()
        return super().get(request, *args, **kwargs)


class EventListView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated, ]


class EventDetailView(generics.RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated, ]
    lookup_field = "pk"


class EventsByDateView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated, ]
    lookup_field = "date"

    def get_queryset(self):
        return Event.objects.filter(date=self.kwargs.get("date"))
