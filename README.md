🛡️ Security Event & Alert Backend (Django)

📌 Features
  - JWT-based authentication
  - Role-based access (Admin / Analyst)
  - Event ingestion API
  - Automatic alert generation
  - Alert listing & filtering
  - Alert status update (Admin only)
  - Pagination & optimized queries
  - SQLite database (Postgres-ready)


📌 Tech Stack
  - Python 3.12 → Core language, async support, fast development
  - Django → Web framework, ORM, security, admin panel
  - Django REST Framework (DRF) → Build APIs, serialization, authentication, throttling
  - SimpleJWT → JWT-based stateless authentication for APIs
  - SQLite → Lightweight, zero-config database for development
  - Swagger (drf-yasg) → Auto-generate API docs and testing
  - Throttling → Rate limiting to prevent abuse / brute-force
  - Channels → Async support, WebSockets, real-time communication
  - Daphne → ASGI server to run Django with WebSockets support


📌 Project Structure
security_backend/
│
├── core/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── permissions.py
│   ├── urls.py
|   ├── consumers.py
|   ├── routing.py
│
├── security_backend/
│   ├── settings.py
│   ├── urls.py
│
├── manage.py
├── README.md


⚙️ Setup Instructions (From Scratch)
  - sudo apt install python3-full python3-venv
  - python3 -m venv venv
  - source venv/bin/activate
  - pip install -r requirements.txt
  - python manage.py migrate
  - python manage.py runserver


👤 User Roles Setup
  - python manage.py createsuperuser
  - http://127.0.0.1:8000/admin/
  - Create user
  - Assign password
  - Assign group:
    - Admin
    - Analyst


📍 Endpoints
  🔐 Auth
    - POST http://127.0.0.1:8000/api/token/
    - POST http://127.0.0.1:8000/api/token/refresh/

  🚨 Core APIs
  - POST http://127.0.0.1:8000/api/events/
  - GET http://127.0.0.1:8000/api/alerts/
  - PATCH http://127.0.0.1:8000/api/alerts/<id>/

📘 Docs
  - Swagger → http://127.0.0.1:8000/swagger/
  - ReDoc → http://127.0.0.1:8000/redoc/