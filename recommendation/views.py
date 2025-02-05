from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Recommendation

class RecommendationView(APIView):
    def post(self, request):
        intent = request.data.get('intent')
        user_data = request.data.get('user_data', {})  # Datos adicionales del usuario

        # Lógica de IA simplificada para generar recomendaciones
        if intent == "Skin dryness intent":
            advice = "Use a moisturizer with hyaluronic acid."
        else:
            advice = "No specific recommendation available."

        # Guardar la recomendación en la base de datos
        recommendation = Recommendation.objects.create(intent=intent, advice=advice)

        return Response({"advice": advice}, status=status.HTTP_201_CREATED)