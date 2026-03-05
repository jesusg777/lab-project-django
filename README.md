# Studle - Student Management System

A Django-based web application designed for students to manage their academic schedules and subjects. This project was developed for the Software Lab 3 course.

## Features

- **Student Schedule**: View weekly class schedules.
- **Subject Management**:
  - Add new subjects.
  - Update existing subject details.
  - Delete subjects.
  - View detailed information for each subject.
- **Authentication**: Secure login for students.
- **Responsive Design**: Built with a custom Material Design theme.

## Tech Stack

- **Backend**: Django 3.2.6
- **Database**: PostgreSQL
- **Frontend**: HTML, CSS, JavaScript (Material Dashboard)

## Setup

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd Lab-project-django
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: .\env\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Configuration**
   Create a `.env` file in the root directory and add your database credentials:
   ```env
   DEBUG=True
   SECRET_KEY=your_secret_key
   DB_NAME=studleDb
   DB_USER=your_db_user
   DB_PASSWORD=your_db_password
   DB_HOST=your_db_host
   DB_PORT=5432
   ```

---

---

5. **Run Migrations**

   ```bash
   python manage.py migrate
   ```

6. **Start the server**
   ```bash
   python manage.py runserver
   ```

## Credits

- Base template: Material Dashboard Django by AppSeed & Creative Tim.
