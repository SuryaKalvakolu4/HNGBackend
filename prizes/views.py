from .models import DailyPrize, Medal, Badge
from .serializers import DailyPrizeSerializer, MedalSerializer, BadgeSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from django.utils.translation import gettext as _
from django.db.models import Value, Sum, Case, When, Q, FloatField
from django.db.models.functions import Coalesce
from surveys.models import Survey



class DailyPrizeListView(generics.ListAPIView):
    queryset = DailyPrize.objects.all().order_by('-id')
    serializer_class = DailyPrizeSerializer
    permission_classes = (IsAuthenticated,)


class MedalView(generics.ListAPIView):
    serializer_class = MedalSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        total_completed = Survey.objects.filter(user=self.request.user).aggregate(
            total = Coalesce(Sum("number_of_completed"), Value(0))
        )["total"]
        queryset = Medal.objects.annotate(total_completed_number=Value(total_completed)).annotate(
            progression_rate = Case(
                When(Q(name=Value("Bronze")) & Q(total_completed_number__lte=37), then=total_completed/37*100),
                When(Q(name=Value("Silver")) & Q(total_completed_number__lte=37), then=Value(0)),
                When(Q(name=Value("Gold")) & Q(total_completed_number__lte=47), then=Value(0)),
                When(Q(name=Value("Silver")) & Q(total_completed_number__lte=47), then=total_completed/47*100),
                When(Q(name=Value("Gold")) & Q(total_completed_number__lte=63), then=total_completed/63*100),
                default=Value(100),
                output_field=FloatField()
            )
        )
        return queryset


class BadgeView(generics.ListAPIView):
    queryset = Badge.objects.all()
    serializer_class = BadgeSerializer
    permission_classes = (IsAuthenticated,)
