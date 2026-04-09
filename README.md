📚 Django Course Marketplace

A web-based learning platform built with Django that enables users to create, sell, purchase, and enroll in online courses.
The platform is designed to simulate a real-world e-learning marketplace, offering both instructor and student functionalities.

One of the core features is the automated email notification system, which sends confirmation emails whenever a user enrolls in a course, improving user engagement and experience.

---

🚀 Core Features

- 👤 User Authentication System
  
  - Secure registration, login, and logout
  - Session-based authentication

- 📚 Course Management
  
  - Users can create and publish their own courses
  - Edit and delete existing courses
  - Structured course data (title, description, price, etc.)

- 💰 Marketplace Functionality
  
  - Users can browse available courses
  - Purchase or enroll in courses created by other users
  - Clear separation between buyers and sellers

- 🛒 Enrollment System
  
  - Seamless enrollment flow
  - Tracks user-course relationships

- 📧 Email Notification System
  
  - Automatic email sent upon successful enrollment
  - Configurable SMTP integration

- 🗂️ Course Browsing
  
  - List view of all available courses
  - Dedicated detail page for each course

- 🔐 Security & Data Handling
  
  - Django built-in protections (CSRF, authentication system)
  - Safe handling of user data

---

🧠 Project Purpose

This project was developed as a full-stack Django application to demonstrate:

- understanding of MVC (Model-View-Template) architecture
- ability to build a functional marketplace system
- implementation of backend logic with real-world use cases
- integration of email services within a web application

It can serve as a strong foundation for more advanced e-learning platforms.

---

🛠️ Tech Stack

- Backend: Django (Python)
- Frontend: HTML, CSS (can be extended with Bootstrap)
- Database: SQLite (default Django database)
- Email Service: SMTP (Gmail or other providers)
- Environment Management: Virtualenv

---

⚙️ Installation & Setup

Follow these steps to run the project locally:

# Clone the repository
git clone https://github.com/coltov524/Django-Project.git

# Navigate into the project folder
cd Django-Project

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Apply database migrations
python manage.py migrate

# Create a superuser (optional but recommended)
python manage.py createsuperuser

# Start the development server
python manage.py runserver

---

📧 Email Configuration

To enable email notifications, configure your email settings in "settings.py":

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'

⚠️ For Gmail, you will need to use an App Password, not your actual account password.

---

📌 How It Works

1. A user creates an account or logs in
2. Users can browse all available courses on the platform
3. A user can:
   - enroll in a course
   - or create and publish their own course
4. When enrolling in a course:
   - the system registers the enrollment
   - an email confirmation is automatically sent
5. Course creators can manage their own content

---

📈 Possible Improvements

To extend this project into a production-ready platform:

- 💳 Integrate payment systems (Stripe / PayPal)
- ⭐ Add course reviews and rating system
- 🔍 Implement search and filtering
- 📊 Create user dashboards (student & instructor)
- 📦 Add pagination for large datasets
- 🌐 Deploy the application (Render, Railway, AWS)
- 🔐 Improve permissions (roles: admin, instructor, student)
- 📱 Make UI responsive and modern (Bootstrap / Tailwind)

---

👨‍💻 Author

Developed by Colțov Tudor-Alexandru

---

⭐ Final Notes

This project represents a solid foundation for a real-world Django application and demonstrates essential backend development skills such as:

- data modeling
- user authentication
- business logic implementation
- email integration

