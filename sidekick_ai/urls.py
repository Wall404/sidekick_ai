from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/intent/', include('intent.urls')),  # URLs del módulo de intención
    path('api/recommendation/', include('recommendation.urls')),  # URLs del módulo de recomendación
]