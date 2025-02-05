from django.test import TestCase, Client
from django.urls import reverse
from intent.models import Intent
from recommendation.models import Recommendation

class RecommendationTests(TestCase):
    def test_recommendation_endpoint(self):
        # Crear una intención en la base de datos
        Intent.objects.create(user_input="My skin feels dry", intent_type="Skin dryness intent")

        client = Client()
        response = client.post(
            reverse('recommendation'),
            {},  # No se necesita enviar datos, ya que se usa la última intención
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 201)
        self.assertIn('advice', response.json())

        # Verificar que la recomendación se guardó en la base de datos
        recommendation = Recommendation.objects.last()
        self.assertEqual(recommendation.advice, "Use a moisturizer with hyaluronic acid.")