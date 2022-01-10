from django.db import models
from django.contrib.auth.models import User
# Used to generate urls by reversing the URL patterns
from django.urls import reverse
from django.db.models.signals import post_save
from django.contrib.auth.models import PermissionsMixin
from django.utils.timezone import now
import uuid
import random
# relation containg all genre of books

from datetime import date, timedelta, datetime
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class MyAccountManager(BaseUserManager):
    def create_user(self, email, name, username, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            name=name,



        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
            name=name,

        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, unique=True,
                          default=uuid.uuid4, editable=False)
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    name = models.CharField(max_length=60, unique=False)
    username = models.CharField(max_length=30, unique=True)
    enrollment_no = models.IntegerField(
        unique=True, default=random.randint(10000, 99999))
    date_joined = models.DateTimeField(
        verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    pic = models.ImageField(blank=True, upload_to='students')
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'username']

    objects = MyAccountManager()

    def __str__(self):
        return f'{self.name}'

        # For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
        return self.is_admin

        # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True


class Genre(models.Model):
    name = models.CharField(
        max_length=200, help_text="Enter a book genre (e.g. Science Fiction, French Poetry etc.)")

    def __str__(self):
        return self.name
# __str__ method is used to override default string returnd by an object


# relation containing language of books
class Language(models.Model):
    name = models.CharField(max_length=200,
                            help_text="Enter the book's natural language (e.g. English, French, Japanese etc.)")

    def __str__(self):
        return self.name

# book relation that has 2 foreign key genre language
# book relation can contain multiple genre so we have used manytomanyfield


class Book(models.Model):
    id = models.UUIDField(primary_key=True, unique=True,
                          default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    summary = models.TextField(
        max_length=1000, help_text="Enter a brief description of the book")
    isbn = models.CharField('ISBN', max_length=13,
                            help_text='13 Character https://www.isbn-international.org/content/what-isbn')
    genre = models.ManyToManyField(
        Genre, help_text="Select a genre for this book")
    language = models.ForeignKey(
        'Language', on_delete=models.SET_NULL, null=True)
    total_copies = models.IntegerField()
    pic = models.ImageField(blank=True, null=True, upload_to='books')
    available_copies = models.IntegerField(name='available_copies')

    # __str__ method is used to override default string returnd by an object
    def __str__(self):
        return self.title


# relation containing info about Borrowed books
# it has  foriegn key book and student for refrencing book and student
# roll_no is used for identifing students
# if a book is returned than corresponding tuple is deleted from database
class Borrower(models.Model):
    id = models.UUIDField(primary_key=True, unique=True,
                          default=uuid.uuid4, editable=False)
    student = models.ForeignKey('Account', on_delete=models.CASCADE)
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    issue_date = models.DateField(
        null=True, blank=True, help_text='YYYY-MM-DD', default=date.today)
    return_date = models.DateField(
        null=True, blank=True, help_text='YYYY-MM-DD')

    def __str__(self):
        return self.student.name.title()+" borrowed "+self.book.title.title()

    def fine(self):
        today = date.today()
        fine = 0
        if self.return_date <= today:
            fine += 5 * (today - self.return_date).days
        return fine


class InformationForm(models.Model):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    name = models.CharField(max_length=60, unique=False)
    username = models.CharField(max_length=30, unique=True)
    student = models.BooleanField(default=False)

    def __str__(self):
        return self.email
