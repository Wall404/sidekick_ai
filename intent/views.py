from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Intent


def home(request):
    return HttpResponse("Welcome to Sidekick AI!")


class IntentView(APIView):
    def post(self, request):
        user_input = request.data.get('user_input')

        # Validate that user_input is present
        if not user_input:
            return Response({"error": "user_input is required"}, status=status.HTTP_400_BAD_REQUEST)

        # Simplified AI logic to detect intent
        if "dryness" in user_input.lower():
            intent_type = "Skin dryness intent"
        else:
            intent_type = "Unknown intent"

        # Save the intent to the database
        intent = Intent.objects.create(user_input=user_input, intent_type=intent_type)

        return Response({"intent": intent_type}, status=status.HTTP_201_CREATED)