# Django
from django.urls import path

# local Django
from .views import SubscriptionRedirectView, SubscriptionListView

app_name = "subscriptions"

urlpatterns = [
    path("subscribe/", SubscriptionRedirectView.as_view(), name="subscribe"),
    path("<int:pk>/", SubscriptionListView.as_view(), name="list"),
]
