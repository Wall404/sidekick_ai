from django.db import models

class Recommendation(models.Model):
    intent = models.CharField(max_length=100)  # Intención del usuario
    advice = models.TextField()  # Recomendación generada
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.intent}: {self.advice}"