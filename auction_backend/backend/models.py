from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser

import datetime
import uuid

class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)

class User(AbstractUser):
    username = None
    email           = models.EmailField(max_length=254, unique=True, editable=True)
    name            = models.CharField(max_length=30, default = uuid.uuid4, editable=True)
    surname         = models.CharField(max_length=30, default = uuid.uuid4, editable=True)
    # image           = models.ImageField(upload_to='profile_pic', default='default.jpg', editable=True)
    date_of_birth   = models.DateField(default=datetime.date.today, editable=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return f'{self.id}, {self.email}'

    
    def to_dict(self):
        return {
            'id'            : self.id,
            'email'         : self.email,
            'name'          : self.name,
            'surname'       : self.surname,
            # 'image'         : self.image,
            'date_of_birth' : self.date_of_birth,
        }