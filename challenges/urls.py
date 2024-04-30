from django.urls import path
from .views import ChallengeListView, ChallengeDetailView


app_name = "challenges"

urlpatterns = [
    path("list/", ChallengeListView.as_view(), name="list"),
    path("detail/<day>/", ChallengeDetailView.as_view(), name="detail"),
]
