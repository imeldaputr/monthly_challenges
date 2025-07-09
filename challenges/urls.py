from django.urls import path
from . import views

# Define the URL patterns for the challenges app, that we want to support
urlpatterns = [
    path("", views.index), # /challenges/
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge, name="month-challenge")  # Dynamic URL for monthly challenges, month as identifier
]

