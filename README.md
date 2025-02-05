# Sidekick AI - Módulos de Intención y Recomendación

## Instalación
1. Clona el repositorio.
2. Instala las dependencias: `pip install -r requirements.txt`.
3. Ejecuta las migraciones: `python manage.py migrate`.
4. Inicia el servidor: `python manage.py runserver`.

## Endpoints
- **Módulo de Intención**:
  - `POST /api/intent/`: Procesa la entrada del usuario y devuelve la intención detectada.
- **Módulo de Recomendación**:
  - `POST /api/recommendation/`: Genera una recomendación basada en la intención del usuario.