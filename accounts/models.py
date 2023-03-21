from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractUser, PermissionsMixin
from employee_profile.models import Employee_profile

# Create your models here.

class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError("A user must have and email")

        else:
            email = self.normalize_email(email)
            user = self.model(email=email, username=username)
            user.set_password(password)
            user.save()

            Employee_profile.objects.create(user=user, first_name='', last_name='', phone='', city='')

            return user

    def create_superuser(self, email, username, password):
        if not email:
            raise ValueError("A superuser must have an email")

        else:
            user = self.create_user(email=email, username=username, password=password)
            user.is_staff = True
            user.is_superuser = True


            user.save()
            Employee_profile.objects.create(user=user)

class CustomUserModel(AbstractUser, PermissionsMixin):
    email = models.CharField(max_length=244, unique=True)
    username = models.CharField(max_length=244, unique=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username",]

    def __str__(self):
        return self.email