from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Intent

class IntentView(APIView):
    def post(self, request):
        user_input = request.data.get('user_input')

        # Lógica de IA simplificada para detectar la intención
        if "dryness" in user_input.lower():
            intent_type = "Skin dryness intent"
        else:
            intent_type = "Unknown intent"

        # Guardar la intención en la base de datos
        intent = Intent.objects.create(user_input=user_input, intent_type=intent_type)

        return Response({"intent": intent_type}, status=status.HTTP_201_CREATED)