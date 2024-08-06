# Library Management System Django

## Description

A Library Management System built using Django to manage books and students. The system allows admins to add, edit, and delete books and student profiles, issue books to students, and manage book returns. Students can view available books and track the books issued to them.

## Technologies Used

- **Django**: Backend framework
- **Bootstrap**: Frontend framework for styling
- **SQLite**: Default database for development

## Installation

1. **Install Python**: Ensure Python is installed on your system.
2. **Install Dependencies**: Run `pip install -r requirements.txt` to install the required packages.
3. **Database Migrations**:
   - Run `python manage.py makemigrations`
   - Run `python manage.py migrate`
4. **Create Superuser**: Run `python manage.py createsuperuser` and enter the required details.
5. **Run the Server**: Execute `python manage.py runserver` and navigate to [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser to log in.

## User Types

- **Superuser/Admin**: Can manage students, books, issue books, delete returned books, and edit/delete profiles.
- **Regular User/Student**: Can log in, view book lists, and see books issued to them.

## Student Registration

1. Students fill out an information form.
2. Admin reviews the submitted information in the admin site.
3. Admin verifies the student and creates a new student profile.
4. Admin sends login credentials to the student via email.

## Adding New Books

Before adding new books, manually add the required genres and languages in the admin site at [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin). Regularly check the admin site for new student registrations.