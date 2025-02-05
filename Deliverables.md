Deliverables Document
A. Design Document
1. App Boundaries

    Intent Module (intent):

        Processes user input and detects the intent.

        Contains the Intent model and the POST /api/intent/ endpoint.

    Recommendation Module (recommendation):

        Generates recommendations based on the user's intent.

        Contains the Recommendation model and the POST /api/recommendation/ endpoint.

    Clear Separation:

        Each module is an independent Django app.

        This allows for modular development and easier scalability.

2. Data Flow

    The user sends input (text or image) to the POST /api/intent/ endpoint.

    The intent module processes the input, detects the intent, and saves it to the database.

    The user (or system) calls the POST /api/recommendation/ endpoint.

    The recommendation module retrieves the latest intent from the database and generates a recommendation based on it.

    The recommendation is returned to the user and saved in the database.

3. Reasoning

    Folder Structure:

        Each module is an independent Django app (intent and recommendation).

        This follows Django best practices, which recommend separating logic into modular apps.

    Use of Django REST Framework (DRF):

        DRF simplifies the creation of RESTful APIs with Django.

        Provides tools for serialization, authentication, and error handling.

    PostgreSQL Database:

        PostgreSQL is a robust and scalable database, ideal for production environments.

        If SQLite is used in development, transitioning to PostgreSQL in production is straightforward.

4. Scalability & Extensibility

    Scalability:

        Use of a task queue (e.g., Celery) to handle asynchronous tasks.

        Migration to a PostgreSQL cluster to handle large volumes of data.

    Extensibility:

        Adding new modules is simple: just create a new Django app and define its models and endpoints.

        Existing modules are not affected by the addition of new ones.

5. Scaling Question (Optional)

If you had to handle 100,000 daily active users, what key changes would you make?

    Key Changes:

        Load Balancing: Use a load balancer (e.g., Nginx) to distribute traffic across multiple application instances.

        Caching: Implement a caching system (e.g., Redis) to store frequent responses and reduce database load.

        Distributed Database: Use a PostgreSQL cluster with replication and partitioning to handle large data volumes.

        Monitoring: Implement monitoring tools (e.g., Prometheus and Grafana) to track system performance.

