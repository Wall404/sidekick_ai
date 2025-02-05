# Sidekick AI - Intent and Recommendation Modules

## Installation
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`.
3. Run migrations: `python manage.py migrate`.
4. Start the server: `python manage.py runserver`.

## Endpoints
- **Intent Module**: `POST /api/intent/`
  - Input: `{"user_input": "My skin feels dry"}`
  - Output: `{"intent": "Skin dryness intent"}`

- **Recommendation Module**: `POST /api/recommendation/`
  - Input: No data needs to be sent (uses the latest saved intent).
  - Output: `{"advice": "Use a moisturizer with hyaluronic acid."}`