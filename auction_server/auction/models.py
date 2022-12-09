from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser

import datetime
import uuid

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields) # authenticate user with email instead of username
        user.set_password(password)
        user.save()
        return user 

    def create_superuser(self, email, password, **extra_fields):
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
            'password'      : self.password,
        }

class Question(models.Model):
    question = models.CharField(max_length=144, editable=True)
    answer = models.CharField(max_length=30, null=True, editable=True)
    owner = models.ForeignKey('auction.User',related_name='owner_set_question', on_delete=models.CASCADE)
    user = models.ForeignKey('auction.User', related_name='user_set', on_delete=models.CASCADE)
    item = models.ForeignKey('auction.Item', related_name='item_set', on_delete=models.CASCADE)

    
    def __str__(self):
        return f'{self.id}, {self.owner}, {self.user}'

    
    def to_dict(self):
        return {
            'id'         : self.id,
            'question'   : self.question,
            'answer'     : self.answer,
            'owner'      : self.owner,
            'user'       : self.user,
            'item'       : self.item
        }
        
class Item(models.Model):
    title = models.CharField(max_length=30, editable=True)
    description = models.CharField(max_length=144, editable=True)
    price = models.IntegerField(editable=True)
    #picture = models.ImageField(upload_to='./item_uploads', editable=True)
    #final_date   = models.DateField(default=datetime.datetime.now() + datetime.timedelta(days=7), editable=True)
    highest_bidder = models.ForeignKey('auction.User', null=True, related_name='highest_bidder_set', on_delete=models.CASCADE)
    owner = models.ForeignKey('auction.User', related_name='owner_set_item' ,on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.id}, {self.highest_bidder}, {self.owner}'

    
    def to_dict(self):
        return {
            'id'                : self.id,
            'title'             : self.title,
            'description'       : self.description,
            'price'             : self.price,
            #'picture'           : self.picture,
            #'final_date'         : self.final_date,
            'highest_bidder'     : self.highest_bidder,
            'owner'             : self.owner,
        }

class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='auction/static')

    def __str__(self):
        return self.title
        

   
