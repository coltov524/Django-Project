# 📚 Django Course Marketplace — Colțov Academy

Colțov Academy is a full-stack Django-based course marketplace platform where users can create, sell, and enroll in online courses. It is designed to simulate a real-world e-learning system with full support for instructor and student workflows.

The project focuses on backend development using Django, implementing authentication, course management, enrollment logic, and automated email notifications, with a clean and scalable architecture.

---

## Overview

Users can register, log in, and interact with a course marketplace. Instructors can publish and manage their own courses, while students can browse and enroll in courses created by others.

Each successful enrollment triggers an automatic confirmation email, improving user feedback and engagement.

The project is built using Django’s MVT architecture and uses Class-Based Views (CBVs) to ensure clean, reusable, and maintainable backend logic.

---

## Features

### Authentication System

* User registration and secure login/logout
* Password change functionality
* Session-based authentication
* Unique username and email validation

---

### Course Management (Instructor Side)

* Create, edit, and delete courses
* Upload course content and media files
* Ownership-based permissions (only course creator can modify)
* Structured course data (title, description, price, etc.)

---

### Marketplace (Student Side)

* Browse all available courses
* View detailed course pages
* Enroll/purchase courses instantly
* Prevent duplicate enrollments
* Clear separation between instructors and students

---

### Enrollment System

* Tracks user ↔ course relationships
* Secure enrollment logic
* Automatic enrollment processing
* Integration with email notification system

---

### Email Notifications

* SMTP-based email system (Gmail or compatible providers)
* Automatic confirmation email after enrollment
* Configurable via Django settings

---

## Architecture

The system follows Django’s MVT architecture with strong separation of concerns:

* Models: handle courses, users, and enrollments
* Views (CBVs): manage business logic and request handling
* Templates: handle frontend rendering
* Forms: manage validation and secure input processing

CBVs are used throughout the project to improve scalability, reduce repetition, and maintain clean structure.

The application is modular, separating user management and course functionality into distinct apps.

---

## Tech Stack

* Django (Python)
* HTML5, CSS3
* SQLite (default database)
* Django Authentication System
* SMTP Email Integration
* Class-Based Views (CBVs)
* Virtualenv environment

---

## Project Structure

Django-Project/
└── Django-project-main/
└── Proiect_Coltov/
└── Proiect/
├── manage.py
├── db.sqlite3
├── courses/
├── users/
├── templates/
├── static/
├── media/

---

## Installation & Setup

git clone [https://github.com/coltov524/Django-Project.git](https://github.com/coltov524/Django-Project.git)
cd Django-Project

python -m venv venv

Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

pip install -r requirements.txt

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver

---

## Email Configuration

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = '[your-email@gmail.com](mailto:your-email@gmail.com)'
EMAIL_HOST_PASSWORD = 'your-app-password'

Gmail requires an App Password instead of the regular account password.

---

## How It Works

A user registers and logs in, then gains access to the marketplace.

From there:

* Users can browse available courses
* Instructors can create and manage courses
* Students can enroll in courses

When a user enrolls:

* The system saves the enrollment in the database
* Links the user to the selected course
* Sends an automatic confirmation email

Each course is managed independently by its creator.

---

## Future Improvements

* Payment integration (Stripe / PayPal)
* Course rating and review system
* Advanced search and filtering
* Video hosting and streaming support
* REST API using Django REST Framework
* Deployment to cloud platforms (Render / Railway / AWS)

---

## Author

Colțov Tudor-Alexandru