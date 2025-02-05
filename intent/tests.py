from django.test import TestCase, Client
from django.urls import reverse
from intent.models import Intent

class IntentTests(TestCase):
    def test_intent_endpoint(self):
        client = Client()
        response = client.post(
            reverse('intent'),
            {'user_input': 'My skin feels dry'},
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 201)
        self.assertIn('intent', response.json())

        # Verificar que la intención se guardó en la base de datos
        intent = Intent.objects.last()
        self.assertEqual(intent.intent_type, "Skin dryness intent")