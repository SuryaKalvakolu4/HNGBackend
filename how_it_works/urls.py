from django.urls import path
from .views import HowItWorksView, FAQView


app_name = "how_it_works"


urlpatterns = [
    path("", HowItWorksView.as_view(), name="how-it-works"),
    path("faq/", FAQView.as_view(), name="faq"),
]
