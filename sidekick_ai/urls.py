from django.contrib import admin
from django.urls import path, include
from intent.views import home  # Importa la vista

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/intent/', include('intent.urls')),
    path('api/recommendation/', include('recommendation.urls')),
    path('', home, name='home'),  # Ruta raíz
]