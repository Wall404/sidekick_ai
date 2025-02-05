from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from intent.models import Intent
from .models import Recommendation

class RecommendationView(APIView):
    def post(self, request):
        # Obtener la última intención del usuario desde la base de datos
        last_intent = Intent.objects.last()  # Obtiene la última intención guardada

        if not last_intent:
            return Response({"error": "No intent found"}, status=status.HTTP_400_BAD_REQUEST)

        # Lógica de IA simplificada para generar recomendaciones
        if last_intent.intent_type == "Skin dryness intent":
            advice = "Use a moisturizer with hyaluronic acid."
        else:
            advice = "No specific recommendation available."

        # Guardar la recomendación en la base de datos
        recommendation = Recommendation.objects.create(intent=last_intent.intent_type, advice=advice)

        return Response({"advice": advice}, status=status.HTTP_201_CREATED)