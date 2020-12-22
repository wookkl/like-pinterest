# Django
from django.urls import path

# local Django
from .views import SubscriptionRedirectView

app_name = "subscriptions"

urlpatterns = [
    path("subscribe/", SubscriptionRedirectView.as_view(), name="subscribe"),
]
