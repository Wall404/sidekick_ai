from django.urls import path
from .views import RecommendationView

urlpatterns = [
    path('recommendation/', RecommendationView.as_view(), name='recommendation'),
]