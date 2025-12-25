from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem
from reportlab.lib.units import cm 
from datetime import date

pdf_file = "Security_Backend_Project_Report.pdf"
doc = SimpleDocTemplate(pdf_file, pagesize=A4, rightMargin=2*cm, leftMargin=2*cm, topMargin=2*cm, bottomMargin=2*cm)


# Styles
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='MyHeading1', fontSize=18, leading=22, spaceAfter=12, spaceBefore=12))
styles.add(ParagraphStyle(name='MyHeading2', fontSize=14, leading=18, spaceAfter=8, spaceBefore=8))
styles.add(ParagraphStyle(name='MyNormal', fontSize=12, leading=16, spaceAfter=6))

heading1 = styles['MyHeading1']
heading2 = styles['MyHeading2']
normal = styles['MyNormal']

# Story
elements = []

# Cover Page
elements.append(Paragraph("Security Event & Alert Backend (Django)", heading1))
elements.append(Paragraph(f"Generated on: {date.today().strftime('%d-%m-%Y')}", normal))
elements.append(Paragraph("Author: Satendra Kumar", normal))
elements.append(Paragraph(" ", normal))  # Spacer

# Project Overview
overview = """
The Security Event & Alert Backend is a Django-based web application designed to efficiently manage security events 
and alerts. It provides secure and scalable REST APIs with JWT authentication, role-based access control, 
and real-time alert notifications using WebSockets. The system is optimized for fast querying, pagination, 
and can be easily switched from SQLite to Postgres for production environments.
"""
elements.append(Paragraph("Project Overview", heading2))
elements.append(Paragraph(overview, normal))

# Features
features_intro = "The backend system provides the following key features:"
features = [
    "JWT-based authentication for secure access",
    "Role-based access control (Admin / Analyst)",
    "Event ingestion API for recording security events",
    "Automatic alert generation based on events",
    "Alert listing and filtering with optimized queries",
    "Alert status update (Admin only)",
    "Pagination for large datasets",
    "SQLite database for development (Postgres-ready)"
]
elements.append(Paragraph("Features", heading2))
elements.append(Paragraph(features_intro, normal))
elements.append(ListFlowable([ListItem(Paragraph(f, normal)) for f in features]))

# Tech Stack
tech_intro = "The following technologies were used to build this backend system:"
tech_stack = [
    "Python 3.12 → Core programming language with async support for WebSockets and fast development",
    "Django → Web framework providing ORM, authentication, admin panel, and security features",
    "Django REST Framework (DRF) → For building REST APIs, serialization, authentication, and throttling",
    "SimpleJWT → JWT-based stateless authentication for APIs",
    "SQLite → Lightweight database for development; easily switchable to Postgres",
    "Swagger (drf-yasg) → Auto-generated API documentation and testing",
    "Throttling → Rate limiting to prevent abuse or brute-force attacks",
    "Channels → Async support for WebSockets and real-time communication",
    "Daphne → ASGI server to run Django with WebSockets support"
]
elements.append(Paragraph("Tech Stack", heading2))
elements.append(Paragraph(tech_intro, normal))
elements.append(ListFlowable([ListItem(Paragraph(t, normal)) for t in tech_stack]))

# Project Structure
structure_intro = "The project is organized as follows:"
structure_desc = """
security_backend/
│
├── core/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── permissions.py
│   ├── urls.py
│   ├── consumers.py
│   ├── routing.py
│
├── security_backend/
│   ├── settings.py
│   ├── urls.py
│
├── manage.py
├── README.md
"""
elements.append(Paragraph("Project Structure", heading2))
elements.append(Paragraph(structure_intro, normal))
elements.append(Paragraph(structure_desc, normal))

# Setup Instructions
setup_intro = "To set up the project locally from scratch, follow these instructions:"
setup_steps = [
    "Install Python 3 full version and venv module: sudo apt install python3-full python3-venv",
    "Create virtual environment: python3 -m venv venv",
    "Activate virtual environment: source venv/bin/activate",
    "Install required dependencies: pip install -r requirements.txt",
    "Run migrations: python manage.py migrate",
    "Start the development server: python manage.py runserver"
]
elements.append(Paragraph("Setup Instructions", heading2))
elements.append(Paragraph(setup_intro, normal))
elements.append(ListFlowable([ListItem(Paragraph(s, normal)) for s in setup_steps]))

# User Roles Setup
roles_intro = "To manage users and assign roles:"
roles_steps = [
    "Create superuser: python manage.py createsuperuser",
    "Access admin panel: http://127.0.0.1:8000/admin/",
    "Create users and assign password",
    "Assign user group: Admin or Analyst"
]
elements.append(Paragraph("User Roles Setup", heading2))
elements.append(Paragraph(roles_intro, normal))
elements.append(ListFlowable([ListItem(Paragraph(r, normal)) for r in roles_steps]))

# API Endpoints
endpoints_intro = "The backend provides the following API endpoints:"
endpoints = [
    "Auth:",
    "POST /api/token/ → Get JWT token",
    "POST /api/token/refresh/ → Refresh JWT token",
    "Core APIs:",
    "POST /api/events/ → Create event",
    "GET /api/alerts/ → List alerts",
    "PATCH /api/alerts/<id>/ → Update alert status (Admin only)",
    "Docs:",
    "Swagger → http://127.0.0.1:8000/swagger/",
    "ReDoc → http://127.0.0.1:8000/redoc/"
]
elements.append(Paragraph("API Endpoints", heading2))
elements.append(Paragraph(endpoints_intro, normal))
elements.append(ListFlowable([ListItem(Paragraph(e, normal)) for e in endpoints]))

# Build PDF
doc.build(elements)
print(f"PDF report generated: {pdf_file}")