from django.urls import path
from .views import IntentView

urlpatterns = [
    path('', IntentView.as_view(), name='intent'),
]