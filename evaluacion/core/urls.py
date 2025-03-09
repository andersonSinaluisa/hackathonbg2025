from django.urls import path
from .views.calculate_score import CalculateScore


urlpatterns = [
    path('calculate-score', CalculateScore.as_view()),
]