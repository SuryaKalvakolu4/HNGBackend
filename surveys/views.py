from django.db.models import Sum

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Survey
from prizes.models import Medal
from .serializers import SurveySerializer


class SurveyCreateView(generics.CreateAPIView):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={"user": request.user})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=201)

    def perform_create(self, serializer):
        serializer.save()
        user = self.request.user
        total_completed_number = Survey.objects.filter(user=user).aggregate(
            total = Sum("number_of_completed")
        )["total"]
        # here we identify which medal the user get
        # first we find total_completed_number
        # (how many challenges the user completed after submiting the survey form)
        # then granting the user with a medal he/she deserves according to the total_completed_number
        if total_completed_number >= 37:
            user.medals.add(Medal.objects.get(name="Bronze"))
        if total_completed_number >= 47:
            user.medals.add(Medal.objects.get(name="Silver"))
        if total_completed_number >= 57:
            user.medals.add(Medal.objects.get(name="Gold"))
        user.save()
        return super().perform_create(serializer)
