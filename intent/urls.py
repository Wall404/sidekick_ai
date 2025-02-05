from django.urls import path
from .views import IntentView

urlpatterns = [
    path('intent/', IntentView.as_view(), name='intent'),
]