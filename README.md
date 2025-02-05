# Sidekick AI - Módulos de Intención y Recomendación

## Instalación
1. Clona el repositorio.
2. Instala las dependencias: `pip install -r requirements.txt`.
3. Ejecuta las migraciones: `python manage.py migrate`.
4. Inicia el servidor: `python manage.py runserver`.

## Endpoints
- **Módulo de Intención**: `POST /api/intent/`
  - Entrada: `{"user_input": "My skin feels dry"}`
  - Salida: `{"intent": "Skin dryness intent"}`

- **Módulo de Recomendación**: `POST /api/recommendation/`
  - Entrada: No se necesita enviar datos (usa la última intención guardada).
  - Salida: `{"advice": "Use a moisturizer with hyaluronic acid."}`