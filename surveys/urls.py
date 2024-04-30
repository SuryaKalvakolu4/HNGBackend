from django.urls import path
from .views import SurveyCreateView

app_name = "surveys"


urlpatterns = [
    path("create/", SurveyCreateView.as_view(), name="create"),
]
