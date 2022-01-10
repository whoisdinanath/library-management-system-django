from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
class Account(AbstractBaseUser, PermissionsMixin):
    email 					= models.EmailField(verbose_name="email", max_length=60, unique=True)
    name                    = models.CharField(max_length= 60, unique=False)
    username 				= models.CharField(max_length=30, unique=True)
    enrollment_no           = models.IntegerField( unique=True ,default=random.randint(10000, 99999) )
    date_joined				= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login				= models.DateTimeField(verbose_name='last login', auto_now=True)
    pic                     = models.ImageField(blank=True, upload_to='profile_image')
    is_admin				= models.BooleanField(default=False)
    is_active				= models.BooleanField(default=True)
    is_staff				= models.BooleanField(default=False)
    is_superuser			= models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'username', 'enrollment_no']

    objects = MyAccountManager()

    def __str__(self):
        return f'{self.name}'



print(Account)