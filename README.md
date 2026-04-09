# Django CRUD Application

## Description

This project is a Django-based web application designed as a course platform where users can browse, enroll in, and sell courses. It provides full CRUD (Create, Read, Update, Delete) functionality for managing course-related data and integrates SMTP-based email notifications for user interactions.

The application follows Django’s MVT (Model-View-Template) architecture and demonstrates a structured and scalable approach to web development, including data management, routing, and dynamic content rendering.

---

## Features

* Create, read, update, and delete records
* Course platform functionality (browse, enroll, and sell courses)
* Email notifications using SMTP
* Structured Django project architecture
* Dynamic content rendering with templates
* Basic navigation and user interaction

---

## Technologies Used

* Python
* Django
* HTML
* CSS
* SMTP (email integration)

---

## Installation

### 1. Clone the repository

```bash id="5b1k2l"
git clone https://github.com/coltov524/Django-Project.git
cd Django-Project
```

### 2. Create a virtual environment

```bash id="3n8v7x"
python -m venv venv
```

### 3. Activate the virtual environment

* On Windows:

```bash id="8k2m1p"
venv\Scripts\activate
```

* On macOS/Linux:

```bash id="4t9q6z"
source venv/bin/activate
```

### 4. Install dependencies

```bash id="7y5u2w"
pip install -r requirements.txt
```

### 5. Configure environment variables

Create a `.env` file in the root directory and add the following:

```env id="2c6d8f"
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_password
EMAIL_USE_TLS=True
```

Note: Do not expose real credentials. Use environment variables for security.

---

### 6. Apply migrations

```bash id="1q2w3e"
python manage.py migrate
```

### 7. Run the development server

```bash id="9z8x7c"
python manage.py runserver
```

### 8. Access the application

Open your browser and navigate to the local development server URL provided in the terminal (typically `http://127.0.0.1:8000/`).

---

## Project Structure

The project follows Django’s standard structure:

* `models.py` – database models
* `views.py` – application logic
* `templates/` – HTML templates
* `urls.py` – routing configuration

---

## What I Learned

* Building web applications using Django
* Implementing CRUD operations in a real-world scenario
* Developing a course platform with user interaction
* Integrating SMTP for sending emails
* Structuring and organizing a scalable Django project

---

## Future Improvements

* Add user authentication (login/register)
* Implement REST API using Django REST Framework
* Improve UI/UX design
* Deploy the application to a cloud platform

---

## Author

Colțov Tudor-Alexandru


