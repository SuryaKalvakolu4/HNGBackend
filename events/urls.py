from django.urls import path
from .views import EventSignUpView, EventListView, EventDetailView, EventsByDateView


app_name = "events"


urlpatterns = [
    path("sign-up/<int:pk>/", EventSignUpView.as_view(), name="sign-up"),
    path("list/", EventListView.as_view(), name="list"),
    path("detail/<int:pk>/", EventDetailView.as_view(), name="detail"),
    path("events-by-date/<date>/", EventsByDateView.as_view(), name="events-by-date"),
]
