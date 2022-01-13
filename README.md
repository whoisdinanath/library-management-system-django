# Library Management System Django

## Installation

First of all install python on your system. Then run `pip install -r requirements.txt` to required settings.
Then run `python manage.py makemigration` `python manage.py migrate`.
Finally it's time to create superuser/admin who will be managing students and books!
Run `python manage.py createsuperuser` and enter the required data.
After that run `python manage.py runserver` and head over to the browser to http://127.0.0.1:8000 and login.

There are two types of user one is superuser/admin and another is regular user/students.
Superuser/Admin can add students, add books, issue books to student, delete the returned book, edit and delete books and students profile.

While, student can login and see books list and the books issued by them.
To register students have to fill up a information form and after that admin can view the informations sent by student in admin site and add a new student based on the details filled by the students in the information form if he/she is verified student of the given organizations.
Then admin will send the credentials created by them via email to the student and using those credentials student can login to the library.

Before adding new books please go to the http://127.0.0.1:8000/admin admin site and add the required genre and language manually as we cannot add genre and language through the site. And visit the admin site to see information form regularly as if someone had registered for the library.
