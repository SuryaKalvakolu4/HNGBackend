from django.urls import path
from .views import DailyPrizeListView, MedalView, BadgeView


app_name = "prizes"

urlpatterns = [
    path("daily-prize-list/", DailyPrizeListView.as_view(), name="daily-prize-list"),
    path("medal-list/", MedalView.as_view(), name="medal-list"),
    path("badge-list/", BadgeView.as_view(), name="badge-list"),
]
