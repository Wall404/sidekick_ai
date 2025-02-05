from django.db import models

class Intent(models.Model):
    user_input = models.TextField()  # Entrada del usuario (texto o descripción)
    intent_type = models.CharField(max_length=100)  # Tipo de intención detectada
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.intent_type}: {self.user_input}"